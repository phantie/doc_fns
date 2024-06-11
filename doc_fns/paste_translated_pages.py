from .writer_from_page_iterable import writer_from_page_iterable

from pypdf import PdfReader, PdfWriter
from typing import Sequence




def paste_translated_pages(original: PdfReader, translated_pages: PdfReader, translated_page_numbers: Sequence[int]) -> PdfWriter:
    """
    Combines pages from an original PDF and a translated PDF to create a new PDF.
    
    This function replaces specific pages in the original PDF with corresponding pages from a translated PDF.
    It ensures that the translated pages are inserted at the specified indices, effectively pasting them into the original PDF.

    Args:
    - original (PdfReader): The PdfReader object for the original PDF.
    - translated_pages (PdfReader): The PdfReader object containing translated pages to be inserted.
    - translated_page_numbers (Sequence[int]): A sequence of integers indicating the indices in the original PDF
      where the translated pages should replace the original pages.

    Returns:
    - PdfWriter: A PdfWriter object containing the combined PDF with the translated pages inserted at the specified indices.

    Raises:
    - AssertionError: If the number of translated pages does not match the length of `translated_page_numbers`.
    - AssertionError: If any page number in `translated_page_numbers` exceeds the number of pages in the translated PDF.
    - AssertionError: If there are duplicate entries in `translated_page_numbers`.

    Example:
    ```python
    from pypdf import PdfReader, PdfWriter

    original_pdf_path = "original.pdf"
    translated_pdf_path = "translated.pdf"
    output_pdf_path = "combined.pdf"

    original_reader = PdfReader(original_pdf_path)
    translated_reader = PdfReader(translated_pdf_path)

    # Replace pages 2 and 4 in the original PDF with the first two pages of the translated PDF
    translated_page_numbers = [1, 3]  # Replace pages 2 and 4 in 0-based index

    writer = paste_translated_pages(original_reader, translated_reader, translated_page_numbers)

    # Save the combined PDF
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Combined PDF saved to {output_pdf_path}")
    ```
    
    The function validates that the number of translated pages matches the number of specified indices and that there are no duplicate indices.
    It iterates over the pages of the original PDF, replacing the pages at the specified indices with the corresponding translated pages.
    The resulting `PdfWriter` object contains the new combined PDF, which can be saved to a file.
    """

    assert len(translated_pages.pages) == len(translated_page_numbers)
    assert all(n < len(translated_pages.pages) for n in translated_page_numbers)
    assert len(set(translated_page_numbers)) == len(translated_page_numbers)

    translated_pages = iter(translated_pages.pages)

    return writer_from_page_iterable(
        next(translated_pages) if page_number in translated_page_numbers
        else original.pages[page_number]
        for page_number in range(len(original.pages)))

