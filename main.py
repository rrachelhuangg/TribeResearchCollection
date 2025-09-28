from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def cs():
    with open('static/cs_data.json') as file:
        cs_research_data = json.load(file)
    return render_template('homepage.html', research_data=cs_research_data, active_tab='cs')

@app.route('/math')
def math():
    with open('static/math_data.json') as file:
        math_research_data = json.load(file)
    return render_template('homepage.html', research_data=math_research_data, active_tab='math')

@app.route('/biology')
def biology():
    with open('static/bio_data.json') as file:
        bio_research_data = json.load(file)
    return render_template('homepage.html', research_data=bio_research_data, active_tab='biology')

@app.route('/data_science')
def data_science():
    with open('static/ds_data.json') as file:
        ds_research_data = json.load(file)
    return render_template('homepage.html', research_data=ds_research_data, active_tab='data_science')
