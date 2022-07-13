import flask
import data
from flask import Flask
import random

app = Flask(__name__)

@app.get("/")
def tell_a_joke():
    joke = random.choice(data.jokes)
    return flask.render_template('joke.html', joke_text=joke)
