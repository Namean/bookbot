# main.py
# The program's entry point and file-reading logic

import sys
from pathlib import Path
from stats import get_num_words


def get_book_text(path_to_file) -> str:
    try:
        with open(path_to_file, mode="r", encoding="utf-8") as fp:
            file_contents = fp.read()
            return file_contents
    except FileNotFoundError:
        print(f"file not found: {path_to_file}")
        user_response = input(
            f"Would you like to create file {path_to_file} [Y/n]?: "
        ).lower()
        if user_response == "y":
            path_to_file.touch()
            get_book_text(path_to_file)
        else:
            sys.exit(f"Error: file not found '{path_to_file}'")

def main():
    book_path = Path("books/frankenstein.txt")
    book_text = get_book_text(book_path)
    get_num_words(book_text)


if __name__ == "__main__":
    main()
