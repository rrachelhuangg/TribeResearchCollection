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
    return render_template('homepage.html', research_data={}, active_tab='math')

@app.route('/biology')
def biology():
    return render_template('homepage.html', research_data={}, active_tab='biology')

@app.route('/english')
def english():
    return render_template('homepage.html', research_data={}, active_tab='english')
