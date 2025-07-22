# This Notebook contains the preprocessing steps for the BALANCE models that predict the next assessment

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from constants import targets, get_one_hot_encoded_columns

df0 = pd.read_csv('data/2025-04-11_balance.csv', sep=',', low_memory=False)

print("ATTENTION: Select the Sources that should be included in the dataset: \n"
      "1=KUFSTEIN, 2=NKI 3=UMBRELLA, 4=OPTIMUM, 5= VERDI, 7=AMAROS ")

# removing NKI from the data set as it is later used for external validation
df1 = df0[df0["Source"] != 2]

# drop columns with zero variance
to_be_dropped = [col for col in df1.columns if df1[col].nunique() <= 1]
print(f'dropping columns with zero variance: {to_be_dropped}')
df2 = df1.drop(columns=to_be_dropped)

# drop assessments that have no assessment_date_days field
df3 = df2.dropna(subset=['Assessment_date_days'])

# drop all patients that have only one assessment date
assessment_counts = df3.groupby('BALANCE_ID').count()['Source']
patients_with_two_assessments = assessment_counts[
    assessment_counts > 1].index.values
df4 = df3[df3.BALANCE_ID.isin(patients_with_two_assessments)]

ohe = OneHotEncoder()
one_hot_encoded = get_one_hot_encoded_columns(df4)
raw_data = ohe.fit_transform(df4[one_hot_encoded]).todense()
one_hot_column_names = ohe.get_feature_names_out(one_hot_encoded)
df_one_hot = pd.DataFrame(raw_data, columns=one_hot_column_names)
df_one_hot.index = df4.index
df5 = pd.concat([df4.drop(columns=one_hot_encoded), df_one_hot], axis=1)
df5.columns = df5.columns.str.replace(r'\.0$', '', regex=True)

# Sort the data to ensure temporal ordering within each BALANCE_ID
df = df5.dropna(subset=targets).sort_values(by=['BALANCE_ID', 'Assessment_date_days'])

df.to_pickle('data/cached_df.pckl')
df.to_csv('data/balance_analysis_set.csv')

# the splitting of the data is one of the most important aspects of this code.
# the result of the following block are the pairs of assessments:
# for each patient, all combinations of that patient's assessments are compiled into a
# list. The difference between the assessment dates is stored in a new column called
# "time_diff".
# for each such pair, the correct "output" is defined as the value from the later
# assessment of that pair.
# For example, if a patient has the following assessments:
#
# assessment |       date | C30_Q1 | ... | C30_FA score
# -----------+------------+--------+-----+-------------
#         A1 | 01.01.2001 |      3 | ... |           74
#         A2 | 01.02.2001 |      4 | ... |           80
#         A3 | 01.04.2001 |      2 | ... |           70
#
# then the result for that patient will be:
#
#    Pair | P1_C30_Q1 | P1_C... | time_diff | C30_FA score
# --------|-----------|---------|-----------|-----------|-------------
# A1 + A2 |         3 |     ... |        31 |           80
# A1 + A3 |         3 |     ... |        59 |           70
# A2 + A3 |         4 |     ... |        28 |           70
#
# Note that the raw data of the second assessment of each pair is not part of the pair


Xs, ys = [], []
patient_ids = df.BALANCE_ID.unique()
for patient_id in patient_ids:
    pdf = df[df.BALANCE_ID == patient_id]
    for i in range(0, pdf.shape[0] - 1):
        for j in range(i + 1, pdf.shape[0]):
            assessment0 = pdf.iloc[i].copy()
            assessment1 = pdf.iloc[j]

            time_diff = assessment1['Assessment_date_days'] - assessment0['Assessment_date_days']
            assessment0['time_diff'] = time_diff
            Xs.append(assessment0)
            ys.append(assessment1[['BALANCE_ID'] + targets])


# Convert to DataFrames
X = pd.DataFrame(Xs).reset_index(drop=True)
y = pd.DataFrame(ys).reset_index(drop=True)

# there should be as many rows in y as there are in X
assert X.shape[0] == y.shape[0]

y.to_pickle('data/cached_y.pckl')
X.to_pickle('data/cached_X.pckl')

# Impute missing values in X
iterative_imputer = IterativeImputer(verbose=2)
X_imputed = pd.DataFrame(iterative_imputer.fit_transform(X), columns=X.columns)

X_imputed.to_pickle('data/cached_X_imputed.pckl')