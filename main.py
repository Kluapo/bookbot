char_list=[]
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    number_of_characters = get_number_characters(text)
    
    filter(number_of_characters)
    
    char_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{numwords} words found in the document\n")
    for char_dict in char_list:
        print (f'The \'{char_dict["char"]}\' character was found {char_dict["num"]} times')
    print ("--- End report ---")

def get_num_words(text):
    words = text.split()
    return (len(words))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_characters(text):
    lowered_text = text.lower()
    character_list = list(lowered_text)
    number_character = {}
    for character in character_list:
        number_character[character] = number_character.get(character, 0) + 1
    return number_character

def filter(dictionary):
    for char in dictionary:
        if char.isalpha():
            char_dict = {"char": char, "num":dictionary[char]}
            char_list.append(char_dict)

def sort_on(dict):
    return dict["num"]

main()
