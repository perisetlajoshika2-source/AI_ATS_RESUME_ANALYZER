import pytest
import numpy as np

from backend import semantic_matcher


class FakeModel:
    """Mock model to test without downloading the AI model."""

    def encode(self, text, convert_to_numpy=True):
        if "python" in text.lower():
            return np.array([1.0, 0.0, 0.0])

        if "django" in text.lower():
            return np.array([0.0, 1.0, 0.0])

        return np.array([0.0, 0.0, 1.0])


@pytest.fixture
def mock_model(monkeypatch):
    monkeypatch.setattr(
        semantic_matcher,
        "model",
        FakeModel()
    )


def test_generate_embedding(mock_model):
    result = semantic_matcher.generate_embedding(
        "Python Developer"
    )

    assert isinstance(result, np.ndarray)
    assert len(result) == 3


def test_empty_embedding():
    with pytest.raises(ValueError):
        semantic_matcher.generate_embedding("")


def test_calculate_similarity(mock_model):
    score = semantic_matcher.calculate_similarity(
        "Python Developer",
        "Python Developer"
    )

    assert score == 100.0


def test_similarity_range(mock_model):
    score = semantic_matcher.calculate_similarity(
        "Python Developer",
        "Django Developer"
    )

    assert 0 <= score <= 100


def test_compare_resume_with_jd(mock_model):
    result = semantic_matcher.compare_resume_with_jd(
        "Python Developer",
        "Python Developer"
    )

    assert "semantic_similarity_score" in result
    assert "matching_method" in result
    assert result["semantic_similarity_score"] == 100.0