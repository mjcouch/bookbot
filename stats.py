
# Get a count of words in a text string
def word_count(book_text):

    words = book_text.split()
    return len(words)

# Get a dictionary of characters contained in a string
def char_counts(book_text):

    lc_book_text = book_text.lower()
    char_dict = {}
    for i in range(0, len(lc_book_text)):
        if lc_book_text[i] in char_dict:
            char_dict[lc_book_text[i]] += 1
        else:
            char_dict[lc_book_text[i]] = 1

    return char_dict

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]

# Get a sorted list of dicionary entries from a dictionary
def sort_dict_list(my_dictionary):
    my_sorted_list = []
    my_sorted_list = [{"char": key, "num": value} for key, value in my_dictionary.items()]
    my_sorted_list.sort(reverse=True, key=sort_on)
    return(my_sorted_list)
    