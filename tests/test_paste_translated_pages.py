import pytest
import doc_fns
from pypdf import PdfReader
import tempfile
import os

def test_paste_translated_pages():
    original = PdfReader("pdfs/ai/original.pdf")
    translated_pages = PdfReader("pdfs/ai/translated_pages.pdf")
    writer = doc_fns.paste_translated_pages(original, translated_pages, [0, 1, 2])

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, "with_pasted_translated_pages.pdf")
        with open(temp_file_path, 'wb') as temp_file:
            writer.write(temp_file)

        written_file = PdfReader(temp_file_path)

        assert len(written_file.pages) == len(original.pages)
        assert all(written_file.pages[i].extract_text() == translated_pages.pages[i].extract_text() for i in [0])
        assert all(written_file.pages[i].extract_text() == original.pages[i].extract_text() for i in [3])