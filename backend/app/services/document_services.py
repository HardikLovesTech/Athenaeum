from pathlib import Path

from fastapi import UploadFile
from pypdf import PdfReader

def ExtractPdfText(File: UploadFile) -> str:
    if File.filename is None:
        raise ValueError("Fine name is missing")

    FilePath = Path(File.filename)

    if FilePath.suffix.lower() != ".pdf":
        raise ValueError("Only pdf files are supported")

    PdfReaderObject = PdfReader(File.file)

    TextParts : list[str] = []


    for Page in PdfReaderObject.pages:
        PageText = Page.extract_text()

        if PageText:
            TextParts.append(PageText)

    return "\n\n".join(TextParts).strip()