from fastapi import FastAPI # type: ignore
from .rally_mock import get_mock_rally_stories
from .ai_generator import generate_test_cases_from_story

app = FastAPI(title="QA AI TestGen")

@app.get("/")
def read_root():
    return {"message": "Welcome to QA-AI-TestGen 🚀", "status": "running"}

@app.get("/rally-stories")
def get_stories():
    """Fetches mock Rally stories."""
    stories = get_mock_rally_stories()
    return {"stories": stories}

@app.post("/generate-testcases")
def generate_testcases(story_id: str):
    return {
        "story_id": story_id,
        "testcases": [
            {"id": "TC001", "title": "Verify input validation"},
            {"id": "TC002", "title": "Check API response for valid payload"},
        ],
    }

