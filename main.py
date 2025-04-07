from stats import (get_word_count, 
                   get_character_count, 
                   sort_characters_by_count)

import sys

def main():
    # Check to see if the user has correctly used the CLI to import a book/text file
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)

    text = get_book_text(sys.argv[1])
    
    # Get and print how many words are found in the text file
    word_count = get_word_count(text)

    # Get and print the number of times each character occurs in the text
    character_count = get_character_count(text)
    #print(character_count)

    # Get and print the sorted character count that only includes letters
    sorted_character_count = sort_characters_by_count(character_count)
    print_character_count_report(sorted_character_count, word_count)



# Return a string of the text passed in from the filepath
def get_book_text(filepath):
    # Open the file, using f as the variable to access the opened version of the file
    with open(filepath) as f:
        # Read the file and return it as a string
        # .read() returns a string
        return f.read()



def print_character_count_report(character_count, word_count):
    # Print the program title and the book it's analysing
    print("============ BOOKBOT ============\n" 
    f"Analyzing book found at {sys.argv[1]}...")
    
    # Print the word count of the book
    print("----------- Word Count ----------\n" 
    f"Found {word_count} total words")

    # Print the character count of each letter
    print("--------- Character Count -------")
    for dict in character_count:       
            print(f"{dict["character"]}: {dict["count"]}\n")
    
    # Print the footer
    print("============= END ===============")



main()