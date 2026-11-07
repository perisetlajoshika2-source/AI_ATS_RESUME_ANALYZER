# AI ATS Resume Analyzer – Prompt Documentation

## 1. Project Overview

**Project Name:** AI ATS Resume Analyzer

**Objective:** To develop an application that analyzes resumes against job descriptions and identifies matching skills, missing skills, keyword matches and areas for improvement.

## 2. AI Tools Used

- ChatGPT – Project planning, code assistance, debugging and explanations.
- GitHub Copilot – AI-assisted coding support, where applicable.
- Sentence Transformers – Semantic similarity using the `all-MiniLM-L6-v2` pretrained model.
- Python development tools – Implementation and testing.

## 3. Prompt Engineering Approach

The project was developed incrementally by dividing the application into smaller modules. Prompts were refined based on errors, expected outputs and testing results.

The following sections describe representative prompts used during development. They are consolidated examples, not a verbatim record of every original conversation.

## 4. Prompts Used During Development

### Prompt 1: Project Planning

"Help me plan a Python-based AI ATS Resume Analyzer. It should accept PDF and DOCX resumes, compare them with job descriptions, identify matching and missing skills, and provide recommendations. Suggest a suitable project architecture."

### Prompt 2: Resume Parsing

"Help me develop a Python module to extract text from PDF and DOCX resumes. Use PyMuPDF for PDF files and python-docx for DOCX files. Include appropriate error handling and support for scanned PDFs using OCR."

### Prompt 3: Job Description Processing

"Help me create a Python module that processes job descriptions and identifies important skills, experience requirements and educational qualifications."

### Prompt 4: Keyword Matching

"Develop a keyword matching module that compares resume content with a job description. Identify matched and missing keywords and calculate a keyword match percentage."

### Prompt 5: Semantic Similarity

"Help me implement semantic similarity between a resume and a job description using the Sentence Transformers model all-MiniLM-L6-v2 and cosine similarity."

### Prompt 6: Resume Analysis

"Help me combine resume parsing, job description processing, keyword matching and semantic similarity into a single analysis module. Return the scores, matched skills, missing skills and basic recommendations."

### Prompt 7: Database Integration

"Help me create an SQLite database module to store resume analysis results and retrieve previous analysis records."

### Prompt 8: FastAPI Backend

"Help me build a FastAPI backend for the resume analyzer. Include endpoints for health checking, resume analysis and retrieving analysis history."

### Prompt 9: Streamlit Frontend

"Help me create a Streamlit interface for the AI ATS Resume Analyzer. Include resume upload, job description input, analysis results, analysis history and an About Project page."

### Prompt 10: Testing and Debugging

"Help me write pytest test cases for the resume parser, keyword checker, semantic matcher, database functions and API endpoints. Help identify and fix errors based on the test results."

## 5. Prompt Refinement Process

During development, the initial prompts were refined to address specific implementation requirements.

The refinement process included:

1. Dividing large development tasks into smaller modules.
2. Providing relevant code and error messages when debugging.
3. Refining instructions based on expected outputs.
4. Testing individual modules before integration.
5. Improving error handling and application functionality.

## 6. Challenges Addressed

- Extracting text from different resume formats.
- Supporting scanned PDF documents through OCR.
- Comparing resume keywords with job descriptions.
- Implementing semantic similarity.
- Connecting the FastAPI backend with Streamlit.
- Storing and retrieving analysis history.
- Testing individual modules and application functionality.

## 7. Final Project Outcome

The final application includes:

- PDF and DOCX resume upload.
- Scanned PDF text extraction using OCR.
- Keyword matching.
- Semantic similarity analysis.
- Matched and missing skills.
- Basic resume improvement recommendations.
- SQLite-based analysis history.
- FastAPI backend.
- Streamlit user interface.
- Automated tests using pytest.

## 8. API and AI Implementation Clarification

This project does not use Groq or an external LLM API key.

Semantic similarity is implemented using the pretrained Sentence Transformers model. The recommendations are generated using basic rule-based logic.

The displayed analysis scores are project-generated indicators and are not official scores from any company's Applicant Tracking System.

## 9. Conclusion

AI assistance was used throughout the development process for planning, understanding concepts, code assistance, debugging and testing.

The project demonstrates the practical use of Python, NLP techniques, semantic similarity, prompt engineering, FastAPI, Streamlit and SQLite in developing an AI-assisted resume analysis application.
