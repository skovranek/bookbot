file_pathname = './books/frankenstein.txt'


with open(file_pathname) as f:
    file_contents = f.read()


def count_words(str):
    words = str.split()
    num = len(words)
    return num


def count_letters(str):
    lowercase_str = str.lower()
    result = {}

    for s in lowercase_str:
        if s in result:
            result[s] += 1
        else:
            result[s] = 1

    return result


def print_report():
    letters_str = 'abcdefghijklmnopqrstuvwxyz'
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)

    print('---------')
    print(f'Printing report for document: {file_pathname[1:]}')
    print('---------\n')
    print(f'Word Count: {word_count}\n')

    for letter in letters_str:
        if letter in letter_count:
            print(f'"{letter}" - occurances: {letter_count[letter]}')

    print('\nEnd')


print_report()
