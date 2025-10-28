from random import randint

def generate_test_cases_from_story(story):
    # Mock AI-generated test cases (replace later with real LLM)
    return [
        {
            "test_id": f"TC{randint(1000,9999)}",
            "story_id": story["id"],
            "test_case": f"Verify {story['title'].lower()} works as expected",
            "expected_result": "System behaves correctly"
        }
    ]
