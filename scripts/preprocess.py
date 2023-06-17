import pandas as pd
from category_encoders import OneHotEncoder


def wrangle(data):
    """
        params:
            data: DataFrame   -> raw datasets

        return:
            data: DataFrame  -> preproccessed datasets
    """

    # remove low-cardinality categorical features
    low_card = (data.nunique()) == 1
    data.drop(columns=low_card[low_card].index.to_list(), inplace=True)

    # Drop target column if it's in the dataset.
    if "Attrition" in data.columns:
        data.drop(columns="Attrition", inplace=True)

    return data


