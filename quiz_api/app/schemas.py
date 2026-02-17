from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class QuestionBase(BaseModel):
    question_text: str
    options: List[str]
    correct_answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    quiz_id: int

    model_config = ConfigDict(from_attributes=True)

class QuizBase(BaseModel):
    topic: str
    difficulty: str

class QuizCreate(QuizBase):
    num_questions: int

class QuizResponse(QuizBase):
    id: int
    created_at: datetime
    questions: List[QuestionResponse]

    model_config = ConfigDict(from_attributes=True)

class HealthCheck(BaseModel):
    status: str
    version: str
