#%% Imports
import numpy as np
import sklearn as sk
import sklearn.model_selection
import sklearn.linear_model
import pickle

#%% Reading and Manipulating Data
testing = False

# Data stolen from here:https://medium.com/analytics-vidhya/building-rgb-color-classifier-part-1-af58e3bcfef7
data_in = np.loadtxt("color_dataset_violet.csv", delimiter=",", dtype=str) 

# Splitting off input data and labels
X = data_in[:,:3].astype(int)
y = data_in[:,3]

# Splitting the data so we can judge accuracy later
if testing:
    X_train, X_val, y_train, y_val = sklearn.model_selection.train_test_split(X, y, train_size=0.8)
    print(X_val.shape)
    
    # Standardizing the data
    mu = 127.5
    s = 74
    X_train = (X_train - mu)/s
    X_val = (X_val - mu)/s
else:
    X_train = X
    y_train = y
    
    # Standardizing the data
    mu = 127.5
    s = 74
    X_train = (X_train - mu)/s

#%% Training Model
model = sk.linear_model.LogisticRegression()
model.fit(X_train, y_train)

#%% Evaluating Accuracy
if testing:
    y_pred = model.predict(X_val)
    accuracy = np.mean(y_pred == y_val)
    print(f'accuracy is : {accuracy}')

#%% Exporting Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)