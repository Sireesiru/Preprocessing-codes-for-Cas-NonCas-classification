# Preprocessing codes for Cas-NonCas classification
The different codes we used for preprocessing to genrating classification models used in the structure based classification of Cas/Non-Cas

#Overview
Clustered Regularly Interspaced Short Palindromic Repeats and CRISPR-associated protein 9 (CRISPR/Cas9) is a revolutionary genome editing technology that allows precise targeted changes to the DNA finding profound implications in medical research and alied fields. However, Cas9 proteins suffer from inherent limitaions like reduced specificity and off-target effects limiting thier applicability.This can be adressed by studying the strucutural aspects of Cas9 proteins. Leveraging machine learning classification models built on 3D structural information of CAS9 proteins, we aim to identify key inter-residue distances contributing to overall stability and allosteric mechanisms of CRISPR/Cas9 proteins.This repository contains data, end to end scripts and methodologies used in our study. Here we developed a unique multi-step pre-processing pipeline that encode the 3D structural information of Cas9 and Non-Cas proteins into 1D vector bits. The steps include 1) calculating Ca-Ca distances between every pair of residues within the protein generating the distance matrix 2) Flatten lower daigonal of the matrix into dataframe columns containing all residue-types and distances within the protein3) Grouping these distances within columns of 210 pairs of all known amino acids based on the residue-type. 4) Histogram transformation of the distances 5)Concatenate the bin values into 1D vector. We performed 2-stage feature selection on vectors of two differnt bit size each identifing top bits which are further used in building RF models for Cas9 and Non-Cas protein classification. Analysing top bits identified important residue-pairs and distances governing the overall strucutal integrity of Cas9 proteins.These distances can guide future structural modification withn Cas9 strucure facilitating the development of novel engineered variants with improved specificity. 

#Key Highlights
Objective: Develop a structure-based ML model to identify important inter-residue interactions in Cas9 proteins.

#Methodology:

1) Muti-step feature Encoding: Convert 3D structural information of proteins into bit-representation feature vectors.
2) Machine learning: Random Forest (RF) for classification.
3) Refined analysis: Perform a two-stage Use SHapley Additive exPlanations (SHAP) feature selection to pinpoint critical residue pairs.
