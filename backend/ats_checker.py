import re

STOPWORDS = {
    "the", "and", "for", "with", "you", "your",
    "are", "our", "this", "that", "will", "from",
    "have", "has", "who", "what", "when", "where",
    "can", "should", "must", "their", "they", "them",
    "into", "about", "using", "such", "all", "any",
    "years", "year", "work", "working", "role",
    "job", "candidate", "team", "ability",
    "required", "requirements", "skills", "skill",
    "welcome", "freshers", "fresher", "looking",
    "knowledge", "experience", "good", "strong",
    "excellent", "responsibilities", "responsibility"
}


def clean_text(text):
    """Convert text into normalized lowercase keywords."""

    if not isinstance(text, str):
        return []

    text = text.lower()

    # Preserve technical terms such as C++, C# and .NET
    words = re.findall(
        r"(?<!\w)(?:\.net|c\+\+|c#|[a-z0-9]+)(?!\w)",
        text
    )

    return words


def extract_keywords(job_description):
    """Extract meaningful keywords from a job description."""

    words = clean_text(job_description)

    keywords = {
        word for word in words
        if len(word) > 1 and word not in STOPWORDS
    }

    return keywords


def analyze_resume(resume_text, job_description):
    """Compare resume keywords with job description keywords."""

    resume_words = set(clean_text(resume_text))

    required_keywords = extract_keywords(job_description)

    matched_keywords = sorted(
        required_keywords.intersection(resume_words)
    )

    missing_keywords = sorted(
        required_keywords.difference(resume_words)
    )

    total_keywords = len(required_keywords)

    if total_keywords == 0:
        score = 0
    else:
        score = round(
            len(matched_keywords) / total_keywords * 100,
            2
        )

    return {
        "ats_score": score,
        "total_keywords": total_keywords,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }