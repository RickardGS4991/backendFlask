from flask import Blueprint
from ..controller.base.question_controller import IQuestionController
from flask_injector import inject

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
@inject
def questions(controller: IQuestionController):
    return controller.all_questions()

@bp.route('/counter-answered', methods=['GET'])
@inject
def counter_answered(controller: IQuestionController):
    return controller.count_answered()

@bp.route('/high-score', methods=['GET'])
@inject
def high_question(controller: IQuestionController):
    return controller.high_score_question()

@bp.route('/view-less-item', methods=['GET'])
@inject
def less_item_view(controller: IQuestionController):
    return controller.less_view_item()

@bp.route('/recent-oldest-items', methods=['GET'])
@inject
def oldest_mostrecent_items(controller: IQuestionController):
    return controller.less_view_item()

