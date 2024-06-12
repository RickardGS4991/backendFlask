from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from flask_injector import inject
from flask import jsonify

class AirlineWithMoreUsecase:
    @inject
    def __init__(self, repository: IFlightRepository):
        self.repository = repository

    def execute(self):
        result = self.repository.airline_more_flight()
        return jsonify({"airline_name": result[0]})