from abc import ABC, abstractmethod

class IQuestionRepository(ABC):
    @abstractmethod
    def get_data(self):
        pass
