import pytest
from backend.ai_analyzer import analyze_resume_with_ai


def test_analyze_resume_with_ai():

    resume_text = """
    B.Tech graduate with Python, Django, SQL and MySQL skills.
    Completed a Restaurant Management project using Django.
    """

    job_description = """
    Looking for a Python Developer with Python, Django,
    SQL, FastAPI and communication skills.
    """

    result = analyze_resume_with_ai(resume_text, job_description)

    assert result["success"] is True
    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["missing_skills"]
    assert 0 <= result["semantic_similarity_score"] <= 100
    assert len(result["recommendations"]) > 0


def test_empty_resume():

    with pytest.raises(ValueError):
        analyze_resume_with_ai("", "Python Developer")


def test_empty_job_description():

    with pytest.raises(ValueError):
        analyze_resume_with_ai("Python Developer", "")

        