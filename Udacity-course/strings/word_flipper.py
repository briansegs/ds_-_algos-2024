# Code

def word_flipper(our_string):

    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # Other solution
    word_list = our_string.split(" ")

    for idx, word in enumerate(word_list):
        word_list[idx] = word[::-1]

    return " ".join(word_list)

    # First solution
    # new_str = ""
    # for word in our_string.split():
    #     new_str += "".join(reversed(word)) + " "

    # return new_str[:-1]

# Test Cases

print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")
