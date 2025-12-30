# Common Model Card for 14 models predicting impaired HRQOL in early breast cancer patients

Time-dynamic machine learning models that predict clinically relevant HRQOL impairments in 14 EORTC QLG-C30 domains. 

## Model Details

### Model Description

Health-related quality of life was measured with the EORTC QLQ-C30. Symptom (fatigue, nausea and vomiting, pain, dyspnoea, insomnia, appetite loss, constipation, diarrhoea, and financial difficulties) and functioning scales (physical, role, emotional, cognitive, and social) are reported on a 4-point Likert scale (“Not at all”, “A bit”, “Quite a bit”, and “Very much”) and transformed to linear scores ranging from 0 to 100 scale. We dichotomized the outcomes according to the established thresholds for clinical importance (TCI) to indicate clinically relevant impairments, defined as scores associated with at least one of the following patient-reported concerns: limitations in daily life, need for help or care, and worries of the patient or their partner/family.

- **Developed by:** Niclas J Hubel, Benjamin Murauer
- **Funded by:** European Organisation for Research and Treatment of Cancer (EORTC) Quality of Life Group, grant number 007-2022 (EORTC 2052). 
- **Model type:** Classifiers based on tabular data
- **License:** No license

### Model Sources 

- **Repository:** https://github.com/NJHubel/BALANCE-ML/blob/main/README.md  
- **Paper:** LINK ME

## Uses

Models can be used for research purposes. 

### Direct Use

We DO NOT recommend direct use of the models in any clinical context!  

## Bias, Risks, and Limitations

Model biases for the following risk groups have been evaluated:

(1) Patients post menopause, 
(2) Patients with financial difficulties, 
(3) Patients with obesity (BMI >= 30), 
(4) Patients with 2 or more comorbidities, 
(5) Patients with lower educational status (secondary education or lower), 
(6) Patients with frailty 

Results are mixed and need to be evaluated on a case-by-case basis. 

## Training Details

### Training Data

We described the data pooling here in more detail: https://doi.org/10.1016/j.esmorw.2025.100172 
In brief, the BALANCE dataset comprises six cohorts with a total of 6316 female, non-metastatic breast cancer patients, including trial data (European Organisation for Research and Treatment of Cancer (EORTC) AMAROS), real-world data (Netherlands Cancer Institute (NKI), district hospital Kufstein, Austria), and observational studies (UMBRELLA, OPTIMUM, and VERDI). Data were collected between 2001 and 2024 and encompass patients receiving active treatment, follow-up, or survivorship care from multiple European countries. 

## Evaluation

Model evaluation was performed in real-world data from the Netherlands Cancer Institute. 

## Citation



## More Information

For more information please refer to the referenced publication. 
