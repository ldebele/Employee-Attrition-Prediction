import sys
import pathlib
import pandas as pd


dir = pathlib.Path(__file__).absolute()
sys.path.append(dir.parent.parent)

MODEL_DIR = './models/2023-06-23T13:43:35_LR.pkl'


def prediction(data):
    """
        params:
            data: pd.dataframe  -> input dataset
        
        return:
            df_pred: pd.dataframe  -> predicted result
    """
    
    # Load the model
    # model = joblib.load(MODEL_DIR)
    model = pd.read_pickle(MODEL_DIR)
    # predict the data
    pred = model.predict(data)

    df_pred = pd.DataFrame(pred).rename({0: "Attrition"}, axis=1)

    dict = {
        "Yes": "Leave",
        "No": "Stay"
    }

    df_pred["Attrition"].replace(dict, inplace=True)

    # return the predicted
    return df_pred


