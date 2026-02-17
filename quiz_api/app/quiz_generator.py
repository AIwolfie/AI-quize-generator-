import random
import time
from typing import List, Dict
from .schemas import QuestionCreate

# Simple template-based quiz generator
TEMPLATES = {
    "python": [
        {
            "q": "What is the keyword used to define a function in Python?",
            "o": ["func", "define", "def", "function"],
            "a": "def"
        },
        {
            "q": "Which data structure is mutable in Python?",
            "o": ["tuple", "list", "string", "integer"],
            "a": "list"
        },
        {
            "q": "How do you start a comment in Python?",
            "o": ["//", "/*", "#", "--"],
            "a": "#"
        },
        {
            "q": "What does PEP 8 stand for?",
            "o": ["Python Enhancement Program 8", "Python Error Protocol 8", "Python Enhancement Proposal 8", "Practical English Proof 8"],
            "a": "Python Enhancement Proposal 8"
        },
        {
            "q": "Which of these is used to handle exceptions in Python?",
            "o": ["try-except", "catch-throw", "handle-error", "if-else"],
            "a": "try-except"
        }
    ],
    "geography": [
        {
            "q": "What is the capital of France?",
            "o": ["London", "Berlin", "Paris", "Madrid"],
            "a": "Paris"
        },
        {
            "q": "Which is the largest continent?",
            "o": ["Africa", "Asia", "Europe", "North America"],
            "a": "Asia"
        },
        {
            "q": "What is the longest river in the world?",
            "o": ["Amazon", "Nile", "Yangtze", "Mississippi"],
            "a": "Nile"
        }
    ],
    "science": [
        {
            "q": "What is the chemical symbol for water?",
            "o": ["CO2", "H2O", "O2", "NaCl"],
            "a": "H2O"
        },
        {
            "q": "Which planet is known as the Red Planet?",
            "o": ["Venus", "Mars", "Jupiter", "Saturn"],
            "a": "Mars"
        }
    ]
}

DEFAULT_QUESTIONS = [
    {
        "q": "What is 2 + 2?",
        "o": ["3", "4", "5", "6"],
        "a": "4"
    },
    {
        "q": "Who wrote 'Romeo and Juliet'?",
        "o": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "a": "William Shakespeare"
    }
]

def generate_questions(topic: str, difficulty: str, num: int) -> List[QuestionCreate]:
    """
    Simulates AI generation with templates and randomized selection.
    """
    # Simulate AI delay
    time.sleep(1) 
    
    topic_key = topic.lower()
    available_pool = TEMPLATES.get(topic_key, DEFAULT_QUESTIONS)
    
    # If we need more than available, we shuffle and repeat or use defaults
    pool = available_pool * (num // len(available_pool) + 1)
    selected = random.sample(pool, num)
    
    results = []
    for item in selected:
        results.append(QuestionCreate(
            question_text=item["q"],
            options=item["o"],
            correct_answer=item["a"]
        ))
    
    return results
