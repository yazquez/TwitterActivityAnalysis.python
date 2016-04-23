from data_loader import TwitterDataLoader
from service import app
from flask import jsonify
from service.service import Service


@app.route('/coordinates', methods=['GET'])
def read_coordinates():
    coordinates = Service().get_coordinates()
    return jsonify(coordinates = coordinates)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


