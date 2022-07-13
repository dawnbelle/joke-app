from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "What can you do if you cannot push your git changes? Use the --force, Luke",
    
    "Why was the function sad after a successful first call? It didn’t get a callback.",

    "What did the spider do on the computer? Made a website!",

    "What did the computer do at lunchtime? Had a byte!",
]

@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
