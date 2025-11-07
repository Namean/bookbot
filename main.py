#!/usr/bin/env python3

# - [Fzf selection in Python](https://chatgpt.com/c/690d71bc-ee88-8330-bad5-f8b32305484d)

import sys
from pathlib import Path
from stats import get_num_words, get_char_count, sort_dict
import subprocess
import tempfile

def select_file():
    with tempfile.NamedTemporaryFile() as tmp:
        # Let fzf write its selection into a temporary file
        fzf_prompt = "--prompt='(ง ◉ _ ◉)ง: '"
        find_method = "find . -type f | fzf > {}"
        ls_method = f"ls ./books | fzf {fzf_prompt} > {{}}"
        subprocess.run(ls_method.format(tmp.name), shell=True)
        tmp.seek(0)
        selection = tmp.read().decode().strip()
        return selection or None


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()  # (str)

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    try:
        file_path = Path(sys.argv[1]) or ""
        full_text = get_book_text(file_path)
        word_count = get_num_words(full_text)

        word_count = get_num_words(full_text)
        char_count = get_char_count(full_text)

        start_banner = "============ BOOKBOT ============"
        end_banner = "============= END ==============="
        word_banner = "----------- Word Count ----------"
        character_banner = "--------- Character Count -------"

        user_banner = f"Analyzing book found at books/{file_path}..."


        def header():
            print(start_banner)
            print(user_banner)
            print(word_banner)
            print(f"Found {word_count} total words")

        def footer():
            print(character_banner)
            sort_dict(char_count)
            print(end_banner)

        header()
        footer()


    except Exception as e:
        print(e)


if __name__ == "__main__":
    import subprocess
    subprocess.run("clear", shell=True)

    main()

