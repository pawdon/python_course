def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


def get_ordered_letters():
    digits = list(range(ord('0'), ord('9') + 1))
    letters = list(range(ord('a'), ord('z') + 1))

    chars = [chr(x) for x in digits + letters]
    return chars


def histogram(text: str):
    letters_hist = dict()
    text = text.lower()
    for letter in text:
        # if letter != ' ':
        # ord(x) zamienia znak (np. litere) na kod ASCII
        # chr(x) zamienia kod ASCII na znak (np. litere)
        if (ord('a') <= ord(letter) <= ord('z')) or (ord('0') <= ord(letter) <= ord('9')):
            """
            if letter in letters_hist:  # <==> if letter in letters_hist.keys()
                letters_hist[letter] += 1
            else:
                letters_hist[letter] = 1
            """
            letters_hist[letter] = letters_hist.get(letter, 0) + 1
    print(letters_hist)
    # Zalozmy, ze histogram ma byc w kolejnosci 0,1,2,...,9,a,b,c,...,z
    ordered_letters = get_ordered_letters()
    print(ordered_letters)
    counts = [str(letters_hist.get(key, 0)) for key in ordered_letters]
    print(counts)

    with open('hist.txt', 'w') as file:
        file.write(';'.join(counts))


if __name__ == '__main__':
    text = read_file('literki.txt')
    print(text)
    histogram(text)
