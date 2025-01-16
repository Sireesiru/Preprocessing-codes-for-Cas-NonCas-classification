# Codes for Strucure-Based Model for Ca9 Vs. NonCas classification

Clustered Regularly Interspaced Short Palindromic Repeats and CRISPR-associated protein 9 (CRISPR/Cas9) is a revolutionary genome editing technology that allows precise targeted changes to the DNA finding profound implications in medical research and alied fields. However, Cas9 proteins suffer from inherent limitaions like reduced specificity and off-target effects limiting thier applicability.This can be adressed by studying the strucutural aspects of Cas9 proteins. Leveraging machine learning classification models built on 3D structural information of CAS9 proteins, we aim to identify key inter-residue distances contributing to overall stability and allosteric mechanisms of CRISPR/Cas9 proteins.This repository contains data, end to end scripts and methodologies used in our study. Here we developed a unique multi-step pre-processing pipeline that encode the 3D structural information of Cas9 and Non-Cas proteins into 1D vector bits. The steps include 1) calculating Ca-Ca distances between every pair of residues within the protein generating the distance matrix 2) Flatten lower daigonal of the matrix into dataframe columns containing all residue-types and distances within the protein3) Grouping these distances within columns of 210 pairs of all known amino acids based on the residue-type. 4) Histogram transformation of the distances 5)Concatenate the bin values into 1D vector. We performed 2-stage feature selection on vectors of two differnt bit size each identifing top bits which are further used in building RF models for Cas9 and Non-Cas protein classification. Analysing top bits identified important residue-pairs and distances governing the overall strucutal integrity of Cas9 proteins.These distances can guide future structural modification withn Cas9 strucure facilitating the development of novel engineered variants with improved specificity. 

The workflow involves:
1. **Data Preparation:** Cleaning and transforming raw data (`src/1_data_prep.py`).
2. **Feature Extraction:** Extracting features from the prepared data (`src/2_feature_extraction.py`).
3. **Classification:** Using extracted features for classification (`src/3_classification.py`)


## Getting Started

### Requirements
- Python 3.8+
- Boruta 0.3
  ```bash
pip install Boruta
  
### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/my_project.git
   cd my_project
2. Prepare the data:
   ```bash
   python src/1_data_prep.py
3. Run feature extraction
   ```bash
   python src/2_feature_extraction.py   
5. Perform classification
   ````bash
   python src/3_classification.py

