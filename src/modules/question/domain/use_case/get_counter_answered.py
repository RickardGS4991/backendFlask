from src.modules.question.domain.repository.question_repository import IQuestionRepository
from flask_injector import inject
class GetCounterAnsweredUseCase:
    @inject
    def __init__(self, repository: IQuestionRepository):
        self.repository = repository

    def execute(self):
        raw_data = self.repository.get_data()
        answered_true = sum(1 for item in raw_data['items'] if item['is_answered'])
        answered_false = sum(1 for item in raw_data['items'] if not item['is_answered'])
        return {
            "answered_true": answered_true,
            "answered_false": answered_false
        }
