from flask_injector import singleton
from ..controller.base.flights_controller import IFlightController
from ..controller.flights_controller import FlightControllerImpl
from src.modules.flights.domain.datasource.flight_datasource import IFlightDatasource
from src.modules.flights.data.datasource.flight_datasource import FlightDatasourceImpl
from src.modules.flights.domain.repository.flight_repository import IFlightRepository
from src.modules.flights.data.repository.flight_repository import FlightRepositoryImpl
from src.modules.flights.domain.use_case.all_flights import AllFlightsUseCase

def configure(binder):
    binder.bind(IFlightDatasource, to=FlightDatasourceImpl, scope=singleton)
    binder.bind(IFlightRepository, to=FlightRepositoryImpl, scope=singleton)
    binder.bind(IFlightController, to=FlightControllerImpl, scope=singleton)
    binder.bind(AllFlightsUseCase, to=AllFlightsUseCase, scope=singleton)