import os
import sys
import pathlib 
import pandas as pd
import streamlit as st

from predict import prediction
from preprocess import wrangle



dir = pathlib.Path(__file__).abspath()

sys.path.append(dir.parent.parent)


TRAIN_DIR = './data/clean_HR_Analytics.csv'
# TRAIN_DIR = Path("./data") / 'clean_HR_Analytics.csv'


def info_tab(tab):
    # tab.write("#### Sample of the dataset")
    # df_train = pd.read_csv(TRAIN_DIR)
    # tab.dataframe(df_train.head(4))

    # tab.write("#### Columns")
    # for col in df_train.columns:
    #     # tab.write(col)
    #     tab.markdown(f"  - {col}")
    pass


def prediction_tab(tab):

    tab.write("### Prediction")
    tab.write("choose employee attrition file in .csv or .xlx format")

    ## files
    files = tab.file_uploader("Upload your file", type=['csv'])

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
    tab1, tab2 = st.tabs(["## Prediction", "## Info"])

    return tab1, tab2



if __name__ == "__main__":
    tab1, tab2 = header()
    info_tab(tab2)
    prediction_tab(tab1)



