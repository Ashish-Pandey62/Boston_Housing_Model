from flask import Flask, render_template, request
import pickle

with open('house_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input parameters from the form
    CRIM = float(request.form['CRIM'])
    ZN = float(request.form['ZN'])
    INDUS = float(request.form['INDUS'])
    NOX = float(request.form['NOX'])
    RM = float(request.form['RM'])
    AGE = float(request.form['AGE'])
    DIS = float(request.form['DIS'])
    RAD = float(request.form['RAD'])
    TAX = float(request.form['TAX'])
    PTRATIO  = float(request.form['PTRATIO'])
    PTRATIO  = float(request.form['PTRATIO'])
    B  = float(request.form['B'])
    LSTAT  = float(request.form['LSTAT'])
    
    
    
    
    

    # Use the model to make a prediction
    prediction = model.predict([[CRIM,ZN,INDUS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])

    # Return the predicted price to the user
    return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)