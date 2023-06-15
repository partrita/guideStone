import streamlit as st
from amis import reconstruct_multi_models
import pandas as pd

st.title("Efficient evolution from general protein language models")

st.write("Scripts for running the analysis described in the paper **Efficient evolution of human antibodies from general protein language models**")


st.subheader("Input")

st.write('To calculate recommend point mutations usually takes 30 seconds, Please be patient')

seq = st.text_input(label = "Enter CDR sequence of antibody 👇",
                    placeholder = "Any white space is not allowed",
                    # key="sequence",
                    )

# parameters
sequence = seq
model_names = [ 'esm1b', 'esm1v1', 'esm1v2', 'esm1v3', 'esm1v4', 'esm1v5', ]
alpha = None

df = pd.DataFrame(columns = ['mutant'])  # Create empty DataFrame with column name
  
if st.button('Run'):
    st.divider()
    st.subheader("Output")
    
    mutations_models = reconstruct_multi_models(
        sequence, model_names, alpha = alpha, )
    
    for k, v in sorted(mutations_models.items(), key=lambda item: -item[1]):
        mut_str = f'{k[1]}{k[0] + 1}{k[2]}'
        df.loc[len(df)] = mut_str

    st.dataframe(df)

else:
    st.divider()
    st.subheader("Output")
    st.write('Please, click the run button')