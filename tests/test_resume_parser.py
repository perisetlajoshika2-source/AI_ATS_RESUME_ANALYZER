import pymupdf
import pytest
from io import BytesIO
from docx import Document

from backend.resume_parser import extract_resume_text

def create_pdf():
    pdf = pymupdf.open()
    page = pdf.new_page()

    page.insert_text(
        (50, 50),
        "Sample Candidate\nPython Developer\nSkills: Python, Django, SQL"
    )

    buffer = BytesIO()
    pdf.save(buffer)
    pdf.close()

    buffer.name = "sample.pdf"
    buffer.seek(0)

    return buffer

def create_docx():
    document = Document()

    document.add_heading("Sample Candidate", level=1)
    document.add_paragraph("Python Developer")
    document.add_paragraph("Skills: Python, Django, SQL")

    buffer = BytesIO()
    document.save(buffer)

    buffer.name = "sample.docx"
    buffer.seek(0)

    return buffer

def test_pdf_extraction():
    file = create_pdf()
    text = extract_resume_text(file)

    assert "Python Developer" in text
    assert "Django" in text

def test_docx_extraction():
    file = create_docx()
    text = extract_resume_text(file)

    assert "Python Developer" in text
    assert "Django" in text

def test_invalid_file():
    file = BytesIO(b"sample content")
    file.name = "sample.txt"

    with pytest.raises(ValueError):
        extract_resume_text(file)

def create_scanned_pdf():
    """Create a small image-based PDF for OCR testing."""

    source_pdf = pymupdf.open()
    page = source_pdf.new_page()

    page.insert_text(
        (50, 70),
        "OCR TEST RESUME\nPython Developer\nSkills: Python, Django, SQL",
        fontsize=18
    )

    # Create a smaller grayscale image
    pixmap = page.get_pixmap(
        dpi=120,
        colorspace=pymupdf.csGRAY,
        alpha=False
    )

    image_bytes = pixmap.tobytes("jpeg")
    source_pdf.close()

    # Create image-based PDF
    scanned_pdf = pymupdf.open()
    scanned_page = scanned_pdf.new_page()

    scanned_page.insert_image(
        scanned_page.rect,
        stream=image_bytes
    )

    buffer = BytesIO()
    scanned_pdf.save(buffer)
    scanned_pdf.close()

    buffer.name = "scanned_resume.pdf"
    buffer.seek(0)

    return buffer

def test_scanned_pdf_ocr():
    """Test OCR extraction from an image-based PDF."""

    file = create_scanned_pdf()
    text = extract_resume_text(file)

    assert "Python" in text
    assert "Django" in text
    assert "SQL" in text