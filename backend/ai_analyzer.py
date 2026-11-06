from backend.jd_processor import process_job_description
from backend.semantic_matcher import compare_resume_with_jd


def analyze_resume_with_ai(resume_text, job_description):

    if not isinstance(resume_text, str) or not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not isinstance(job_description, str) or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    # Process job description
    jd_analysis = process_job_description(job_description)

    # Get required skills
    required_skills = (
        jd_analysis["technical_skills"]
        + jd_analysis["soft_skills"]
    )

    # Identify matching and missing skills
    resume_lower = resume_text.lower()

    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in resume_lower
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in resume_lower
    ]

    # Calculate semantic similarity
    semantic_result = compare_resume_with_jd(
        resume_text,
        job_description
    )

    # Generate recommendations
    recommendations = []

    if missing_skills:
        recommendations.append(
            "Consider learning these skills: "
            + ", ".join(missing_skills)
        )

    if "project" not in resume_lower:
        recommendations.append(
            "Add relevant projects to demonstrate practical experience."
        )

    if not recommendations:
        recommendations.append(
            "Add measurable achievements to make your resume stronger."
        )

    return {
        "success": True,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "semantic_similarity_score": semantic_result[
            "semantic_similarity_score"
        ],
        "recommendations": recommendations,
        "analysis_method": "NLP + Sentence Transformers"
    }