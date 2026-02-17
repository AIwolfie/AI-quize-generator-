# AI Quiz Generator API

A production-ready FastAPI project that generates quiz questions based on a given topic and difficulty level.

## Features
- **FastAPI**: Modern, fast (high-performance) web framework.
- **SQLite**: Local relational database.
- **Pydantic**: Data validation and architectural separation.
- **Background Tasks**: For simulating AI generation delay.
- **Logging**: Proper standard output logging.
- **Rule-based Generation**: Mocked AI logic for deterministic results.

## Project Structure
```text
quiz_api/
│── app/
│   ├── main.py             # Entry point
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # DB configuration
│   ├── quiz_generator.py   # "AI" Logic
│   ├── crud.py             # DB operations
│   ├── routes.py           # API Endpoints
│   ├── utils.py            # Logging & Helpers
│── requirements.txt        # Dependencies
│── README.md               # Instructions
```

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API**:
   ```bash
   python -m app.main
   # OR
   uvicorn app.main:app --reload
   ```

3. **API Documentation**:
   Once running, visit `http://127.0.0.1:8000/docs` for interactive Swagger UI.

## Example Usage

### 1. Generate a Quiz
**Request (cURL)**:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-quiz' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "python",
  "difficulty": "medium",
  "num_questions": 3
}'
```

**Response**:
```json
{
  "topic": "python",
  "difficulty": "medium",
  "id": 1,
  "created_at": "2024-05-20T10:00:00",
  "questions": [
    {
      "question_text": "What is the keyword used to define a function in Python?",
      "options": ["func", "define", "def", "function"],
      "correct_answer": "def",
      "id": 1,
      "quiz_id": 1
    },
    ...
  ]
}
```

### 2. Fetch a Quiz
**Request (cURL)**:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/quiz/1'
```

### 3. Health Check
**Request (cURL)**:
```bash
curl -X 'GET' 'http://127.0.0.1:8000/health'
```
