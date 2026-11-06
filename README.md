# AI ATS Resume Analyzer

## Project Overview
AI ATS Resume Analyzer is a Python-based application that analyzes resumes against job descriptions and helps candidates understand how well their skills match a job requirement.

## Features
- Upload PDF and DOCX resumes
- Extract resume text
- OCR support for scanned PDF files
- Job description analysis
- Keyword matching
- Semantic similarity analysis
- Matched and missing skills identification
- Basic resume improvement recommendations
- Analysis history
- FastAPI backend and Streamlit frontend

## Technologies Used
- Python
- Streamlit
- FastAPI
- SQLite
- PyMuPDF
- python-docx
- Tesseract OCR
- Sentence Transformers
- Scikit-learn
- Pytest

## Project Structure
```text
AI_ATS_RESUME_ANALYZER/
├── backend/
├── frontend/
├── prompts/
├── tests/
├── README.md
└── requirements.txt
```

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/perisetlajoshika2-source/AI_ATS_RESUME_ANALYZER.git
cd AI_ATS_RESUME_ANALYZER
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start FastAPI
```bash
python -m uvicorn backend.main:app --reload
```

### 5. Start Streamlit in another terminal
```bash
streamlit run frontend/app.py
```

## Note
The analysis scores are indicative project-generated results, not official ATS scores. Recommendations are based on basic rule-based logic.

## Developer
Perisetla Joshika

**Project:** AI ATS Resume Analyzer
