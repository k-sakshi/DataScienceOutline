'''
Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
he can remove just one character at the index in the string, and the remaining characters will occur the same
number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .


Test Cases

Test Case 1:

Input string: "aaabbbcc"
expected Output: YES
Explanation: By removing one 'a' or one 'b', all remaining characters (a, b, and c) will have the same frequency (3).

Test Case 2:

Input string"aabbccdde"
Output: NO
Explanation: Removing any single character will not make all remaining characters have the same frequency.

'''

from collections import Counter


def validity(s):
    
    char =Counter(s)
    char_values = Counter(char.values())
   
    # If there is only one unique frequency, the string is already valid
    if len(char_values) == 1:
        return "YES"

    # If there are more than two unique frequencies, the string cannot be made valid
    
    if len(char_values) > 2:
        return "NO"

    min_freq, min_freq_count = char_values.most_common()[-1]
    max_freq, max_freq_count = char_values.most_common()[0]

    if min_freq_count == 1 and min_freq == 1:
        # Removing the character with frequency 1 will result in a valid string
        return "YES"
    if max_freq_count == 1 and max_freq - min_freq == 1:
        # Removing one character from the group with higher frequency will result in a valid string
        return "YES"

    return "NO"


string = input("Enter string : ")

print(validity(string))


