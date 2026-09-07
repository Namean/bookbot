from pathlib import Path

def get_book_text(path_to_file) -> str:
    with open(path_to_file, mode='r', encoding='utf-8') as fp:
        file_contents = fp.read()
        return file_contents

def main():
    book_path = Path("books/frankenstein.txt")
    print( get_book_text(book_path) )

if __name__ == '__main__':
    main()
