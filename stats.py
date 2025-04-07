# Returns the number of words in the passed in text file
def get_word_count(text):
        # Add each unique word to a list
        list_of_words = text.split()
        return len(list_of_words)



# Returns the number of times each character is found in the text
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



# Sort the character_count list from largest to smallest
def sort_characters_by_count(character_count):
        sorted_character_count = []
        
        # Iterate through each key in the dictionary
        for key in character_count:
                # Check if the name of the key is a letter
                if key.isalpha() == True:
                    # Add a two key-value pair dictionary to the sorted list, one for the letter and the other for the count
                    sorted_character_count.append({"character": key, "count": character_count[key]})

        # Sort the list of dictionaries from highest to lowest using the value assigned in the "count" key of each dictionary
        sorted_character_count.sort(reverse=True, key=sort_dict_by_count)

        return sorted_character_count



# Tells the .sort() in sort_characters_by_count() what key to sort by in the dictionary
def sort_dict_by_count(dict):
        return dict["count"]

