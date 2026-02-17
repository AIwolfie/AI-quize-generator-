from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def create_quiz(db: Session, quiz: schemas.QuizCreate) -> models.Quiz:
    db_quiz = models.Quiz(
        topic=quiz.topic,
        difficulty=quiz.difficulty
    )
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz

def create_question(db: Session, question: schemas.QuestionCreate, quiz_id: int) -> models.Question:
    db_question = models.Question(
        **question.dict(),
        quiz_id=quiz_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_quiz(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizzes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quiz).offset(skip).limit(limit).all()
