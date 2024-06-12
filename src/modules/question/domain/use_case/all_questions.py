from src.modules.question.domain.repository.question_repository import IQuestionRepository
from flask_injector import inject

class AllQuestionUsecase:
    @inject
    def __init__(self, repository: IQuestionRepository):
        self.repository = repository

    def execute(self):
        data = self.repository.get_data()
        return data