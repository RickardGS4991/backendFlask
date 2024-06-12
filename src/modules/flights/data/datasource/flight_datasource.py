from src.modules.flights.domain.datasource.flight_datasource import IFlightDatasource
from src.modules.flights.data.model.flight_model import Flight, Airport, Airline
from src.core.flask_sql.flask_sql import db
from sqlalchemy import func

class FlightDatasourceImpl(IFlightDatasource):

    def get_all_flights(self):
        return db.session.query(Flight).all()

    def airport_most_visited(self):
        result = db.session.query(
            Airport.airport_name,
            func.count(Flight.id_flight).label('num_movements')
        ).join(Flight, Airport.id_airport == Flight.id_airport).group_by(
            Airport.airport_name
        ).order_by(func.count(Flight.id_flight).desc()).first()
        return result

    def airline_with_more_flights(self):
        result = db.session.query(
            Airline.airline_name,
            func.count(Flight.id_flight).label('num_flights')
        ).join(Flight, Airline.id_airline == Flight.id_airline).group_by(
            Airline.airline_name
        ).order_by(func.count(Flight.id_flight).desc()).first()
        return result

    def day_with_more_visits(self):
        result = db.session.query(
            Flight.date_arrive,
            func.count(Flight.id_flight).label('num_flights')
        ).group_by(
            Flight.date_arrive
        ).order_by(func.count(Flight.id_flight).desc()).first()
        return result

    def airlines_two_flights(self):
        subquery = db.session.query(
            Flight.id_airline,
            Flight.date_arrive,
            func.count(Flight.id_flight).label('num_flights')
        ).group_by(
            Flight.id_airline,
            Flight.date_arrive
        ).subquery()

        result = db.session.query(
            Airline.airline_name
        ).join(
            subquery, Airline.id_airline == subquery.c.id_airline
        ).filter(
            subquery.c.num_flights > 2
        ).distinct().all()

        return result