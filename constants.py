def get_one_hot_encoded_columns(df):
    all_one_hot_encoded = [
        "Marital_status",
        "Education_status",
        "Diag_code",
        "Lateralisation",
        "Location_code",
        "Histology_code",
        "Differentation_grade",
        'Country',
        'T_staging',
        'N_staging',
        "Stage",
        "Her2Neu_status",
        "T_staging_postOP",
        "N_staging_postOP",
        "Stage_postOP",
        *[f'Treatment_{i}' for i in range(1, 12)]
    ]
    return [c for c in all_one_hot_encoded if c in df.columns]

targets = ['C30_FA_class', 'C30_PA_class', 'C30_NV_class', 'C30_SL_class',
           'C30_DY_class', 'C30_AP_class', 'C30_CO_class', 'C30_DI_class',
           'C30_FI_class', 'C30_PF2_class', 'C30_RF2_class', 'C30_SF_class',
           'C30_EF_class', 'C30_CF_class']


def get_feature_sets(df):
    feature_sets = {'C30_raw_answers': [f"C30_Q{i}" for i in range(1, 31)],

                    'BR_23_raw_answers': [f"BR23_Q{i}" for i in range(31, 54)],

                    'Patient_characteristics': ['RWD', 'Assessment_date_days', 'Age_TX',
                                                'BMI_T0',
                                                'Menopause', 'Vital_status',
                                                'Survival_duration', 'Comorbidities'] +
                                               [col for col in df.columns if
                                                col.startswith("Education_status")] +
                                               [col for col in df.columns if
                                                col.startswith("Marital_status")],

                    'Disease_characteristics': ["M_staging", 'ER_status', 'ER_stat_cat',
                                                'PR_status', 'PR_stat_cat',
                                                "M_staging_postOP"] +
                                               [col for col in df.columns if
                                                col.startswith("Location_code")] +
                                               [col for col in df.columns if
                                                col.startswith("Lateralisation")] +
                                               [col for col in df.columns if
                                                col.startswith("Diag_code")] +
                                               [col for col in df.columns if
                                                col.startswith("Histology_code")] +
                                               [col for col in df.columns if
                                                col.startswith(
                                                    "Differentation_grade")] +
                                               [col for col in df.columns if
                                                col.startswith("T_staging_")] +
                                               [col for col in df.columns if
                                                col.startswith("N_staging_")] +
                                               [col for col in df.columns if
                                                col.startswith("Stage")] +
                                               [col for col in df.columns if
                                                col.startswith("Her2Neu_status")],

                    'Treatment_characteristics': ['Surgery', 'Radiotherapy',
                                                  'Chemotherapy', 'Neo_Chemo',
                                                  'Immunotherapy',
                                                  'Neo_Immuno', 'Hormonaltherapy',
                                                  'Neo_Hormonal',
                                                  'Start_date_TR1', 'Stop_date_TR1',
                                                  'Start_date_TR2', 'Stop_date_TR2',
                                                  'Start_date_TR3', 'Stop_date_TR3',
                                                  'Start_date_TR4', 'Stop_date_TR4',
                                                  'Start_date_TR5', 'Stop_date_TR5',
                                                  'Start_date_TR6', 'Stop_date_TR6',
                                                  'Start_date_TR7', 'Stop_date_TR7',
                                                  'Start_date_TR8', 'Stop_date_TR8',
                                                  'Start_date_TR9', 'Start_date_TR10',
                                                  'Start_date_TR11', ] +
                                                 [col for col in df.columns if
                                                  col.startswith("Treatment_")]
                    }

    feature_sets['all'] = [*feature_sets['C30_raw_answers'],
                           *feature_sets['BR_23_raw_answers'],
                           *feature_sets['Patient_characteristics'],
                           *feature_sets['Disease_characteristics'],
                           *feature_sets['Treatment_characteristics']]
    return feature_sets
