# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:10:36 2023

@author: RATUL BHOWMIK
"""


import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import os
import base64
import pickle

# The App
st.title('💊 HDAC-Pred app')
st.info('HDAC-Pred allows users to predict bioactivity of a query molecule against the Human Histone Deacetylase target protein.')



# loading the saved models
bioactivity_first_model = pickle.load(open('pubchem.pkl', 'rb'))
bioactivity_second_model = pickle.load(open('substructure.pkl', 'rb'))
bioactivity_third_model = pickle.load(open('descriptors.pkl', 'rb'))

# Define the tabs
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['Main', 'About', 'What is Human Histone Deacetylase (HDAC)?', 'Dataset', 'Model performance', 'Python libraries', 'Citing us', 'Application Developers'])

with tab1:
    st.title('Application Description')
    st.success(
        " This module of [**HDAC-Pred**](https://github.com/RatulChemoinformatics/HDAC-Pred) has been built to predict bioactivity and identify potent inhibitors against Human Histone Deacetylase using robust machine learning algorithms."
    )

# Define a sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        'Choose a prediction model',
        [
            'HDAC prediction model using pubchemfingerprints',
            'HDAC prediction model using substructurefingerprints',
            'HDAC prediction model using 1D and 2D molecular descriptors',
        ],
    )

# HDAC prediction model using pubchemfingerprints
if selected == 'HDAC prediction model using pubchemfingerprints':
    # page title
    st.title('Predict bioactivity of molecules against HDAC using pubchemfingerprints')

    # Molecular descriptor calculator
    def desc_calc():
        # Performs the descriptor calculation
        bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        os.remove('molecule.smi')

    # File download
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
        return href

    # Model building
    def build_model(input_data):
        # Apply model to make predictions
        prediction = bioactivity_first_model.predict(input_data)
        st.header('**Prediction output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        df = pd.concat([molecule_name, prediction_output], axis=1)
        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    # Sidebar
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
        st.sidebar.markdown("""
        [Example input file](https://github.com/RatulChemoinformatics/QSAR/blob/main/predict.txt)
        """)

    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep=' ', header=None)
            load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

            st.header('**Original input data**')
            st.write(load_data)

            with st.spinner("Calculating descriptors..."):
                desc_calc()

            # Read in calculated descriptors and display the dataframe
            st.header('**Calculated molecular descriptors**')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            # Read descriptor list used in previously built model
            st.header('**Subset of descriptors from previously built models**')
            Xlist = list(pd.read_csv('pubchem.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            # Apply trained model to make prediction on query compounds
            build_model(desc_subset)
        else:
            st.warning('Please upload an input file.')

# HDAC prediction model using substructurefingerprints
elif selected == 'HDAC prediction model using substructurefingerprints':
    # page title
    st.title('Predict bioactivity of molecules against HDAC using substructurefingerprints')

    # Molecular descriptor calculator
    def desc_calc():
        # Performs the descriptor calculation
        bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/SubstructureFingerprinter.xml -dir ./ -file descriptors_output.csv"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        os.remove('molecule.smi')

    # File download
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
        return href

    # Model building
    def build_model(input_data):
        # Apply model to make predictions
        prediction = bioactivity_second_model.predict(input_data)
        st.header('**Prediction output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        df = pd.concat([molecule_name, prediction_output], axis=1)
        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    # Sidebar
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
        st.sidebar.markdown("""
        [Example input file](https://raw.githubusercontent.com/dataprofessor/bioactivity-prediction-app/main/example_acetylcholinesterase.txt)
        """)

    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep=' ', header=None)
            load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

            st.header('**Original input data**')
            st.write(load_data)

            with st.spinner("Calculating descriptors..."):
                desc_calc()

            # Read in calculated descriptors and display the dataframe
            st.header('**Calculated molecular descriptors**')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            # Read descriptor list used in previously built model
            st.header('**Subset of descriptors from previously built models**')
            Xlist = list(pd.read_csv('substructure.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            # Apply trained model to make prediction on query compounds
            build_model(desc_subset)
        else:
            st.warning('Please upload an input file.')
            
            
# HDAC prediction model using 1D and 2D molecular descriptors
if selected == 'HDAC prediction model using 1D and 2D molecular descriptors':
    # page title
    st.title('Predict bioactivity of molecules against HDAC using 1D and 2D molecular descriptors')

    # Molecular descriptor calculator
    def desc_calc():
        # Performs the descriptor calculation
        bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -2d -descriptortypes ./PaDEL-Descriptor/descriptors.xml -dir ./ -file descriptors_output.csv"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        os.remove('molecule.smi')

    # File download
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
        return href

    # Model building
    def build_model(input_data):
        # Apply model to make predictions
        prediction = bioactivity_third_model.predict(input_data)
        st.header('**Prediction output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name='molecule_name')
        df = pd.concat([molecule_name, prediction_output], axis=1)
        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    # Sidebar
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input file", type=['txt'])
        st.sidebar.markdown("""
        [Example input file](https://raw.githubusercontent.com/dataprofessor/bioactivity-prediction-app/main/example_acetylcholinesterase.txt)
        """)

    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep=' ', header=None)
            load_data.to_csv('molecule.smi', sep='\t', header=False, index=False)

            st.header('**Original input data**')
            st.write(load_data)

            with st.spinner("Calculating descriptors..."):
                desc_calc()

            # Read in calculated descriptors and display the dataframe
            st.header('**Calculated molecular descriptors**')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            # Read descriptor list used in previously built model
            st.header('**Subset of descriptors from previously built models**')
            Xlist = list(pd.read_csv('descriptors.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            # Apply trained model to make prediction on query compounds
            build_model(desc_subset)
        else:
            st.warning('Please upload an input file.')
            
            
with tab2:
  coverimage = Image.open('Logo.png')
  st.image(coverimage)
with tab3:
  st.header('What is HDAC?')
  st.write('HDAC stands for Histone Deacetylase, an enzyme involved in regulating gene expression by modifying histone proteins. They play a role in epigenetic processes, influencing how genes are turned on or off without altering the underlying DNA sequence. There are different classes of HDACs, grouped into zinc-dependent and NAD+-dependent families. Inhibition of HDACs is a potential therapeutic approach for various diseases, including cancer, due to their involvement in cell cycle regulation. HDAC inhibitors can affect not only histones but also non-histone proteins, influencing diverse cellular processes. HDACs are part of the larger histone modification machinery, working in concert with histone acetyltransferases (HATs) to maintain chromatin. The balance between histone acetylation and deacetylation is crucial for proper cellular function and development.')
with tab4:
  st.header('Dataset')
  st.write('''
    In our work, we retrieved a Human Histone Deacetylase (HDAC) dataset from the ChEMBL database. The data was curated and resulted in a non-redundant set of 2677 HDAC inhibitors, which can be divided into:
    - 1684 active compounds
    - 549 inactive compounds
    - 444 intermediate compounds
    ''')
with tab5:
  st.header('Model performance')
  st.write('We selected a total of 3 different molecular signatures namely pubchem fingerprints, substructure fingerprints, and 1D 2D molecular descriptors to build the web application. The correlation coefficient, RMSE, and MAE values for the pubchem fingerprint model was found to be 0.9756, 0.2963, and 0.2254. The correlation coefficient, RMSE, and MAE values for the substructure fingerprint model was found to be 0.9599, 0.3239, and 0.2531. The correlation coefficient, RMSE, and MAE values for the 1D and 2D molecular descriptor model was found to be 0.982, 0.296, and 0.2282')
with tab6:
  st.header('Python libraries')
  st.markdown('''
    This app is based on the following Python libraries:
    - `streamlit`
    - `pandas`
    - `rdkit`
    - `padelpy`
  ''')
with tab7:
  st.markdown('Anjum A, Farooqi H, Abdin MZ, Tiwari AK. Combinatorial effect of Macrotyloma uniflorum (Lam.) Verdc. seed extract and vorinostat (suberoylanilide hydroxamic acid) in human leukemia cells, ***Pharmacognosy Magazine*** (2022). DOI: https://dx.doi.org/10.4103/pm.pm_70_21.')
with tab8:
  st.markdown('Ratul Bhowmik, Amber Rizwan, Dr. Humaira Farooqi. [***Phytomedicine and Cancer Biology Lab, Department of Biotechnology, Jamia Hamdard, New Delhi, India***] ')