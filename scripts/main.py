import sys
import pathlib 
import pandas as pd
import streamlit as st

from predict import prediction
from preprocess import wrangle
from utils import read_info_column


dir = pathlib.Path(__file__).absolute()
sys.path.append(dir.parent.parent)

TRAIN_DIR = './data/clean_HR_Analytics.csv'


def info_tab(tab):
    tab.write("#### Sample of the dataset")
    df_train = pd.read_csv(TRAIN_DIR)
    tab.dataframe(df_train.head(4))

    employee_info = read_info_column()

    tab.write("#### Columns Information")
    for col in df_train.columns:

        tab.markdown(f"  - {col}     -    {employee_info[col]}")



def prediction_tab(tab):

    tab.write("### Prediction")
    tab.write("choose employee attrition file in .csv or .xlsx format")

    ## files
    files = tab.file_uploader("Upload your file", type=['csv', 'xlsx'])

    if files:
        df = pd.read_csv(files)
        # Display the dataframe
        tab.dataframe(df)

    submit = tab.button("Predict")

    if submit:
        # preprocessing the data
        df = wrangle(df)
        # predict the data
        pred = prediction(df)

        tab.write("### Results")
        tab.dataframe(pred)

def header():
    st.title("Employee Attrition Prediction")
    st.write("The purpose of this web app is to provide accurate predictions of employee attrition\
         within an organization by analyzing multiple employee-related features.")

    tab1, tab2 = st.tabs(["## Prediction", "## Info"])

    return tab1, tab2



if __name__ == "__main__":
    tab1, tab2 = header()
    info_tab(tab2)
    prediction_tab(tab1)



