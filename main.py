def get_word_count(book):
    print(len(book.split()), "words found in the document")

def get_character_count(book):
    lowered_string = book.lower()
    letters = {}
    for character in lowered_string:
        if character in letters:
            letters[character] += 1
        else:
            letters[character] = 1
    sorted1 = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    for letter, count in sorted1.items():
        if letter.isalpha() == True:
            print(f"The {letter} character was found {count} times")
    return sorted1

def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        get_word_count(file_contents)
        get_character_count(file_contents)
        print("--- End report ---")
            

main()