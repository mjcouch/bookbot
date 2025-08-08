

def get_book_text(file_path):

    with open(file_path) as f:
        
        file_contents = f.read()
    
    return file_contents

def main():

    # Import sys module
    import sys

    # Import word_count function into main
    from stats import word_count, char_counts, sort_dict_list

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Read file contents
    book_text = get_book_text(book_path)
    
    #Get a count of the number of words in the book
    num_words = word_count(book_text)

    char_list = {}
    char_list = char_counts(book_text)

    new_sorted_list = sort_dict_list(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in range(0, len(new_sorted_list)):
        if new_sorted_list[i]["char"].isalpha():
            print(f"{new_sorted_list[i]["char"]}: {new_sorted_list[i]["num"]}")
    

# call the main function
main()