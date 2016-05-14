from service import app
from flask import jsonify
from service.service import Service


@app.route('/coordinates/<string:survey_id>', methods=['GET'])
def read_coordinates(survey_id):
    coordinates = Service().get_coordinates(survey_id)
    return jsonify(coordinates=coordinates)

@app.route('/survey/<string:survey_id>', methods=['GET'])
def read_survey_config(survey_id):
    survey = Service().get_survey_config(survey_id)
    return jsonify(survey=survey)


@app.route('/grouped/<string:survey_id>', methods=['GET'])
def read_totals_by_topic(survey_id):
    survey = Service().get_totals_by_topic(survey_id)
    return jsonify(survey=survey)



@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
