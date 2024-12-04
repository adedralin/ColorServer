from flask import Flask, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Standardizing constants
MU = 127.5
S = 74

def hex_to_rgb(hex_color):
    """Convert hex color to RGB array."""
    return np.array([int(hex_color[i:i+2], 16) for i in (0, 2, 4)])

@app.route('/predict/<hex_color>')
def predict_color(hex_color):
    """Predict color name from hex code."""
    try:
        # Convert hex to RGB
        rgb = hex_to_rgb(hex_color)
        
        # Standardize
        query = (rgb - MU) / S
        query = query.reshape(1, -1)
        
        # Predict
        y_pred = model.predict(query)
        
        # Return the prediction as plain text
        return y_pred[0], 200
    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

