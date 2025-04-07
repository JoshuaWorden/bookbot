# Returns the number of words in the passed in text file
def get_word_count(text):
        # Add each unique word to a list
        list_of_words = text.split()
        return len(list_of_words)

def get_character_count(text):
        # Convert all uppercase characters to lowercase as they are counted as the same
        text = text.lower()

        # Dictionary to store all of the characters found and their number of occurrences
        character_count = {}

        for i in range(len(text)):
                # If the character is in the dictionary, increment its count by 1
                if text[i] in character_count:
                        character_count[text[i]] += 1
                # If it's not in the dictionary, add it to the dictionary and give it a starting value of 1
                else:
                        character_count[text[i]] = 1

        return character_count
                        