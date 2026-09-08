# stats.py
# Functions that analyze the text

def get_num_words(book_text: str = None) -> int:
    num_words = 0

    if book_text is None:
        return num_words 

    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

    return len(book_text.split())

