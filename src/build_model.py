import pandas as pd
from sklearn.linear_model import LogisticRegression
from joblib import dump


data = pd.read_csv("data/iris.data")
model = LogisticRegression()

train_x =  data.iloc[:, :-1]
train_y = data.iloc[:, -1]

model.fit(train_x, train_y)

dump(model, "models/logistic_regressor")
