import pytest
from backend.database import (
    create_table,
    save_analysis,
    get_all_analyses,
    get_analysis_by_id
)


def test_database_operations(tmp_path, monkeypatch):

    import backend.database as database

    # Use a temporary database for testing
    test_db = tmp_path / "test_database.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    create_table()

    analysis_id = save_analysis(
        resume_filename="sample_resume.pdf",
        job_description="Python Developer with Django and SQL",
        keyword_match_score=75.0,
        semantic_similarity_score=82.5,
        matched_skills=["Python", "Django"],
        missing_skills=["FastAPI"],
        recommendations=["Learn FastAPI"]
    )

    assert analysis_id == 1

    records = get_all_analyses()

    assert len(records) == 1
    assert records[0]["resume_filename"] == "sample_resume.pdf"

    record = get_analysis_by_id(analysis_id)

    assert record is not None
    assert record["keyword_match_score"] == 75.0
    assert record["semantic_similarity_score"] == 82.5


def test_get_analysis_by_invalid_id(tmp_path, monkeypatch):

    import backend.database as database

    test_db = tmp_path / "test_database.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db)

    create_table()

    result = get_analysis_by_id(999)

    assert result is None