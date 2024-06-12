from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from src.modules.flights.domain.datasource.flight_datasource import IFlightDatasource
from flask_injector import inject

class FlightRepositoryImpl(IFlightRepository):
    @inject
    def __init__(self, datasource: IFlightDatasource):
        self.datasource = datasource

    def get_all_flights(self):
        print('finish repository')
        data = self.datasource.get_all_flights()
        return data

    def airport_most_visited(self):
        return self.datasource.airport_most_visited()

    def airline_more_flight(self):
        return self.datasource.airline_with_more_flights()

    def day_more_visited(self):
        return self.datasource.day_with_more_visits()

    def airlines_with_two(self):
        return self.datasource.airline_with_more_flights()
