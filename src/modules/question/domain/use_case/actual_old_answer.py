from ..repository.question_repository import IQuestionRepository
from flask_injector import inject
from datetime import datetime

class OldNewAnswerUsecase:
    @inject
    def __init__(self, repository: IQuestionRepository):
        self.repository: repository

    def execute(self):
        data = self.repository.get_data()

        for item in data['items']:
            item['creation_date'] = datetime.fromtimestamp(item['creation_date'])
            print(f"Converted creation_date for item {item['question_id']}: {item['creation_date']}")

        most_recent_question = max(data['items'], key=lambda item: item['creation_date'])
        oldest_question = min(data['items'], key=lambda item: item['creation_date'])

        print("Most recent question:", most_recent_question)
        print("Oldest question:", oldest_question)

        items = {
            "most_recent_question": self.format_item(most_recent_question),
            "oldest_question": self.format_item(oldest_question),
        }

        return items

    def format_item(self, item):
        return {
            "tags": item['tags'],
            "owner": item['owner'],
            "is_answered": item['is_answered'],
            "view_count": item['view_count'],
            "answer_count": item['answer_count'],
            "score": item['score'],
            "last_activity_date": item['last_activity_date'],
            "creation_date": item['creation_date'].isoformat(),
            "last_edit_date": item['last_edit_date'],
            "question_id": item['question_id'],
            "content_license": item['content_license'],
            "link": item['link'],
            "title": item['title'],
        }