from flask import jsonify
from flask_injector import inject
from src.modules.flights.domain.use_case.all_flights import AllFlightsUseCase
from src.modules.flights.domain.use_case.most_visited_airport import MostVisitedAirportUsecase
from src.modules.flights.domain.use_case.airline_with_more import AirlineWithMoreUsecase
from src.modules.flights.domain.use_case.day_more_visited import DayWithMoreVisits
from src.modules.flights.domain.use_case.airline_with_two import AirlineWithTwoUsecase
from .base.flights_controller import IFlightController

class FlightControllerImpl(IFlightController):
    @inject
    def __init__(
            self,
            get_flight_all: AllFlightsUseCase,
            most_visited_usecase: MostVisitedAirportUsecase,
            airline_with_more_usecase: AirlineWithMoreUsecase,
            day_more_usecase: DayWithMoreVisits,
            get_airline_with_more_two_usecase: AirlineWithTwoUsecase
    ):
        self.get_flight_all = get_flight_all
        self.most_visited_usecase = most_visited_usecase
        self.airline_with_more_usecase = airline_with_more_usecase
        self.day_more_usecase = day_more_usecase
        self.get_airline_with_more_two_usecase = get_airline_with_more_two_usecase

    def get_flights(self):
        flights = self.get_flight_all.execute()
        return jsonify(flights)

    def visited_most_airport(self):
        result = self.most_visited_usecase.execute()
        return jsonify(result)

    def airline_most_visited(self):
        return self.airline_with_more_usecase.execute()

    def more_visited_day(self):
        return self.day_more_usecase.execute()

    def get_airline_with_more_two(self):
        return self.get_airline_with_more_two_usecase.execute()
