"""
The second milestone is to create a function called filter_strings which takes as input a list of strings, and a string to filter for, and then returns a list of all strings that contain the substring.

Example
filter_strings(['I want to learn', 'I like learning', "I'm horny"], "learn")
['I want to learn', 'I like learning']
"""


def filter_strings(list_of_strings, string_to_filter_for):
    # Store the final strings into this list
    final = []

    # Loop through the list of strings
    for i in list_of_strings:
        # Check if the substring is present in the current string
        if string_to_filter_for in i:
            # If present, add the string to the final list
            final.append(i)
        #if there is no substring in list
        else:
            return "There is no substring in the list"
    return final


list_of_strings = ['I want to learn', 'I like learning', 'I love to learn']
string_to_filter_for = "learn"
print(filter_strings(list_of_strings, string_to_filter_for))






