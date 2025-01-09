import streamlit as st
import pandas as pd
from PIL import Image
import subprocess
import base64
import os
import pickle


st.title('HDAC Bioactivity Prediction App - 💊')
st.info('This webapp is used to predict the pIC50 values of compounds to get the bioactiity of the compounds with respect to their inhibitory characteristics against HDAC.')

#defining the tabs that will be present just above the webapp
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['Main','About','What is Human Histone Deacetylase (HDAC)?','Dataset','Model Performance', 'Python Libraries', 'Citing Us', 'Application Developer'])

with tab1:
    st.title('Application Working and Description')
    st.success('This module of [**HDAC-Pred**] has been built to predict bioactivity and identify potent inhibitors against Human Histone Deacetylase using robust machine learning algorithms.')
    
    st.markdown('''Contributors:\n
    Faiq Alam - Worked on computational design, machine learning modeling, and bioactivity prediction.\n
    Amber Rizwan and Humaira Farooqi: Focused on experimental validation and laboratory testing of the compounds at the[Phytomedicine and Cancer Laboratory, Department of Biotechnology, SCLS, Jamia Hamdard].
    ''')

with tab2:
    st.title('About the Process')
    image = Image.open('Logo.png')
    st.image(image, use_container_width= True)

with tab3:
    st.title('What is Histone Deacetylase (HDAC)?')
    st.write("HDAC stands for Histone Deacetylase, an enzyme involved in regulating gene expression by modifying histone proteins. They play a role in epigenetic processes, influencing how genes are turned on or off without altering the underlying DNA sequence. There are different classes of HDACs, grouped into zinc-dependent and NAD+-dependent families. Inhibition of HDACs is a potential therapeutic approach for various diseases, including cancer, due to their involvement in cell cycle regulation. HDAC inhibitors can affect not only histones but also non-histone proteins, influencing diverse cellular processes. HDACs are part of the larger histone modification machinery, working in concert with histone acetyltransferases (HATs) to maintain chromatin. The balance between histone acetylation and deacetylation is crucial for proper cellular function and development.")

with tab4:
    st.header("Training Dataset Information")
    st.write('''
    In our work, we retrieved a Human Histone Deacetylase (HDAC) dataset from the ChEMBL database. The data was curated and resulted in a non-redundant set of 2677 HDAC inhibitors, which was divided into:
    - 1684 active compounds
    - 549 inactive compounds
    - 444 intermediate compounds
    ''')

with tab5:
    st.header('Model Performance')
    st.write("We selected a total of 3 different molecular signatures namely pubchem fingerprints, substructure fingerprints, and 1D 2D molecular descriptors to build the web application. The correlation coefficient, RMSE, and MAE values for the pubchem fingerprint model was found to be 0.9756, 0.2963, and 0.2254. The correlation coefficient, RMSE, and MAE values for the substructure fingerprint model was found to be 0.9599, 0.3239, and 0.2531. The correlation coefficient, RMSE, and MAE values for the 1D and 2D molecular descriptor model was found to be 0.982, 0.296, and 0.2282")

with tab6:
    st.title("Python Libraries Used in the App")
    st.markdown('''
    This app makes use of the following libraries:
    - 'streamlit'
    - 'pandas'
    - 'rdkit'
    - 'padelpy'
    - 'pickle'
    - 'lazypredict'
    ''')

with tab7:
    st.write('In the process of publishing')

with tab8:
    st.markdown('Faiq, Amber Rizwan, Humaira Farooqi. [***Phytomedicine and Cancer laboratory, Department of Biotechnology,SCLS Jamia Hamdard***]')





## Function to  calculate the molecular descriptors
# def desc_calc():
#     bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
#     process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#     output, error = process.communicate()
#     os.remove('molecule.smi')

#File Download Function
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href


def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href

# #Model Building Function

# def build_model(input_data):
#     load_model = pickle.load(open('pubchem.pkl', 'rb'))

#     #using the model to make prediction
#     prediction = load_model.predict(input_data)
#     st.header('**Prediction Output**')
#     prediction_output = pd.Series(prediction, name='pIC50')
#     molecule_name = pd.Series(load_data[1], name ='Molecule_Name')
#     df= pd.concat([molecule_name,prediction_output], axis=1)

#     st.write(df)
#     st.markdown(filedownload(df), unsafe_allow_html=True)

