import sqlite3
import json
from pathlib import Path
from datetime import datetime


# Database location
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "resume_analyzer.db"


def get_connection():
    """Create a database connection."""

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def create_table():
    """Create the analysis history table."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_filename TEXT NOT NULL,
            job_description TEXT NOT NULL,
            keyword_match_score REAL,
            semantic_similarity_score REAL,
            matched_skills TEXT,
            missing_skills TEXT,
            recommendations TEXT,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    resume_filename,
    job_description,
    keyword_match_score,
    semantic_similarity_score,
    matched_skills,
    missing_skills,
    recommendations
):
    """Save resume analysis results."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analysis_history (
            resume_filename,
            job_description,
            keyword_match_score,
            semantic_similarity_score,
            matched_skills,
            missing_skills,
            recommendations,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_filename,
        job_description,
        keyword_match_score,
        semantic_similarity_score,
        json.dumps(matched_skills),
        json.dumps(missing_skills),
        json.dumps(recommendations),
        datetime.now().isoformat()
    ))

    connection.commit()

    analysis_id = cursor.lastrowid

    connection.close()

    return analysis_id


def get_all_analyses():
    """Retrieve all saved analysis records."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM analysis_history
        ORDER BY id DESC
    """)

    records = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return records


def get_analysis_by_id(analysis_id):
    """Retrieve one analysis using its ID."""

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM analysis_history WHERE id = ?",
        (analysis_id,)
    )

    record = cursor.fetchone()

    connection.close()

    return dict(record) if record else None