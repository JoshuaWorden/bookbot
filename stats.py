# Returns the number of words in the passed in text file
def get_word_count(filepath):
    # Open the file
    with open(filepath) as f:
        # Read the file, and append each word to list_of_words
        list_of_words = f.read().split()

    return len(list_of_words)
