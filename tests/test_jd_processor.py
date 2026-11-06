import pytest

from backend.jd_processor import (
    clean_text,
    extract_skills,
    extract_experience,
    extract_education,
    process_job_description
)


def test_clean_text():
    text = "Python    Developer"
    result = clean_text(text)
    assert result == "Python Developer"


def test_extract_skills():
    text = "We need Python, Django, MySQL and FastAPI."

    result = extract_skills(
        text,
        ["Python", "Django", "MySQL", "FastAPI"]
    )

    assert len(result) == 4
    assert "Python" in result
    assert "Django" in result
    assert "MySQL" in result
    assert "FastAPI" in result


def test_extract_experience():
    text = "Looking for a fresher Python Developer."
    result = extract_experience(text)

    assert "fresher" in result


def test_extract_education():
    text = "B.Tech or BCA graduates can apply."
    result = extract_education(text)

    assert "B.Tech" in result
    assert "BCA" in result


def test_process_job_description():
    jd = """
    Python Developer - Fresher
    Skills: Python, Django, MySQL, FastAPI.
    Good communication skills required.
    Qualification: B.Tech.
    """

    result = process_job_description(jd)

    assert "Python" in result["technical_skills"]
    assert "Django" in result["technical_skills"]
    assert "MySQL" in result["technical_skills"]
    assert "FastAPI" in result["technical_skills"]
    assert "Communication" in result["soft_skills"]
    assert "B.Tech" in result["education_requirements"]
    assert "Fresher" in result["experience_requirements"]


def test_empty_job_description():
    with pytest.raises(ValueError):
        process_job_description("")

