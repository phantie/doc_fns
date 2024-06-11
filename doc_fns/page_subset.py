from pypdf import PdfReader, PageObject
from typing import Iterator, Sequence


def page_subset(reader: PdfReader, subset: Sequence[int]) -> Iterator[PageObject]:
    """
    Generates a subset of pages from a PDF reader based on the provided page indices.
    
    Args:
    - reader (PdfReader): The PdfReader object containing the pages to extract from.
    - subset (Sequence[int]): A sequence of integers representing the page indices to include in the subset.

    Returns: Lazy sequence of pages for the specified page indices

    Raises:
    - AssertionError: If the maximum index in `subset` is greater than or equal to the number of pages in the PDF.

    Example:
    ```python
    from pypdf import PdfReader
    
    reader = PdfReader("example.pdf")
    subset = [0, 2, 4]  # Get pages 1, 3, and 5
    
    for page in page_subset(reader, subset):
        print(page.extract_text())  # Process each selected page
    ```

    The function iterates over the PDF pages and filters them to yield only those whose indices are specified in the `subset`.
    It ensures that all specified indices are valid by asserting that the highest index is within the range of available pages.
    This approach allows for efficient and lazy evaluation, as pages are yielded one by one as they are filtered.
    """

    assert max(subset) < len(reader.pages)

    return map(lambda page_number_page: page_number_page[1], 
        filter(lambda page_number_page: page_number_page[0] in subset,
        enumerate(reader.pages)))
