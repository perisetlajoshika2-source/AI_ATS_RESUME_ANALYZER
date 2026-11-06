import re


# Technical skills database
TECHNICAL_SKILLS = [
    "Python", "Java", "JavaScript", "C++", "C",
    "SQL", "MySQL", "PostgreSQL", "MongoDB",
    "HTML", "CSS", "React", "Angular",
    "Django", "Flask", "FastAPI",
    "Machine Learning", "Deep Learning",
    "Generative AI", "Artificial Intelligence",
    "NLP", "LLM", "LangChain", "RAG",
    "TensorFlow", "PyTorch",
    "Pandas", "NumPy",
    "REST API", "Git", "GitHub",
    "Docker", "AWS", "Azure",
    "Data Analysis", "Data Science",
    "Streamlit", "Power BI", "Excel"
]


# Soft skills database
SOFT_SKILLS = [
    "Communication",
    "Teamwork",
    "Problem Solving",
    "Leadership",
    "Time Management",
    "Critical Thinking",
    "Adaptability",
    "Creativity",
    "Analytical Skills"
]


def clean_text(text):
    """Clean and normalize job description text."""

    if not isinstance(text, str):
        raise ValueError("Job description must be text.")

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_skills(text, skill_list):
    """Extract matching skills from text."""

    text = clean_text(text).lower()
    found_skills = []

    for skill in skill_list:

        pattern = (
            r"(?<![a-z0-9])"
            + re.escape(skill.lower())
            + r"(?![a-z0-9])"
        )

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def extract_experience(text):
    """Extract experience requirements from job description."""

    patterns = [
        r"\b\d+\s*[-to]+\s*\d+\s*years?\b",
        r"\b\d+\+?\s*years?\b",
        r"\bfresher\b",
        r"\bentry[- ]level\b",
        r"\bno experience required\b"
    ]

    matches = []

    for pattern in patterns:
        results = re.findall(pattern, text, re.IGNORECASE)
        matches.extend(results)

    return list(dict.fromkeys(matches))


def extract_education(text):
    """Identify educational qualifications."""

    education_keywords = [
        "B.Tech",
        "B.E",
        "B.Sc",
        "BCA",
        "MCA",
        "M.Tech",
        "M.Sc",
        "MBA",
        "Bachelor's degree",
        "Master's degree",
        "Graduation",
        "Computer Science",
        "Information Technology"
    ]

    text = clean_text(text).lower()

    found_education = []

    for qualification in education_keywords:

        pattern = (
            r"(?<![a-z0-9])"
            + re.escape(qualification.lower())
            + r"(?![a-z0-9])"
        )

        if re.search(pattern, text):
            found_education.append(qualification)

    return found_education


def process_job_description(job_description):
    """
    Process a job description and return
    structured requirements.
    """

    text = clean_text(job_description)

    if not text:
        raise ValueError("Job description cannot be empty.")

    technical_skills = extract_skills(
        text,
        TECHNICAL_SKILLS
    )

    soft_skills = extract_skills(
        text,
        SOFT_SKILLS
    )

    experience = extract_experience(text)

    education = extract_education(text)

    return {
        "job_description": text,
        "technical_skills": technical_skills,
        "soft_skills": soft_skills,
        "experience_requirements": experience,
        "education_requirements": education
    }