import flask
from data import jokes
from flask import Flask
import random

app = Flask(__name__)

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return flask.render_template('joke.html', joke_text=joke)
