''' 

Q1. Write a program that takes a string as input, and counts the frequency of each word in the string, there might
be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word

Test Cases:


Test Case 1:

Example input - string = “Programming is fun programming is fun creative”
Example output - 11
Explanation: "Programming" appears 2 times, "fun" and ”is” also appears three times in the list. However, "Programming" has 11 letters, so it is returned as the result.


Test Case 2:

Example input - string = “Hello everyone Nice to meet you all”
Example output - 8
Explanation:  In this string, every word appears only one time. However, "everyone" has more letters, so it's length returned as the result.

'''
 


#importing library

from collections import Counter


#defining function to count frequency

def frequency(word_list):


#frequency of words
    word_counter = Counter(word_list)

#most frequent words
    frequent_word = max(word_counter.values())

    frequent_word = [word for word, count in word_counter.items() if count == frequent_word]

#if frequency of two words are same counting longest word among them

    longest_word = max(frequent_word, key=len)

    # returning lenghth of word with highest frequency and longest length.

    return len(longest_word)
   



#take input as string

string = input("Provide your string : ")


#converting string into list of words

word_list =string.split(sep=" ")

#calling function

word =frequency(word_list)

#printing result

print(word)

