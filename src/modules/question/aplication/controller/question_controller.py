from .base.question_controller import IQuestionController
from src.modules.question.domain.use_case.get_counter_answered import GetCounterAnsweredUseCase
from src.modules.question.domain.use_case.all_questions import AllQuestionUsecase
from src.modules.question.domain.use_case.high_score_reputation import HighScoreReputationUsecase
from src.modules.question.domain.use_case.view_count import LessViewItemUsecase
from src.modules.question.domain.use_case.actual_old_answer import OldNewAnswerUsecase
from flask import jsonify
from flask_injector import inject
class QuestionControllerImpl(IQuestionController):
    @inject
    def __init__(
            self,
            get_counter_answered_use_case: GetCounterAnsweredUseCase,
            all_questions_use_case: AllQuestionUsecase,
            high_score_use_case: HighScoreReputationUsecase,
            less_view_count_item: LessViewItemUsecase,
            recent_oldest_items: OldNewAnswerUsecase
    ):
        self.get_counter_answered_use_case = get_counter_answered_use_case
        self.all_question_use_case = all_questions_use_case
        self.high_score_use_case = high_score_use_case
        self.less_view_count_item = less_view_count_item
        self.recent_oldest_items = recent_oldest_items

    def all_questions(self):
        questions = self.all_question_use_case.execute()
        return jsonify(questions)

    def count_answered(self):
        counter_answered = self.get_counter_answered_use_case.execute()
        print(counter_answered)
        return jsonify(counter_answered)

    def high_score_question(self):
        question = self.high_score_use_case.execute()
        print(question)
        return jsonify(question)

    def less_view_item(self):
        question = self.less_view_count_item.execute()
        print(question)
        return jsonify(question)

    def actual_oldest_items(self):
        questions = self.recent_oldest_items.execute()
        print(questions)
        return jsonify(questions)


