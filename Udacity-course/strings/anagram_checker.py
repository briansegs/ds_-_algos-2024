def anagram_checker(str1, str2):

    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # First solution
    # st1 = []
    # st2 = []
    # for l in str1:
    #     if l != " ":
    #         st1.append(l.lower())
    # for l in str2:
    #     if l != " ":
    #         st2.append(l.lower())
    # st1.sort()
    # st2.sort()
    # s1a = "".join(st1)
    # s2b = "".join(st2)

    # return s1a == s2b

    #Second solution
    if len(str1) != len(str2):
        # Clean the strings
        cln_str1 = str1.replace(" ", "").lower()
        cln_str2 = str2.replace(" ", "").lower()

        return sorted(cln_str1) == sorted(cln_str2)


# Test Cases

print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")
