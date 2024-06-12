from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from flask_injector import inject
from flask import jsonify

class DayWithMoreVisits:
    @inject
    def __init__(self, repository: IFlightRepository):
        self.repostory = repository

    def execute(self):
        query = self.repostory.day_more_visited()
        return jsonify({"date_arrive":query[0].strftime('%Y-%m-%d')})