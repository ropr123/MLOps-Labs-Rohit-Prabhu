import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

def load_data():
    wine = load_wine()
    X = wine.data
    y = wine.target
    print(wine.feature_names)
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
    return X_train, X_test, y_train, y_test