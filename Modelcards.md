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

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

{{ direct_use | default("[More Information Needed]", true)}}


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

{{ out_of_scope_use | default("[More Information Needed]", true)}}

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

{{ bias_risks_limitations | default("[More Information Needed]", true)}}

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

{{ bias_recommendations | default("Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.", true)}}

## How to Get Started with the Model

Use the code below to get started with the model.

{{ get_started_code | default("[More Information Needed]", true)}}

## Training Details

### Training Data

We described the data pooling here in more detail: https://doi.org/10.1016/j.esmorw.2025.100172 
In brief, the BALANCE dataset comprises six cohorts with a total of 6316 female, non-metastatic breast cancer patients, including trial data (European Organisation for Research and Treatment of Cancer (EORTC) AMAROS), real-world data (Netherlands Cancer Institute (NKI), district hospital Kufstein, Austria), and observational studies (UMBRELLA, OPTIMUM, and VERDI). Data were collected between 2001 and 2024 and encompass patients receiving active treatment, follow-up, or survivorship care from multiple European countries. 

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

{{ preprocessing | default("[More Information Needed]", true)}}


#### Training Hyperparameters

- **Training regime:** {{ training_regime | default("[More Information Needed]", true)}} <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

{{ speeds_sizes_times | default("[More Information Needed]", true)}}

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

{{ testing_data | default("[More Information Needed]", true)}}

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

{{ testing_factors | default("[More Information Needed]", true)}}

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

{{ testing_metrics | default("[More Information Needed]", true)}}

### Results

{{ results | default("[More Information Needed]", true)}}

#### Summary

{{ results_summary | default("", true) }}

## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

{{ model_examination | default("[More Information Needed]", true)}}




## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

{{ citation_bibtex | default("[More Information Needed]", true)}}

**APA:**

{{ citation_apa | default("[More Information Needed]", true)}}


## More Information [optional]

