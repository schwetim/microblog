# importing Flask object from Flask package
from flask import Flask

# create applocation named app with Flask, parameter __name__ contains the name of the current python module
app = Flask(__name__)

# Sending and receiving messages from/to user
# @app.route is a decorator, that transforms a regular python function to a flask function -> transforms the answer (Rückantwort) to a HTTP-answer


@app.route('/')
def hello():
    return 'Hello World!'
