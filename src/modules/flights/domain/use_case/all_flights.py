from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from flask_injector import inject

class AllFlightsUseCase:
    @inject
    def __init__(self, repository: IFlightRepository):
        self.repository = repository

    def execute(self):
        data = self.repository.get_all_flights()
        flights = []
        for flight in data:
            flights.append({
                'id_flight': flight.id_flight,
                'id_airline': flight.id_airline,
                'id_airport': flight.id_airport,
                'id_movement': flight.id_movement,
                'date_arrive': flight.date_arrive.strftime('%Y-%m-%d')
            })
        return flights