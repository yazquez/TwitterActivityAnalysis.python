"""Create and configure the Flask server"""
from flask import Flask

app = Flask(__name__)

# Routes
from service import controler
