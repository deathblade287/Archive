import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from utils import auto_dropper, define_y_axis, label_encoder_auto, last

db_path = input('Database Path: ')
db_name = input('Database (.csv) Name: ')
y_columnName = input("Column Name Of Value 'Y' (Prediction Value): ")

# db_path = r"/home/deathblade287/Dropbox/ML/Projects/Insurance_Premium"
# db_name = "insurance-premium.csv"
# y_columnName = "charges"

# Loading Database
os.chdir(db_path)
data = pd.read_csv(db_name)

data, y = define_y_axis(data, y_columnName)

# Formating Final Answer
v = auto_dropper(data, y)
l = v.keys()
l = list(l)
max_acc = max(l)

print(
    f'Best Accuracy Is: {max_acc}, which is achieved by the combinations {v[max_acc]}')
