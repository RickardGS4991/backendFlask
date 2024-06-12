from abc import ABC, abstractmethod

class IFlightController(ABC):
    @abstractmethod
    def get_flights(self):
        pass

    @abstractmethod
    def visited_most_airport(self):
        pass

    @abstractmethod
    def airline_most_visited(self):
        pass

    @abstractmethod
    def more_visited_day(self):
        pass

    @abstractmethod
    def get_airline_with_more_two(self):
        pass