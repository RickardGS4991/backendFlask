
from src.modules.question.aplication.di.question_container import configure as configure_questions
from src.modules.flights.application.di.flight_container import configure as configure_flight
from src.modules.question.aplication.route.question_route import bp as question_bp
from src.modules.flights.application.route.flight_route import flight_bp
from src.core.flask_sql.flask_sql import db
from flask import Flask, jsonify
from flask_injector import FlaskInjector
from src.core.database.database_connection import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(question_bp, url_prefix='/questions')
app.register_blueprint(flight_bp, url_prefix='/flights')

@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "message": str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    FlaskInjector(app=app, modules=[configure_questions, configure_flight])
    app.run(debug=True, host='0.0.0.0', port=4000)
