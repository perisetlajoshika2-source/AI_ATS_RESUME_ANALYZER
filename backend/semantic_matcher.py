from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the pre-trained embedding model
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = None


def load_model():
    """Load the Sentence Transformer model."""

    global model

    if model is None:
        model = SentenceTransformer(MODEL_NAME)

    return model


def generate_embedding(text):
    """Convert text into numerical embeddings."""

    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input text cannot be empty.")

    embedding_model = load_model()

    embedding = embedding_model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding


def calculate_similarity(resume_text, job_description):
    """Calculate semantic similarity between resume and JD."""

    resume_embedding = generate_embedding(resume_text)
    jd_embedding = generate_embedding(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    similarity_percentage = round(
        float(similarity) * 100, 2
    )

    return similarity_percentage


def compare_resume_with_jd(resume_text, job_description):
    """Compare resume and job description semantically."""

    similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    return {
        "semantic_similarity_score": similarity_score,
        "matching_method": "Sentence Transformers + Cosine Similarity"
    }