from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_placement():
    try:
        # Get input values from form
        cgpa = float(request.form.get('cgpa'))
        iq = int(request.form.get('iq'))
        profile_score = int(request.form.get('profile_score'))

        # Make prediction
        result = model.predict(np.array([[cgpa, iq, profile_score]]))

        # Check result and return message
        if result[0] == 1:
            message = 'Student get Placed in the Campus Placement'
        else:
            message = 'Student does not get Placed in the Campus Placement'

        return render_template('index.html', result=message)

    except Exception as e:
        return str(e)  # Return error message for debugging

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
