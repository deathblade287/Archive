# !pip install sklearn
import os

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from utils import auto_dropper, label_encoder_auto


def train(data, y):
    data, columns_encoded = label_encoder_auto(data)

    sc = StandardScaler()
    data = sc.fit_transform(data)

    # Dividing Data Into Training & Test For Model
    seed = 9
    test_size = 0.3
    X_train, X_test, y_train, y_test = train_test_split(
        data, y, test_size=test_size, random_state=seed)

    clf = LinearRegression(normalize=True)
    type(X_test)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    # Accuracy Of Model

    # print(r2_score(y_test, y_pred))
    return data, r2_score(y_test, y_pred)


# df = pd.read_csv('orignal_data.csv')
# data, accuracy_score = train(df)
