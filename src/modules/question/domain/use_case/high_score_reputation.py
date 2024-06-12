from src.modules.question.domain.repository.question_repository import IQuestionRepository
from flask_injector import inject

class HighScoreReputationUsecase:
    @inject
    def __init__(self, repository: IQuestionRepository):
        self.repository = repository

    def execute(self):
        data = self.repository.get_data()
        high_score_question = max(data['items'], key=lambda item: item['score'])
        return high_score_question