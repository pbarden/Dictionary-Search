"""
autocorrect.py
@Paul Barden

Spelling error correction module
"""
def autocorrect(bad_word, dict_obj):
    """
    Parameters
    -----------
    bad_word : str
        The word that is misspelled
    dict_obj : dictionary
        The dictionary to search and compare other words

    Returns
    -----------
    Suggested words as a list
    """
    sug_words = []
    for k in dict_obj.keys():
        if bad_word in k : sug_words.append(k)
        elif bad_word[:-1] in k : sug_words.append(k)
        elif bad_word[1:] in k : sug_words.append(k)
        elif len(bad_word) > 5 and bad_word[:-2] in k : sug_words.append(k)
        elif len(bad_word) > 5 and bad_word[1:-1] in k : sug_words.append(k)
        elif len(bad_word) > 5 and bad_word[2:] in k : sug_words.append(k)
        elif len(bad_word) > 8 and bad_word[:-4] in k : sug_words.append(k)
        elif len(bad_word) > 8 and bad_word[3:-3] in k : sug_words.append(k)
        elif len(bad_word) > 8 and bad_word[4:] in k : sug_words.append(k)

    return sug_words