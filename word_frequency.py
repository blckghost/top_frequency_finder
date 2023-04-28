"""
This program returns the top 20 most common words in a user provided text input -
The program is written to return a frequency count of the top 20 words in a book

This program utilizes concepts such MAP ADT (dict in python) to create a key - value pair between a word and its
frequency

"""


def replace_contraction(word: str, c_dict: dict) -> str:
    """
    replace a contraction and returns its full version
    s.replace_contraction('can't) >> cannot

    """
    try:
        return c_dict[word]
    except KeyError:
        return word


if __name__ == "__main__":

    book_name = str(
        input("Welcome to frequency counter - Please enter the name of your textfile without its extension: "))
    book_name += ".txt"

    contraction_file = input("Please provide a name for your textfile of contractions - without its extension: ")
    contraction_file += ".txt"
    con = open(contraction_file, 'r')

    cont_map = dict()
    for line in con:  # now we have every contraction in our dict as a key: contraction, value: extended version
        cont_map[line.replace('\n', '').split(',')[0]] = line.replace('\n', '').split(',')[1]

    book_contents = []
    book = open(book_name, 'r')
    for line in book:
        book_contents.append(replace_contraction(line.replace('\n', ''), cont_map))

    freq_map = {}
    for words in book_contents:
        if len(freq_map) != 0:
            count = freq_map.get(words)
            if count is None:
                freq_map[words] = 0
            else:
                freq_map[words] = count + 1
        else:
            freq_map[words] = 0
    print(freq_map)


