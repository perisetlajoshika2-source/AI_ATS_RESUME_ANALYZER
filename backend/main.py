from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from backend.resume_parser import extract_resume_text
from backend.ats_checker import analyze_resume
from backend.ai_analyzer import analyze_resume_with_ai
from backend.database import (
    create_table,
    save_analysis,
    get_all_analyses,
    get_analysis_by_id
)

app = FastAPI(
    title="AI ATS Resume Analyzer",
    description="API for resume parsing and job description matching",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    create_table()


@app.get("/")
def home():
    return {
        "message": "AI ATS Resume Analyzer API is running successfully!"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/analyze-resume")
async def analyze_resume_api(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        # Validate file and extract resume text
        resume_text = extract_resume_text(file)

        # Keyword analysis
        keyword_result = analyze_resume(
            resume_text,
            job_description
        )

        # AI and semantic analysis
        ai_result = analyze_resume_with_ai(
            resume_text,
            job_description
        )

        # Save results in database
        analysis_id = save_analysis(
            resume_filename=file.filename,
            job_description=job_description,
            keyword_match_score=keyword_result["ats_score"],
            semantic_similarity_score=ai_result[
                "semantic_similarity_score"
            ],
            matched_skills=ai_result["matched_skills"],
            missing_skills=ai_result["missing_skills"],
            recommendations=ai_result["recommendations"]
        )

        return {
            "success": True,
            "analysis_id": analysis_id,
            "resume_filename": file.filename,
            "keyword_match_score": keyword_result["ats_score"],
            "matched_keywords": keyword_result["matched_keywords"],
            "missing_keywords": keyword_result["missing_keywords"],
            "semantic_similarity_score": ai_result[
                "semantic_similarity_score"
            ],
            "matched_skills": ai_result["matched_skills"],
            "missing_skills": ai_result["missing_skills"],
            "recommendations": ai_result["recommendations"]
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Resume analysis failed: {str(error)}"
        )


@app.get("/history")
def analysis_history():
    return get_all_analyses()


@app.get("/history/{analysis_id}")
def analysis_details(analysis_id: int):
    record = get_analysis_by_id(analysis_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Analysis record not found"
        )

    return record