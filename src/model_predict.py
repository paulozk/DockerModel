from joblib import load
import pandas as pd
import sys

def predict(feature_values):
    model = load("models/logistic_regressor")
    data_new = pd.DataFrame([feature_values])
    prediction = model.predict(data_new)

    return prediction[0]


if(__name__ == "__main__"):
    args = sys.argv
    print(args)
    print(predict(args[1:]))


