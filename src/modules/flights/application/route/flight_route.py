from flask import Blueprint
from ..controller.base.flights_controller import IFlightController
from flask_injector import inject

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/', methods=['GET'])
@inject
def get_all_flight_route(controller: IFlightController):
    print('finish route')
    return controller.get_flights()

@flight_bp.route('/airport-most-movements', methods=['GET'])
@inject
def get_airport_with_most_movements_route(controller: IFlightController):
    return controller.visited_most_airport()

@flight_bp.route('/airline-more', methods=['GET'])
@inject
def airline_with_more_visits(controller: IFlightController):
    return controller.airline_most_visited()

@flight_bp.route('/day-more', methods=['GET'])
@inject
def day_with_more_visits(controller: IFlightController):
    return controller.more_visited_day()

@flight_bp.route('/airline-two', methods=['GET'])
@inject
def get_airline_with_more_than_two_flights(controller: IFlightController):
    return controller.get_airline_with_more_two()