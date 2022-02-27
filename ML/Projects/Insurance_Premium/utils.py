import os
# import sys
from itertools import chain, combinations

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder, StandardScaler


def define_y_axis(data, column_y):
    y = data[column_y]
    data_new = data.drop(column_y, axis=1)
    return data_new, y

# Step 3: Drop Useless Columns + Features (Make Program Try All Combinations Of Dropping, & Then Give Hieghest Acuuracy One)


def last(y):
    data, columns_encoded = label_encoder_auto("insurance-premium.csv",
                                               path=r"/home/deathblade287/Dropbox/ML/Projects/Insurance_Premium")
    sc = StandardScaler()
    data = sc.fit_transform(data)

    seed = 9
    test_size = 0.3
    X_train, X_test, y_train, y_test = train_test_split(
        data, y, test_size=test_size, random_state=seed)

    clf = LinearRegression(normalize=True)
    type(X_test)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # Accuracy Of Model
    accuracy_final_score = r2_score(y_test, y_pred)
    print(accuracy_final_score)
    return accuracy_final_score


def auto_dropper(data, y_column_value, manual=True):
    data = data  # DataFrame
    data_unchanged_values = data
    y = y_column_value  # Y (pred) Value For DF
    column_list = list(data.columns)  # Columns In DataFrame

    # Iterate Through Every Possobility Of Columns (To Be Dropped)
    all_column = []

    def all_subsets(ss):
        return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

    for subset in all_subsets(column_list):
        print(subset)
        all_column.append(subset)

    print(column_list)
    print(type(column_list))
    print(all_column)
    print(type(all_column))
    print('\n\n')

    # Convert Iterated Tuples To List
    for i in range(len(all_column)):
        all_column[i] = list(all_column[i])
    all_column.pop(0)
    print(all_column)

    all_accuracyData_columns = {}

    for i in range(len(all_column)):
        for j in range(len(all_column[i])):
            data = data.drop(all_column[i][j], axis=1)
        accuracyScoreNow = last(y)  # Rest Of Process
        data = data_unchanged_values
        all_accuracyData_columns[accuracyScoreNow] = all_column[i]
    return all_accuracyData_columns

    # Try, Drop & Record Accuracy Of Each List(Combination Of Columns) Stored

    # print(data)
    # print(type(data))


def label_encoder_auto(fileName, path=os.getcwd()):
    # Defining Database
    os.chdir(path)
    data = pd.read_csv(fileName)
    columns_encoded = []
    # Lable Encoding (Starting)...
    le = LabelEncoder()
    for i in range(len(data.columns)):
        column_now = data.columns[i]
        all_rows = data[column_now][0:]
        # Removing The Index + pandas.core.series.Series => List
        all_rows = all_rows.to_list()
        for i in range(len(all_rows)):
            if type(all_rows[i]) == int:
                status_encoding = False
            elif type(all_rows[i]) != int:
                status_encoding = True
                break
        if status_encoding == True:
            data[column_now] = le.fit_transform(data[column_now])
            columns_encoded.append(column_now)
    return data, columns_encoded
    # l[column_now] = all_rows
