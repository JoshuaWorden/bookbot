from stats import get_word_count
from stats import get_character_count

# Return a string of the text passed in from the filepath
def get_book_text(filepath):
    # Open the file, using f as the variable to access the opened version of the file
    with open(filepath) as f:
        # Read the file and return it as a string
        # .read() returns a string
        return f.read()
    

def main():
    text = get_book_text("books/frankenstein.txt")
    
    # Get and print how many words are found in the text file
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

    # Get and print the number of times each character occurs in the text
    character_count = get_character_count(text)
    print(character_count)

main()