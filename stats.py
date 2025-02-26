def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    char_dicti = {}
    char_list = []
    for char in book_text:
        char_lower = char.lower()
        char_list.append(char_lower)
    for item in set(char_list):
        char_dicti[item] = char_list.count(item)
    return char_dicti

def sorted_dict(dicti):
    def sort_on(dict):
        return list(dict.values())[0]
    list_dicti = []
    for key in dicti:
        each_dicti = {}
        each_dicti[key] = dicti[key]
        list_dicti.append(each_dicti)
    list_dicti.sort(reverse = True, key = sort_on)
    return list_dicti