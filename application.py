from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression 
import pickle
import numpy as np

application = Flask(__name__)


model = pickle.load(open('model.pkl','rb'))

@application.route('/')
def hello_world():
    return render_template('index.html')

@application.route('/predict',methods=['POST','GET'])
def predict():
    # print(list(request.form.values()))
    # input_features = [int(x) for x in request.form.values()]
    # input_array = [np.array(input_features)]    
    
    temp = int(request.form.get("temp"))
    humidity = int(request.form.get("humidity"))
    wind_speed = int(request.form.get("wind_speed"))
    input_features = [temp,humidity,wind_speed]
    input_array= np.array(input_features).reshape(1,-1)
    print(input_array)
    prediction = model.predict_proba(input_array)
    output = float('{0:.{1}f}'.format(prediction[0][1],2))
    print(output)

    if output >= 0.5:
        return render_template('index.html', pred=f'Forest is in Danger. \nProbability of forest fire is {output*100}%')
    else:
        return render_template('index.html', pred=f'Forest is safe. \nPorbability of forest fire is {output*100}%')

if __name__ == 'main':
    application.run(debug=False)