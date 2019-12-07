def read_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text


if __name__ == '__main__':
    text = read_file('literki.txt')
    print(text)
