import sys
from typing import Dict
from stats import count_words, get_letter_counts, get_formatted_letter_counts

def get_book_text(path: str) -> str:
    try:
        # print('Reading the file under %s path...' % path)
        with open(path) as book:
            file_contents = book.read()
        return file_contents

    except Exception as e:
        print('There has been an error reading the file...')
        print('Please investigate further..{}' % e)

    return ""

def format_dict_to_output(dict: Dict, word_count: int, path: str) -> str:
    print("============ BOOKBOT ============")
    print("Analyzing book found at %s..." % path)
    print("----------- Word Count ----------")
    print("Found %d total words" % word_count)
    print("--------- Character Count -------")
    for key, value in dict.items():
        print("%c: %d" % (key,value))
    print("============= END ===============")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        contents = get_book_text(path)    
        word_count = count_words(contents)    
        letter_counts = get_letter_counts(contents)    
        formatted_letter_counts = get_formatted_letter_counts(letter_counts)    
        format_dict_to_output(formatted_letter_counts, word_count, path)
    
if __name__ == "__main__":
    main()
