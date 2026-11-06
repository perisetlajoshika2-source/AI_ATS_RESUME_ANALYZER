import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

# Page configuration
st.set_page_config(
    page_title="AI ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Header
st.title("📄 AI ATS Resume Analyzer")

st.write(
    "Analyze your resume against a job description "
    "using NLP, keyword matching and semantic similarity."
)

st.divider()

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Resume Analyzer", "Analysis History", "About Project"]
)

# Resume Analyzer
if page == "Resume Analyzer":

    st.header("Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload your resume (PDF or DOCX)",
        type=["pdf", "docx"]
    )

    job_description = st.text_area(
        "Enter Job Description",
        height=220,
        placeholder="Paste the complete job description here..."
    )

    if st.button("🚀 Analyze Resume", type="primary"):

        if uploaded_file is None:
            st.error("Please upload your resume.")

        elif not job_description.strip():
            st.error("Please enter a job description.")

        else:
            try:
                with st.spinner("Analyzing your resume..."):

                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    }

                    data = {
                        "job_description": job_description
                    }

                    response = requests.post(
                        f"{API_URL}/analyze-resume",
                        files=files,
                        data=data,
                        timeout=180
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("Resume analysis completed!")

                        st.divider()

                        st.subheader("📊 Analysis Scores")

                        col1, col2 = st.columns(2)

                        keyword_score = result["keyword_match_score"]
                        semantic_score = result[
                            "semantic_similarity_score"
                        ]

                        with col1:
                            st.metric(
                                "Keyword Match Score",
                                f"{keyword_score}%"
                            )
                            st.progress(
                                max(0, min(100, keyword_score)) / 100
                            )

                        with col2:
                            st.metric(
                                "Semantic Similarity",
                                f"{semantic_score}%"
                            )
                            st.progress(
                                max(0, min(100, semantic_score)) / 100
                            )

                        st.info(
                            "These are project-generated matching scores, "
                            "not official ATS scores."
                        )

                        st.divider()

                        st.subheader("✅ Matched Skills")

                        matched = result["matched_skills"]

                        if matched:
                            st.write(", ".join(matched))
                        else:
                            st.info("No matching skills found.")

                        st.subheader("❌ Missing Skills")

                        missing = result["missing_skills"]

                        if missing:
                            st.write(", ".join(missing))
                        else:
                            st.success("No missing skills found.")

                        st.divider()

                        st.subheader("🔍 Keyword Analysis")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.write("Matched Keywords")
                            st.write(result["matched_keywords"])

                        with col2:
                            st.write("Missing Keywords")
                            st.write(result["missing_keywords"])

                        st.divider()

                        st.subheader("💡 Recommendations")

                        for recommendation in result["recommendations"]:
                            st.write("• " + recommendation)

                        st.caption(
                            f"Analysis ID: {result['analysis_id']}"
                        )

                    else:
                        st.error(
                            f"Backend error ({response.status_code}): "
                            f"{response.text}"
                        )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to FastAPI. "
                    "Please start the backend server first."
                )

            except requests.exceptions.Timeout:
                st.error(
                    "Analysis timed out. Please try again."
                )

            except Exception as error:
                st.error(f"Analysis failed: {error}")


# Analysis History
elif page == "Analysis History":

    st.header("📚 Previous Analysis History")

    if st.button("Refresh History"):

        try:
            response = requests.get(
                f"{API_URL}/history",
                timeout=30
            )

            if response.status_code == 200:

                records = response.json()

                if records:
                    st.success(
                        f"Found {len(records)} analysis records."
                    )

                    for record in records:

                        with st.expander(
                            f"Analysis #{record['id']} - "
                            f"{record['resume_filename']}"
                        ):

                            st.write(
                                "Keyword Score:",
                                record["keyword_match_score"]
                            )

                            st.write(
                                "Semantic Score:",
                                record["semantic_similarity_score"]
                            )

                            st.write(
                                "Job Description:",
                                record["job_description"]
                            )

                            st.write(
                                "Date:",
                                record["created_at"]
                            )

                else:
                    st.info("No analysis history available.")

            else:
                st.error("Unable to retrieve analysis history.")

        except requests.exceptions.ConnectionError:
            st.error("FastAPI server is not running.")

        except Exception as error:
            st.error(str(error))


# About Project
elif page == "About Project":

    st.header("About AI ATS Resume Analyzer")

    st.write("""
    This project analyzes resumes against job descriptions.

    **Technologies Used:**

    - Python
    - Streamlit
    - FastAPI
    - SQLite
    - PyMuPDF
    - Python-docx
    - Sentence Transformers
    - NLP
    - Cosine Similarity

    **Main Features:**

    - PDF and DOCX resume upload
    - Scanned PDF text extraction using OCR
    - Keyword matching
    - Semantic similarity analysis
    - Matched and missing skills
    - Resume improvement recommendations
    - Analysis history
    """)