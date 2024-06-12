from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from flask_injector import inject
from flask import jsonify

class AirlineWithTwoUsecase:
    @inject
    def __init__(self, repository: IFlightRepository):
        self.repository = repository

    def execute(self):
        query = self.repository.airlines_with_two()
        result = [airline.airline_name for airline in query]
        return jsonify(result)