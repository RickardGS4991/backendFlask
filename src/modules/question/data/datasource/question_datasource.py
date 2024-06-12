from src.modules.question.domain.datasource.question_datasource import IQuestionDatasource
from config import API_URL
import requests
class QuestionDatasourceImpl(IQuestionDatasource):
    def fetch_data(self):
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()