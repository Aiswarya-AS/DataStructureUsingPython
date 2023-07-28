# create dict from two lists
keys = [1, 2, 3, 4, 5, 6]
values = ["one", "two", "three", "four", "five", "six"]

# list of tupes to dict
list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
# dictionary = dict(list_of_tuples)
dictionary = {key: value for key, value in list_of_tuples}
# swap keys and values in dictonary
dict1 = {1: "one", 2: "two", 3: "three"}
dict1 = {value: key for key, value in dict1.items()}
dict2 = {num: num**2 for num in range(1, 11)}
