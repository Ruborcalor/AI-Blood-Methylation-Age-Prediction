from __future__ import absolute_import, division, print_function, unicode_literals
from flask import render_template, request
from app import app

import json
import plotly
#import plotly.plotly as py
#import chart_studio.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

#import tensorflow as tf

# import keras

#from keras.models import load_model

@app.route("/")
def index():

    # cgs = ["cg02228185", "cg01511567", "cg02085507", "cg08370996", "cg04084157", "cg19761273", "cg17274064", "cg20692569", "cg24450312", "cg04528819", "cg06493994", "cg22736354", "cg01820374", "cg07158339", "cg27544190", "cg02479575", "cg03286783", "cg09809672", "cg05442902"]

    cgs = ["cg24450312", "cg02085507", "cg02479575", "cg09809672", "cg06493994", "cg22736354", "cg04084157", "cg04528819", "cg20692569", "cg07158339", "cg01511567", "cg01820374", "cg03286783", "cg08370996", "cg02228185", "cg19761273", "cg17274064", "cg27544190", "cg05442902"]
    # cgs = ['cg05442902', 'cg20692569', 'cg02228185', 'cg02085507', 'cg27544190', 'cg03286783', 'cg01820374', 'cg07158339', 'cg24450312', 'cg17274064', 'cg04084157', 'cg19761273', 'cg22736354', 'cg06493994', 'cg04528819', 'cg02479575', 'cg09809672', 'cg08370996', 'cg01511567']
    # cgs = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
    # cgs += ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
    # cgs = list(set(cgs))
    # spots16 = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
    # spots6 = ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
    # spots19 = list(set((spots6 + spots16)))
    # print("Spots 19:")
    # print(spots19)


    np_valid_pred = np.load('./app/y_valid_pred.npy')
    np_valid_real = np.load('./app/y_valid_real.npy')

    # Create a trace
    trace = go.Scatter(
        x = np_valid_real,
        y = np_valid_pred,
        mode='markers',
        marker=dict(size=[16] * len(np_valid_real), color=[2] * len(np_valid_real))
    )

    data = [trace]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("/startbootstrap-bare-gh-pages/index.html", cgs = cgs, plot=graphJSON)

@app.route("/about")
def about():
    return """
        <h1 style='color: red;'>I'm a red H1 heading!</h1>
        <p>This is a lovely little paragraph</p>
        <code>Flask is <em>awesome</em></code>
        """


@app.route("/click_point", methods=['POST'])
def click_point():
    if request.method == 'POST':

        # cgs = ["cg02228185", "cg01511567", "cg02085507", "cg08370996", "cg04084157", "cg19761273", "cg17274064", "cg20692569", "cg24450312", "cg04528819", "cg06493994", "cg22736354", "cg01820374", "cg07158339", "cg27544190", "cg02479575", "cg03286783", "cg09809672", "cg05442902"]
        # cgs = ['cg05442902', 'cg20692569', 'cg02228185', 'cg02085507', 'cg27544190', 'cg03286783', 'cg01820374', 'cg07158339', 'cg24450312', 'cg17274064', 'cg04084157', 'cg19761273', 'cg22736354', 'cg06493994', 'cg04528819', 'cg02479575', 'cg09809672', 'cg08370996', 'cg01511567']
        cgs = ["cg24450312", "cg02085507", "cg02479575", "cg09809672", "cg06493994", "cg22736354", "cg04084157", "cg04528819", "cg20692569", "cg07158339", "cg01511567", "cg01820374", "cg03286783", "cg08370996", "cg02228185", "cg19761273", "cg17274064", "cg27544190", "cg05442902"]





        # spots16 = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
        # spots6 = ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
        # spots19 = list(set((spots6 + spots16)))
        # print("Spots 19:")
        # print(spots19)
        # cgs = ["cg19761273", "cg27544190", "cg03286783", "cg01511567", "cg07158339", "cg05442902", "cg24450312", "cg17274064", "cg02085507", "cg20692569", "cg04528819", "cg08370996", "cg04084157", "cg22736354", "cg06493994", "cg02479575"]
        # cgs += ["cg09809672", "cg22736354", "cg02228185", "cg01820374", "cg06493994", "cg19761273"]
        # cgs = list(set(cgs))
        print(cgs)

        np_x_test = np.load('./app/X_test.npy')
        print(np_x_test[request.json['pointNumber']])
        return json.dumps({
            'x': request.json["x"], 
            'y': request.json["y"], 
            'pointNumber': request.json["pointNumber"], 
            'methyl': np_x_test[request.json['pointNumber']].tolist(),
            'cgs': cgs,
            'success':True}), 200, {'ContentType':'application/json'} 

        #return "go"

# @app.route("/model_predict", methods=['POST'])
# def model_predict():
#     if request.method == 'POST':
# 
#         #model = load_model('/home/gautierk/McGill/202mais/app/app/model.h5')
#         # Create a basic model instance
#         #model = create_model()
# 
#         # Display the model's architecture
#         #model.load_weights('/home/gautierk/McGill/202mais/app/app/model_weights.index.npy')
#         x_test = np.array(request.json["knobs"])
#         y_pred = model.predict(x_test)
#         return json.dumps({
#             'x_test': request.json("knobs"),
#             #'pred': y_pred, 
#             'cgs': cgs,
#             'success':True}), 200, {'ContentType':'application/json'} 


# def create_model():
#     model = tf.keras.models.Sequential([
#         tf.keras.layers.Dense(512, activation='relu', input_shape=(19,)),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.Dense(256, activation='relu'),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.Dense(128, activation='relu'),
#         tf.keras.layers.Dropout(0.2),
#         tf.keras.layers.Dense(1)
#     ])
# 
#     model.compile(optimizer='adam',

    # cgs = ['cg05442902', 'cg20692569', 'cg02228185', 'cg02085507', 'cg27544190', 'cg03286783', 'cg01820374', 'cg07158339', 'cg24450312', 'cg17274064', 'cg04084157', 'cg19761273', 'cg22736354', 'cg06493994', 'cg04528819', 'cg02479575', 'cg09809672', 'cg08370996', 'cg01511567']
    cgs = ["cg24450312", "cg02085507", "cg02479575", "cg09809672", "cg06493994", "cg22736354", "cg04084157", "cg04528819", "cg20692569", "cg07158339", "cg01511567", "cg01820374", "cg03286783", "cg08370996", "cg02228185", "cg19761273", "cg17274064", "cg27544190", "cg05442902"]
#                 loss='sparse_categorical_crossentropy',
#                 metrics=['accuracy'])
# 
#     return model
