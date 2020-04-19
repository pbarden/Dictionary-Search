"""
main.py
@Paul Barden

Main module
"""
from monograph import Word, LanguageDictionary
from autocorrect import autocorrect

print("Dictionary Search\nan app by Paul Barden")

# Create a new dictionary to search
my_dict = LanguageDictionary("dictionary.json")

keep_going = True

while keep_going:
    # Grab a word from the user
    user_input = input("\nPlease enter a word: (enter '\\q' to quit)\n")

    if user_input == "\\q":
        quit()
    else:
        my_word = Word(user_input)

        # Store the definition of the word
        my_word.means(my_dict.query(my_word.show()))    

        # Return a definition
        if my_word.define():
            print("\nWord data for: {}\n\nDefinition(s) found:\n---------------------".format(my_word.show().title()))
            print(my_word.define())
        else:
            print("\nWord data for: {}\n\nNo definition found.".format(my_word.show().title()))

            # Check for spelling mistakes and provide suggestions
            suggest_word_list = autocorrect(my_word.show(), my_dict.dump())
            suggest_word_list.sort()
            if suggest_word_list:
                print("\nHere are some related terms:\n")
                for sw in suggest_word_list:
                    print ("  - {}".format(sw.title()))