import pytest
import doc_fns
from pypdf import PdfReader


def test_page_subset_full_range():
    reader = PdfReader("pdfs/ai/original.pdf")
    assert list(doc_fns.page_subset(reader, range(0, len(reader.pages)))) # full range


def test_page_subset_excessive_pages():
    reader = PdfReader("pdfs/ai/original.pdf")
    with pytest.raises(AssertionError):
        doc_fns.page_subset(reader, [len(reader.pages) + 1]) # excessive pages