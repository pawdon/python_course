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
    # print(letters_hist)
    # Zalozmy, ze histogram ma byc w kolejnosci 0,1,2,...,9,a,b,c,...,z
    ordered_letters = get_ordered_letters()
    # print(ordered_letters)
    counts = [str(letters_hist.get(key, 0)) for key in ordered_letters]
    # print(counts)

    with open('hist.txt', 'w') as file:
        file.write(';'.join(counts))

    return letters_hist


def letters_replace(text):
    letters_hist = histogram(text)
    print(letters_hist)
    count_list = [{'letter': key, 'count': val} for key, val in letters_hist.items()]
    print(count_list)
    count_list.sort(key=lambda x: x['count'], reverse=True)
    print(count_list)

    letter1 = count_list[0]['letter']
    letter2 = count_list[1]['letter']
    print(letter1, letter2)

    text_as_list = list(text)
    for i in range(len(text_as_list)):
        if text_as_list[i] == letter1:
            text_as_list[i] = letter2
        elif text_as_list[i] == letter2:
            text_as_list[i] = letter1

    text = ''.join(text_as_list)
    print(text)

    with open('zamiana.txt', 'w') as file:
        file.write(text)


if __name__ == '__main__':
    text = read_file('literki.txt')
    print(text)
    letters_replace(text)
