from repository.repository import Repository


class Service:
    def get_coordinates(self, survey_id):
        return Repository().get_coordinates(survey_id)
