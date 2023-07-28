'''
Generate a list of even numbers from 1 to 20.
Create a list of squares of numbers from 1 to 10.
Filter out vowels from a given string.
Generate a list of numbers divisible by both 3 and 5 from 1 to 100.
Create a list of strings that start with a vowel from a given list of words.
Convert a list of strings to uppercase.
Remove duplicate elements from a list.
Generate a list of all possible pairs from two separate lists.
Filter out prime numbers from a given list of integers.
Create a list of words that have more than five characters from a given sentence.
'''

import itertools

# 1. even upto 20
even_1_to_20 = [x for x in range(1, 21) if x % 2 == 0]
# square up to 10
squares_1_to_10 = [x * x for x in range(1, 11)]


# 2.filter out vowels from given string
def filter_vowels(string1):
    vowels = "aeiouAEIOU"
    result = ""

    for i in string1:
        if i not in vowels:
            result += i
    return result


string1 = "Aiswarya"
filter_vowels(string1)


# 2 a)filter out vowels using list comprehesion
def vowels_filter(string1):
    vowels = "aeiouAEIOU"
    return " ".join([i for i in string1 if i not in vowels])


string2 = "aiswarya"


# 3.list of numbers that is divisible by both 3 and 5
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

# 4.convert list of string to uppercase
string1 = ["helo", "aiswrya", "how", "are ", "you"]
upper_case = [x.upper() for x in string1]

#  5.remove duplicates from list
#  using set
original_list = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5]
unique_list = list(set(original_list))

# using list comprehension
unique_list1 = [x for i, x in enumerate(original_list) if x not in original_list[:i]]

# generate all possible pairs from 2 lists
# using nested loops
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
pairs = []
for i in list1:
    for j in list2:
        pairs.append((i, j))

# using itertools
pairs = list(itertools.product(list1, list2))


# prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = [x for x in nums if is_prime(x)]

# Create a list of words that have more than five characters from a given sentence.
sentance = (
    "Create a list of words that have more than five characters from a given sentence"
)
list1 = [x for x in sentance.split(" ") if len(x) > 5]
