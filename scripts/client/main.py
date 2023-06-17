import streamlit as st
import pandas as pd


TRAIN_DIR = './data/clean_HR_Analytics.csv'


def info_tab(tab):
    df_train = pd.read_csv(TRAIN_DIR)
    tab.dataframe(df_train.head(4))

    tab.write("#### Columns")
    for col in df_train.columns:
        # tab.write(col)
        tab.markdown(f"- {col}")



def prediction_tab(tab):

    tab.write("### Prediction")

    tab.write("choose employee attrition file in .csv or .xlx format")

    ## files
    files = tab.file_uploader("Upload your file", type=['csv'])

    if files:
        df = pd.read_csv(files)
        # Display the dataframe
        tab.dataframe(df)

    submit = tab.button("Prediction")

    if submit:
        pass



    tab.write("### Results")




st.title("Employee Attrition Prediction")

tab1, tab2 = st.tabs(["Prediction", "Info"])

info_tab(tab2)
prediction_tab(tab1)



