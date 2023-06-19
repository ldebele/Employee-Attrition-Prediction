import joblib
from glob import glob
import pandas as pd

from pathlib import Path

MODEL_DIR = Path("./models") / "2023-06-14T12:21:27_RF.pkl"


# MODEL_DIR = glob('./models/*_RF.pkl')


def prediction(data):
    """
        params:
            data: dataframe  -> input dataset
        
        return:
            df_pred: dataframe  -> predicted result
    """
    
    # Load the model
    model = joblib.load(MODEL_DIR)
    # predict the data
    pred = model.predict(data)

    df_pred = pd.DataFrame(pred).rename({0: "Attrition"}, axis=1)

    # return the predicted
    return df_pred


