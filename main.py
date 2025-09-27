from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('static/cs_data.json') as file:
        cs_research_data = json.load(file)
    return render_template('homepage.html', cs_research_data=cs_research_data)

@app.route('/about')
def about():
    return 'About'