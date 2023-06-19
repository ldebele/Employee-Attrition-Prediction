import sys
import joblib
import pathlib
import pandas as pd


dir = pathlib.Path(__file__).absolute()
sys.path.append(dir.parent.parent)

MODEL_DIR = './models/2023-06-19T14:29:57_RF.joblib'



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


