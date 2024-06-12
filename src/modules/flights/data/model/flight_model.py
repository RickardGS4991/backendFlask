from src.core.flask_sql.flask_sql import db

class Airline(db.Model):
    __tablename__ = 'airlines'
    id_airline = db.Column(db.Integer, primary_key=True)
    airline_name = db.Column(db.String(255), nullable=False)

class Airport(db.Model):
    __tablename__ = 'airports'
    id_airport = db.Column(db.Integer, primary_key=True)
    airport_name = db.Column(db.String(255), nullable=False)

class Movement(db.Model):
    __tablename__ = 'movements'
    id_movement = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)

class Flight(db.Model):
    __tablename__ = 'country_flights'
    id_flight = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_airline = db.Column(db.Integer, db.ForeignKey('airlines.id_airline'), nullable=False)
    id_airport = db.Column(db.Integer, db.ForeignKey('airports.id_airport'), nullable=False)
    id_movement = db.Column(db.Integer, db.ForeignKey('movements.id_movement'), nullable=False)
    date_arrive = db.Column(db.Date, nullable=False)

    airline = db.relationship('Airline', backref=db.backref('country_flights', lazy=True))
    airport = db.relationship('Airport', backref=db.backref('country_flights', lazy=True))
    movement = db.relationship('Movement', backref=db.backref('country_flights', lazy=True))