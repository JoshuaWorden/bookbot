# Return a string of the text derived from the filepath
def get_book_text(filepath):
    # Open the file, using f as the variable to access the opened version of the file
    with open(filepath) as f:
        # Read the file and return it as a string
        # .read() returns a string
        return f.read()

def main():
    # Note to self: Only need relative path when referencing files within project directory
    print(get_book_text("books/frankenstein.txt"))
        

main()