from stats import count_words

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

def main():
    path = './books/frankenstein.txt'
    contents = get_book_text(path)
    # print(contents)
    word_count = count_words(contents)
    print('%d words found in the document' % word_count)

if __name__ == "__main__":
    main()
