from pypdf import PdfWriter, PageObject
from typing import Iterable


def writer_from_page_iterable(pages: Iterable[PageObject]) -> PdfWriter:
    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    return writer
