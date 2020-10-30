from flask import Blueprint, render_template, redirect, url_for, request, flash, session, Response
import json
import datetime
import numpy as np
import pickle
import os
import numpy 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', prediction=None)

@main.route('/predict', methods=['POST'])
def predict():
    prediction_values = []
    file_name = os.path.abspath('/Users/nelsongarcia/Desktop/Monash/homeworks /proyecto_terminado/terminado_increib/app/model/finalized_model.sav')
    model = pickle.load(open(file_name, 'rb'))

    house_type = request.form.get('house_type')
    bedrooms = request.form.get('bedrooms')
    state = request.form.get('state')
    print(house_type, bedrooms, state)

    __data_columns = ['bedrooms', "unit", "house", "townhouse", 'NSW','VIC', 'WA', 'SA', 'QLD', 'ACT']
    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = 0
    x[2] = 0
    x[3] = 0
    x[4] = 0
    x[5] = 0
    x[6] = 0
    x[7] = 0
    x[8] = 0
    x[9] = 0

    y = np.zeros(len(__data_columns))
    y[0] = 2
    y[1] = 1
    y[2] = 0
    y[3] = 0
    y[4] = 1
    y[5] = 0
    y[6] = 0
    y[7] = 0
    y[8] = 0
    y[9] = 0
    
    if house_type == 'unit':
        x[1] = 1

    elif house_type == 'house':
        x[2] = 1

    elif house_type == 'townhouse':
        x[3] = 1

    if state == 'NSW':
        x[4] = 1

    elif state == 'VIC':
        x[5] = 1

    elif state == 'WA':
        x[6] = 1

    elif state == 'SA':
        x[7] = 1

    elif state == 'QLD':
        x[8] = 1

    elif state == 'ACT':
        x[9] = 1

    print(x)
    print(y)
    prediction = round(model.predict([x])[0], 2)
    print(prediction)
    return render_template('index.html', prediction=prediction)
