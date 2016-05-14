from repository.repository import Repository
import json

class Service:
    def get_survey_config(self, survey_id):
        with open('config/surveys.json') as data_file:
            surveys = json.load(data_file)
        return surveys[survey_id]

    def get_coordinates(self, survey_id):
        return Repository().get_coordinates(survey_id)

    def get_totals_by_topic(self, survey_id):
        return Repository().get_totals_by_topic(survey_id)

