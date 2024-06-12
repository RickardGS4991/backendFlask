DROP TABLE IF EXISTS country_flights;
DROP TABLE IF EXISTS movements;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS airlines;

CREATE TABLE airlines (
    id_airline INT PRIMARY KEY,
    airline_name VARCHAR(255) NOT NULL
);

INSERT INTO airlines(id_airline, airline_name) VALUES
(1, 'Volaris'),
(2, 'Aeromar'),
(3, 'Interjet'),
(4, 'Aeromexico');

CREATE TABLE airports (
    id_airport INT PRIMARY KEY,
    airport_name VARCHAR(255) NOT NULL
);

INSERT INTO airports (id_airport, airport_name) VALUES
(1, 'Benito Juarez'),
(2, 'Guanajuato'),
(3, 'La paz'),
(4, 'Oaxaca');

CREATE TABLE movements (
    id_movement INT PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

INSERT INTO movements (id_movement, description) VALUES
(1, 'Salida'),
(2, 'Llegada');

CREATE TABLE country_flights (
    id_flight INT AUTO_INCREMENT PRIMARY KEY,
    id_airline INT,
    id_airport INT,
    id_movement INT,
    date_arrive DATE,
    FOREIGN KEY (id_airline) REFERENCES airlines(id_airline),
    FOREIGN KEY (id_airport) REFERENCES airports(id_airport),
    FOREIGN KEY (id_movement) REFERENCES movements(id_movement)
);

INSERT INTO country_flights (id_airline, id_airport, id_movement, date_arrive) VALUES
(1, 1, 1, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(3, 2, 2, '2021-05-02'),
(4, 3, 2, '2021-05-02'),
(1, 3, 2, '2021-05-02'),
(2, 1, 1, '2021-05-02'),
(2, 3, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04'),
(3, 4, 1, '2021-05-04');