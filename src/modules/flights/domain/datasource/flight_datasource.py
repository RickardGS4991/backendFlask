from abc import ABC, abstractmethod

class IFlightDatasource(ABC):
    @abstractmethod
    def get_all_flights(self):
        pass

    @abstractmethod
    def airport_most_visited(self):
        pass

    @abstractmethod
    def airline_with_more_flights(self):
        pass

    @abstractmethod
    def day_with_more_visits(self):
        pass

    @abstractmethod
    def airlines_two_flights(self):
        pass
