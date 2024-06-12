from abc import ABC, abstractmethod

class IFlightRepository(ABC):
    @abstractmethod
    def get_all_flights(self):
        pass

    @abstractmethod
    def airport_most_visited(self):
        pass

    @abstractmethod
    def airline_more_flight(self):
        pass

    @abstractmethod
    def day_more_visited(self):
        pass

    @abstractmethod
    def airlines_with_two(self):
        pass