# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 17:55:15 2018

@author: Rohan
"""

# Implementing a neural network for the ferrtility dataset.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

fert = pd.read_csv("fertilecsv.csv")

result = pd.get_dummies(fert['Target'],drop_first = True)

fert = pd.concat([fert.drop('Target',axis = 1) , result ] , axis = 1)


from sklearn.model_selection import train_test_split

X = fert.drop('O',axis = 1)
y = fert['O']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


from keras.models import Sequential
from keras.layers import Dense

clf = Sequential() # Creating the model

clf.add(Dense(units=5, activation='relu',kernel_initializer='uniform', input_dim=9))
clf.add(Dense(units=5, activation='relu',kernel_initializer='uniform'))
clf.add(Dense(units=1, activation='sigmoid',kernel_initializer='uniform'))

clf.compile(optimizer='adam', loss= 'binary_crossentropy', metrics=['accuracy'])


clf.fit(X_train, y_train, batch_size=10, epochs=300)

y_pred = clf.predict(X_test)

y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
