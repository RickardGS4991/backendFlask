from .owner_model import Owner
from typing import List, Optional

class QuestionModel:
    def __init__(
            self,
            tags: List[str],
            owner: Owner,
            is_answered: bool,
            view_count: int,
            accepted_answer_id: Optional[int],
            closed_date: Optional[int],
            answer_count:int,
            score: int,
            last_activity_date: int,
            creation_date: int,
            last_edit_date: Optional[int],
            question_id: int,
            content_license: Optional[str],
            link: str,
            closed_reason: Optional[str],
            title: str):
        self.tags = tags
        self.owner = owner
        self.is_answered = is_answered
        self.view_count = view_count
        self.accepted_answer_id = accepted_answer_id
        self.closed_date = closed_date
        self.answer_count = answer_count
        self.score = score
        self.last_activity_date = last_activity_date
        self.creation_date = creation_date
        self.last_edit_date = last_edit_date
        self.question_id = question_id
        self.content_license = content_license
        self.link = link
        self.closed_reason = closed_reason
        self.title = title

    def to_dict(self):
        return {
            "tags": self.tags,
            "owner": self.owner.to_dict(),
            "is_answered": self.is_answered,
            "view_count": self.view_count,
            "accepted_answer_id": self.accepted_answer_id,
            "closed_date": self.closed_date,
            "answer_count": self.answer_count,
            "score": self.score,
            "last_activity_date": self.last_activity_date,
            "creation_date": self.creation_date,
            "last_edit_date": self.last_edit_date,
            "question_id": self.question_id,
            "content_license": self.content_license,
            "link": self.link,
            "closed_option": self.closed_option,
            "title": self.title
        }