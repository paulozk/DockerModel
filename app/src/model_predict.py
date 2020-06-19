from joblib import load
import pandas as pd
import sys

def model_predict(feature_values):

    model = load("models/logistic_regressor.pkl")
    data_new = pd.DataFrame([feature_values])

    prediction = model.predict(data_new)


    return prediction[0]
    #return "mooie bloem"


if(__name__ == "__main__"):
    args = sys.argv
    print(args)
    print(predict(args[1:]))


