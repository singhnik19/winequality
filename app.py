import pickle
import pandas as pd
import numpy as np
import flask
from flask import request
with open(f'model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=["GET", "POST"])
def index():
    if flask.request.method == 'GET':
        return(flask.render_template('form.html'))

    if flask.request.method == 'POST':
        fixedAcidity= float(flask.request.form['fixedAcidity'])
        volatileAcidity=float(request.form['volatileAcidity'])
        citricAcid = float(flask.request.form['citricAcid'])
        residualSugar= float(request.form['residualSugar'])
        chlorides= float(flask.request.form['chlorides'])
        freeSulphurDioxide = float(request.form['freeSulphurDioxide'])
        totalSulphurDioxide = float(flask.request.form['totalSulphurDioxide'])
        density = float(request.form['density'])
        ph = float(flask.request.form['ph'])
        sulphates = float(request.form['sulphates'])
        alcohol = float(request.form['alcohol'])
        input_array=[fixedAcidity,volatileAcidity,citricAcid,residualSugar,chlorides,freeSulphurDioxide,totalSulphurDioxide,density,ph,sulphates,alcohol]
        quality=model.predict([input_array])
        quality_rendered=quality[0]
        print(quality)
        return flask.render_template('form.html',original_input={'Fixed Acidity':fixedAcidity,'Volatile Acidity':volatileAcidity,'Citric Acid':citricAcid,
                                                                 'Residual Sugar':residualSugar,'Chlorides':chlorides,'Free Sulphur Dioxide':freeSulphurDioxide,
                                                                 'Total Sulphur Dioxide':totalSulphurDioxide,'Density':density,'pH':ph,'Sulphates':sulphates,
                                                                 'Alcohol':alcohol},quality=quality_rendered,)
if __name__ == '__main__':
    app.run(debug="True")
