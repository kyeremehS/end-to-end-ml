import os
import numpy as np
from flask import Flask, render_template, request
from src.mlproject.pipeline.prediction import PredictionPipeline  # Assuming you have this file for your prediction logic

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')  # Assuming you have a script that trains your model
    return "Training completed successfully!"

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Read the inputs provided by the user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Prepare input data for prediction
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            # Instantiate the prediction pipeline and make a prediction
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=predict)  # Render results page with prediction

        except Exception as e:
            print('The Exception message is:', e)
            return 'Something went wrong! Please try again.'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
