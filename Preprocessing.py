import pandas as pd
import matplotlib.pyplot as plt
import statistics
from sklearn.model_selection import train_test_split
import GUI_handling as mainVariables
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Main Variables Getting from GUI
learning_rate = mainVariables.eta
epochs = mainVariables.m
with_bias = mainVariables.bias
mse = mainVariables.mse

# columns that will be removed from x_train , x_test
Li_col = ["body_mass_g", "gender", "flipper_length_mm", "bill_depth_mm", "bill_length_mm"]
Li_col.remove(mainVariables.firstFeature)
Li_col.remove(mainVariables.secondFeature)

# read data
dataset = pd.read_csv("data_set/penguins.csv")

# split data into train_test depending on the data needed only from 2 classes
# [60 [30 class 1 , 30 class 2] train , 40 [20 class 1 , 20 class 2]] test
x_class1 = dataset[dataset['species'] == mainVariables.class1].drop(columns="species")
x_class2 = dataset[dataset['species'] == mainVariables.class2].drop(columns="species")
y_class1 = dataset[dataset['species'] == mainVariables.class1].drop(columns=["body_mass_g","gender","flipper_length_mm","bill_depth_mm","bill_length_mm"])
y_class2 = dataset[dataset['species'] == mainVariables.class2].drop(columns=["body_mass_g","gender","flipper_length_mm","bill_depth_mm","bill_length_mm"])


x1_train,x1_test,y1_train,y1_test = train_test_split(x_class1, y_class1, test_size=0.382, random_state=20)
x2_train,x2_test,y2_train,y2_test = train_test_split(x_class2, y_class2, test_size=0.382, random_state=20)

# Final x_train , x_Test , y_train , y_test for our model
x_train = pd.concat([x1_train,x2_train])
x_test = pd.concat([x1_test,x2_test])
y_train = pd.concat([y1_train,y2_train])
y_test = pd.concat([y1_test,y2_test])

x_train.fillna(statistics.mode(x_train["gender"]), inplace=True)
x_test.fillna(statistics.mode(x_test["gender"]), inplace=True)

# encoder for gender values
enc = LabelEncoder()
x_train["gender"] = enc.fit_transform(np.array(x_train["gender"]).reshape(-1, 1))
x_test["gender"] = enc.fit_transform(np.array(x_test["gender"]).reshape(-1, 1))


# new encoder for y values
enc = LabelEncoder()
y_train = enc.fit_transform(np.array(y_train).reshape(-1, 1))
y_test = enc.fit_transform(np.array(y_test).reshape(-1, 1))


# concat data again and shuffle it
x_train["species"] = y_train
x_test["species"] = y_test

x_train = x_train.sample(frac=1)
x_test = x_test.sample(frac=1)
y_train = x_train["species"]
y_test = x_test["species"]

# normalize data
for i in ['bill_length_mm', 'body_mass_g', 'bill_depth_mm', 'flipper_length_mm']:
    scaler = MinMaxScaler()
    x_train[[i]] = scaler.fit_transform(x_train[[i]])
    x_test[[i]] = scaler.fit_transform(x_test[[i]])

# drop all columns except the features that needed
Li_col.append("species")
x_train.drop(columns=Li_col, inplace=True)
x_test.drop(columns=Li_col, inplace=True)


# Functions [Draw all corr between features]
def DrawAllCombinations():
    global enc
    X = dataset.drop(columns="species", inplace=False)
    X["gender"].fillna(statistics.mode(X["gender"]), inplace=True)
    # encoder for gender values
    enc = LabelEncoder()
    dataset["gender"] = enc.fit_transform(np.array(dataset["gender"]).reshape(-1, 1))
    for i in X.columns:
        for j in X.columns:
            if i == j or j < i:
                continue
            else:
                plt.rcParams.update({'figure.figsize': (10, 8), 'figure.dpi': 100})
                plt.scatter(X[i][0:50], X[j][0:50], color='red', label=f'Adelie')
                plt.scatter(X[i][50:100], X[j][50:100], color='blue', label=f'Gentoo')
                plt.scatter(X[i][100:150], X[j][100:150], color='green', label=f'Chinstrap')
                plt.title('(' + i + ' , ' + j + ')')
                plt.legend()
                plt.show()

