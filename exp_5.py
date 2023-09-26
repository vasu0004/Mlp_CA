# -*- coding: utf-8 -*-
"""exp_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YJu5NEJvIpbA2tx-1AbEV9vwG5s_nl-_

Linear Regression
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data[:, 0].reshape(-1, 1) # Use sepal length as independent variable
y = iris.data[:, 1].reshape(-1, 1) # Use sepal width as dependent variable
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Predict sepal width using the linear regression model
y_pred = model.predict(X_test)
# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""Non-Linear Regression

"""

from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data # Input features
y = iris.target # Target variable
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a non-linear regression model (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100)
# Fit the model to the training data
model.fit(X_train, y_train)
# Predict the target variable
y_pred = model.predict(X_test)
# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)