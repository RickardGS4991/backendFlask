from src.modules.question.domain.repository.question_repository import IQuestionRepository
from src.modules.question.domain.datasource.question_datasource import IQuestionDatasource
from flask_injector import inject

class QuestionRepositoryImpl(IQuestionRepository):
    @inject
    def __init__(self, datasource: IQuestionDatasource):
        self.datasource = datasource

    def get_data(self):
        raw_data = self.datasource.fetch_data()
        return raw_data
