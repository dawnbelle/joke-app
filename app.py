import flask
import data
from flask import Flask
import random

app = Flask(__name__)

@app.get("/")
def tell_a_joke():
    print("Beginning to tell a joke")
    joke = random.choice(data.jokes)
    print(f"The joke we are telling is {joke}")
    return flask.render_template('joke.html', joke_text=joke)
