import pandas as pd
from category_encoders import OneHotEncoder


def wrangle(data):


    # remove low-cardinality categorical features
    low_card = (data.nunique()) == 1
    data.drop(columns=low_card[low_card].index.to_list(), inplace=True)

    if "Attrition" in data.columns:
        data.drop(columns="Attrition", inplace=True)

    return data


