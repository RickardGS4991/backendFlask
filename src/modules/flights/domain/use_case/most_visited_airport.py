from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from flask_injector import inject
from flask import jsonify

class MostVisitedAirportUsecase:
    @inject
    def __init__(self, repository: IFlightRepository):
        self.repository = repository

    def execute(self):
        query = self.repository.airport_most_visited()
        return {
            'airport_name': query[0],
            'num_movements': query[1]
        }
