from abc import ABC, abstractmethod

class IQuestionController(ABC):
    @abstractmethod
    def all_questions(self):
        pass
    @abstractmethod
    def count_answered(self):
        pass

    @abstractmethod
    def high_score_question(self):
        pass

    @abstractmethod
    def less_view_item(self):
        pass

    @abstractmethod
    def actual_oldest_items(self):
        pass