# #displaying the logo image of the webpage
# image = Image.open('Logo.png')


# st.image(image, use_container_width = True)




#function for downloading file
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    return href






#defining functions for fingerprint and descriptors calculation

#pubchem fingerprint calculation
def pubchem_calc():
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')


#substructure fingerprint calculation
def substructure_calc():
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/SubstructureFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')


#1D-2D Descriptor Calculator
def descriptor_calc():
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -2d -descriptortypes ./PaDEL-Descriptor/descriptors.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')















#defining SIDEBAR for uploading and files and selecting different prediction fingerprints
with st.sidebar:
    selected = st.selectbox(
        'Choose Prediction Fingerprint Model',
        [
            'HDAC prediction model using pubchemfingerprints',
            'HDAC prediction model using substructurefingerprints',
            'HDAC prediction model using 1D and 2D molecular descriptors',
        ],
    )

if selected == 'HDAC prediction model using pubchemfingerprints':
    st.title("Predicting Bioactivity of Uploaded Compounds using their Pubchem Fingerprints")

    # #pubchem fingerprint calculator
    # def desc_calc():
    #     bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    #     process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #     output, error = process.communicate()
    #     os.remove('molecule.smi')

    # #File Download Function
    # def filedownload(df):
    #     csv = df.to_csv(index = False)
    #     b64 = base64.b64encode(csv.encode()).decode()
    #     href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    #     return href
    
    #Model Building Function

    def pubchem_model(input_data):
        load_model = pickle.load(open('pubchem.pkl', 'rb'))

        #using the model to make prediction
        prediction = load_model.predict(input_data)
        st.header('**Prediction Output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name ='Molecule_Name')
        df= pd.concat([molecule_name,prediction_output], axis=1)

        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)


    #sidebar
    with st.sidebar.header('Upload the CSV Data Below:'):
        uploaded_file = st.sidebar.file_uploader("Upload the input file", type = ['txt','csv'])

    #Clicking the Predict Buttone and what to do when predict is clicked
    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep = ' ', header = None)
            load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False )

            st.header('***Original Input Data***')
            st.write(load_data)

            with st.spinner("Calculating Descriptors..."):
                pubchem_calc()
            

            #reading and displaying the calculated descriptors
            st.header('**Calculated Molecular Descriptors:')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            st.header('**Subset of Descriptors chosen from Previously built model:**')
            Xlist = list(pd.read_csv('pubchemtxt.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            #applying trained model to make prediction on query compounds
            pubchem_model(desc_subset)

        else:
            st.warning('No File Uploaded. Please upload a txt or csv file to predict pIC50 values.')

elif selected == 'HDAC prediction model using substructurefingerprints':
    st.title('Predict bioactivity of molecules against HDAC using substructurefingerprints')

    #substructure fingerprint calculation
    # def desc_calc():
    #     bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/SubstructureFingerprinter.xml -dir ./ -file descriptors_output.csv"
    #     process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #     output, error = process.communicate()
    #     os.remove('molecule.smi')

    # def filedownload(df):
    #     csv = df.to_csv(index = False)
    #     b64 = base64.b64encode(csv.encode()).decode()
    #     href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    #     return href
    
    #model building for substructure fingerprints

    def substructure_model(input_data):
        load_model = load_model = pickle.load(open('substructure.pkl', 'rb'))

        #using the model to make prediction
        prediction = load_model.predict(input_data)
        st.header('**Prediction Output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name ='Molecule_Name')
        df= pd.concat([molecule_name,prediction_output], axis=1)

        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    with st.sidebar.header('Upload your CSV File'):
        uploaded_file = st.sidebar.file_uploader("Upload the input file", type = ['txt','csv'])
    
    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep = ' ', header = None)
            load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False )

            st.header('***Original Input Data***')
            st.write(load_data)

            with st.spinner("Calculating Descriptors..."):
                substructure_calc()
            

            #reading and displaying the calculated descriptors
            st.header('**Calculated Molecular Descriptors:')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            st.header('**Subset of Descriptors chosen from Previously built model:**')
            Xlist = list(pd.read_csv('substructuretxt.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            #applying trained model to make prediction on query compounds
            substructure_model(desc_subset)

        else:
            st.warning('No File Uploaded. Please upload a txt or csv file to predict pIC50 values.')

if selected == 'HDAC prediction model using 1D and 2D molecular descriptors':

    st.title('Predict bioactivity of molecules against HDAC using 1D and 2D molecular descriptors')


    # #1D-2D Descriptor Calculator
    # def desc_calc():
    #     bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -2d -descriptortypes ./PaDEL-Descriptor/descriptors.xml -dir ./ -file descriptors_output.csv"
    #     process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    #     output, error = process.communicate()
    #     os.remove('molecule.smi')

    # def filedownload(df):
    #     csv = df.to_csv(index = False)
    #     b64 = base64.b64encode(csv.encode()).decode()
    #     href = f'<a href="data:file/csv;base64,{b64}" download="prediction.csv">Download Predictions</a>'
    #     return href
    
    #model selection and building for 1D 2D descriptors
    def descriptor_model(input_data):
        load_model = load_model = pickle.load(open('descriptor.pkl', 'rb'))

        #using the model to make prediction
        prediction = load_model.predict(input_data)
        st.header('**Prediction Output**')
        prediction_output = pd.Series(prediction, name='pIC50')
        molecule_name = pd.Series(load_data[1], name ='Molecule_Name')
        df= pd.concat([molecule_name,prediction_output], axis=1)

        st.write(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    #sidebar
    with st.sidebar.header('Upload the CSV Data Below:'):
        uploaded_file = st.sidebar.file_uploader("Upload the input file", type = ['txt','csv'])

    #Clicking the Predict Buttone and what to do when predict is clicked
    if st.sidebar.button('Predict'):
        if uploaded_file is not None:
            load_data = pd.read_table(uploaded_file, sep = ' ', header = None)
            load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False )

            st.header('***Original Input Data***')
            st.write(load_data)

            with st.spinner("Calculating Descriptors..."):
                descriptor_calc()
            

            #reading and displaying the calculated descriptors
            st.header('**Calculated Molecular Descriptors:')
            desc = pd.read_csv('descriptors_output.csv')
            st.write(desc)
            st.write(desc.shape)

            st.header('**Subset of Descriptors chosen from Previously built model:**')
            Xlist = list(pd.read_csv('descriptortxt.csv').columns)
            desc_subset = desc[Xlist]
            st.write(desc_subset)
            st.write(desc_subset.shape)

            #applying trained model to make prediction on query compounds
            descriptor_model(desc_subset)

        else:
            st.warning('No File Uploaded. Please upload a txt or csv file to predict pIC50 values.')
    




    

    









            



        

    


    
    

    










# #page title and other information being displayed on it
# st.markdown("""
# # Bioactivity Prediction App (HDAC

# This app allows will allow you to find the bioactivity of compounds in inhibiting 'Histone Deacetylase'. 'Histone Deacetylase is known drug target for causing Cancer

# **Credits**
# 1. The app was built by Faiq Alam (B.Tech, Computer Engineering, Aligarh Muslim University in collaboration with Amber Rizwan, Jamia Hamdard Univeristy
            
# 2. Descriptor was calculated using the Padel Descriptor Software ([Paper: (https://doi.org/10.1002/jcc.21707] and (http://www.yapcwsoft.com/dd/padeldescriptor/) )

# """)

# #creating the sidebar to upload the csv file
# with st.sidebar.header('Upload the CSV Data Below:'):
#     uploaded_file= st.sidebar.file_uploader("Upload the input file", type = ['txt'])


# #Clicking the Predict Buttone and what to do when predict is clicked
# if st.sidebar.button('Predict'):
#     load_data = pd.read_table(uploaded_file, sep = ' ', header = None)
#     load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False )

#     st.header('**Uploaded Data**')
#     st.write(load_data)

#     with st.spinner("Calculating Descriptors......."):
#         desc_calc()

#     #reading and displaying the calculated descriptors
#     st.header('**Calculated Molecular Descriptors:')
#     desc = pd.read_csv('descriptors_output.csv')
#     st.write(desc)
#     st.write(desc.shape)

#     st.header('**Subset of Descriptors chosen from Previously built model:**')
#     Xlist = list(pd.read_csv('pubchemtxt.csv').columns)
#     desc_subset = desc[Xlist]
#     st.write(desc_subset)
#     st.write(desc_subset.shape)

#     #applying trained model to make prediction on query compounds
#     build_model(desc_subset)

# else:
#     st.info('No data uploaded: Upload Input Data to Predict')







