import pytest

from backend.ats_checker import (
    clean_text,
    extract_keywords,
    analyze_resume
)


def test_clean_text():
    result = clean_text("Python Developer")

    assert result == ["python", "developer"]


def test_extract_keywords():
    jd = "Python Developer with Django and MySQL skills"

    result = extract_keywords(jd)

    assert "python" in result
    assert "django" in result
    assert "mysql" in result


def test_analyze_resume():
    resume = "Python Django HTML CSS"
    jd = "Python Django MySQL FastAPI"

    result = analyze_resume(resume, jd)

    assert result["ats_score"] == 50.0
    assert result["total_keywords"] == 4

    assert "python" in result["matched_keywords"]
    assert "django" in result["matched_keywords"]

    assert "mysql" in result["missing_keywords"]
    assert "fastapi" in result["missing_keywords"]


def test_empty_resume():
    result = analyze_resume(
        "",
        "Python Django MySQL"
    )

    assert result["ats_score"] == 0


def test_empty_job_description():
    result = analyze_resume(
        "Python Django",
        ""
    )

    assert result["ats_score"] == 0