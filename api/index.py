from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# app = Flask(__name__, template_folder="../templates", static_folder="../static")

# # Load the model and label encoder
# model_path = os.path.join(os.path.dirname(__file__), "../savemodel.sav")
# encoder_path = os.path.join(os.path.dirname(__file__), "../label_encoder.pkl")

# with open(model_path, 'rb') as model_file:
#     model = pickle.load(model_file)
# with open(encoder_path, 'rb') as encoder_file:
#     label_encoder = pickle.load(encoder_file)

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'savemodel.sav'), 'rb') as model_file:
    model = pickle.load(model_file)

with open(os.path.join(base_dir, 'label_encoder.pkl'), 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)


@app.route('/')
def home():
    result = ''
    return render_template('index.html', result=result)

@app.route('/predict', methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Predict using the model
    encoded_result = model.predict(features)[0]

    # Decode the prediction
    result = label_encoder.inverse_transform([encoded_result])[0]

    return render_template('index.html', result=result, 
                           sepal_length=sepal_length,
                           sepal_width=sepal_width,
                           petal_length=petal_length, 
                           petal_width=petal_width)

if __name__ == '__main__':
    app.run(debug=True,port=5001)