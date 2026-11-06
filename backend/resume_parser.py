import pymupdf
from docx import Document
import re


# Maximum file size: 5 MB
MAX_FILE_SIZE = 5 * 1024 * 1024


def get_filename(file):
    """Get filename from normal file or FastAPI UploadFile."""

    return (
        getattr(file, "filename", None)
        or getattr(file, "name", None)
    )


def get_file_object(file):
    """Get the actual file stream."""

    return getattr(file, "file", file)


def validate_resume_file(file):
    """Validate resume extension and file size."""

    filename = get_filename(file)

    if not filename:
        raise ValueError("Filename is missing.")

    filename = filename.lower()

    if not filename.endswith((".pdf", ".docx")):
        raise ValueError("Only PDF and DOCX files are supported.")

    file_object = get_file_object(file)

    file_object.seek(0, 2)
    file_size = file_object.tell()
    file_object.seek(0)

    if file_size == 0:
        raise ValueError("Uploaded file is empty.")

    if file_size > MAX_FILE_SIZE:
        raise ValueError("File size should not exceed 5 MB.")

    return True


def clean_text(text):
    """Clean unnecessary spaces while preserving line breaks."""

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def extract_text_from_pdf(file):
    """Extract text from normal and scanned PDFs."""

    extracted_text = ""
    file_object = get_file_object(file)

    try:
        file_object.seek(0)
        pdf_data = file_object.read()

        with pymupdf.open(
            stream=pdf_data,
            filetype="pdf"
        ) as pdf_document:

            for page in pdf_document:

                page_text = page.get_text("text")

                # OCR for scanned PDFs
                if not page_text.strip():

                    ocr_textpage = page.get_textpage_ocr(
                        language="eng",
                        dpi=300,
                        full=True,
                        tessdata=r"C:\Program Files\Tesseract-OCR\tessdata"
                    )

                    page_text = page.get_text(
                        "text",
                        textpage=ocr_textpage
                    )

                extracted_text += page_text + "\n"

    except Exception as e:
        raise ValueError(f"Unable to read PDF file: {str(e)}")

    return extracted_text


def extract_text_from_docx(file):
    """Extract text from DOCX files."""

    extracted_text = ""
    file_object = get_file_object(file)

    try:
        file_object.seek(0)

        document = Document(file_object)

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                extracted_text += paragraph.text + "\n"

        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    extracted_text += cell.text + "\n"

    except Exception as e:
        raise ValueError(f"Unable to read DOCX file: {str(e)}")

    return extracted_text


def extract_resume_text(file):
    """Main function to extract resume text."""

    validate_resume_file(file)

    filename = get_filename(file).lower()

    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)

    else:
        raise ValueError("Unsupported file format.")

    text = clean_text(text)

    if not text:
        raise ValueError(
            "No readable text found in the resume."
        )

    return text