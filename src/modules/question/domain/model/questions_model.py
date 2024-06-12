from .question_model import QuestionModel
from typing import List

class QuestionsModel:
    def __init__(self, items: List[QuestionModel]):
        self.items = items