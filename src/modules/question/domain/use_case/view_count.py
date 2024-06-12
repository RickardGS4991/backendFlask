from src.modules.question.domain.repository.question_repository import IQuestionRepository
from flask_injector import inject

class LessViewItemUsecase:
    @inject
    def __init__(self,repository: IQuestionRepository):
        self.repository = repository

    def execute(self):
        questions = self.repository.get_data()
        less_view_count = min(questions['items'], key=lambda item: item['view_count'])
        return less_view_count

