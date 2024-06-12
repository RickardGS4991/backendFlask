from flask_injector import singleton
from ..controller.base.question_controller import IQuestionController
from ..controller.question_controller import QuestionControllerImpl
from src.modules.question.domain.repository.question_repository import IQuestionRepository
from src.modules.question.data.repository.question_repository import QuestionRepositoryImpl
from src.modules.question.domain.datasource.question_datasource import IQuestionDatasource
from src.modules.question.data.datasource.question_datasource import QuestionDatasourceImpl
from src.modules.question.domain.use_case.get_counter_answered import GetCounterAnsweredUseCase
from src.modules.question.domain.use_case.high_score_reputation import HighScoreReputationUsecase
from src.modules.question.domain.use_case.actual_old_answer import OldNewAnswerUsecase
from src.modules.question.domain.use_case.view_count import LessViewItemUsecase
from src.modules.question.domain.use_case.all_questions import AllQuestionUsecase


def configure(binder):
    binder.bind(IQuestionDatasource, to=QuestionDatasourceImpl, scope=singleton)
    binder.bind(IQuestionRepository, to=QuestionRepositoryImpl, scope=singleton)
    binder.bind(GetCounterAnsweredUseCase, to=GetCounterAnsweredUseCase, scope=singleton)
    binder.bind(HighScoreReputationUsecase, to=HighScoreReputationUsecase, scope=singleton)
    binder.bind(LessViewItemUsecase, to=LessViewItemUsecase, scope=singleton)
    binder.bind(AllQuestionUsecase, to=AllQuestionUsecase, scope=singleton)
    binder.bind(OldNewAnswerUsecase, to=OldNewAnswerUsecase, scope=singleton)
    binder.bind(IQuestionController, to=QuestionControllerImpl, scope=singleton)
