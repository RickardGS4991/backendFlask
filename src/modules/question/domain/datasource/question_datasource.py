from abc import ABC, abstractmethod

class IQuestionDatasource(ABC):
    @abstractmethod
    def fetch_data(self):
        pass