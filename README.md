# HDAC Cancer Inhibitory Prediction App

## Overview
This repository hosts a web-based application that predicts the HDAC (Histone Deacetylase) inhibitory potential of compounds—a key factor in cancer therapy research. The project leverages machine learning models trained on curated molecular data to estimate pIC50 values, providing a rapid in silico screening tool for potential HDAC inhibitors.

## About the Project
The app is built using Python and Streamlit, offering an interactive interface for researchers and students. It integrates various molecular descriptors—including PubChem Fingerprints, Substructure Fingerprints, and 1D/2D Molecular Descriptors—to generate predictions using a Random Forest model. This work is part of an ongoing research initiative aimed at developing novel computational methods for identifying cancer-inhibitory compounds.

**Important Note:** An accompanying research paper detailing the methodology and initial results is included in this repository. However, the paper is currently under review and unpublished. To protect the confidentiality and intellectual property of the research, detailed experimental data and proprietary processing methods have been intentionally omitted from public disclosure. Only summary information is provided here.

## Key Features
- **Interactive Web Interface:** Easily upload input files and select molecular descriptor types.
- **Robust Prediction Models:** Uses multiple molecular fingerprint approaches and descriptors for accurate pIC50 predictions.
- **Streamlined Workflow:** Seamless integration from data input to prediction output.
- **Research-Driven:** Based on rigorous machine learning techniques and statistical validation, with methodologies developed as part of ongoing research.

## Repository Contents
- **App Code:** Python scripts and notebooks for the Streamlit web application.
- **Model Training:** Code for data preprocessing, feature extraction, and Random Forest model training.
- **Supporting Files:** Configuration files, dependency lists, and utility scripts.
- **Research Paper Draft:** An unpublished manuscript that summarizes the project’s background, methodology, and initial findings. (Access to full details is restricted to protect intellectual property.)

## Contact & Collaboration
For research collaborations, inquiries about the methodology, or access to further details of the unpublished paper, please contact:
- **Email:** gn8360@myamu.ac.in

## Acknowledgments
- **ChEMBL Database:** For providing the essential bioactivity data used in model training.
- **Open-Source Community:** For the numerous libraries and tools (such as Streamlit, scikit-learn, and RDKit) that made this project possible.

## Disclaimer
*The research paper included in this repository is unpublished and currently under review. Detailed experimental data and proprietary methodologies have been intentionally omitted to protect ongoing research efforts.*

## License
This project is proprietary. All rights are reserved. Unauthorized use, reproduction, or distribution of this work, in whole or in part, is strictly prohibited without prior written permission from the author.
