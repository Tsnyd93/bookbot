def main():
    import sys
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    from stats import sorted
    from stats import get_num_words
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    from stats import lower_case
    low_count=lower_case(text)
    from stats import sorted
    sorted_dict=sorted(low_count)
    for char in sorted_dict:
        char_string= char["char"]
        if char_string.isalpha():
            print(f"{char_string}: {char['num']}")
        
            

        
    
    

def get_book_text(path):
    with open(path) as f:
        return f.read()






main()
