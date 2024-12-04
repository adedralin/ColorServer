#%% Import
import numpy as np
import sklearn as sk
import sklearn.linear_model
import pickle

#%% Input
def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return np.array(rgb)

hex_code = 'aa00ff' # This will be the input you have to get from the url
query = hex_to_rgb(hex_code)

# Standardizing
mu = 127.5
s = 74
query = (query - mu)/s
query = query.reshape(1, -1)

#%% Predict
# Load the model
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Make Prediction
y_pred = loaded_model.predict(query)
print(y_pred[0])