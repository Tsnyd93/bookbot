def main():
    import sys
    from stats import sorted
    from stats import get_num_words
    from stats import lower_case
    from stats import sorted
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    lower_case_count=lower_case(text)
    sorted_dict=sorted(lower_case_count)
    for char in sorted_dict:
        char_string= char["char"]
        if char_string.isalpha():
            print(f"{char_string}: {char['num']}")
        
            
def get_book_text(path):
    with open(path) as f:
        return f.read()






main()
