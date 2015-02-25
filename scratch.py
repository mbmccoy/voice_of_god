from collections import defaultdict
import re


def file_words(file_pointer):
    """Generator for words in a file"""
    regex = re.compile('[^a-zA-Z]')
    for line in file_pointer:
        for word in line.split():
            word = regex.sub('', word)
            if word:
                yield word.lower()

if __name__ == '__main__':
    filename = 'data/bible-kjv.raw.txt'
    tuple_length = 2

    word_map = defaultdict(lambda: [])

    with open(filename, 'r') as fp:
        word_list = []
        for word in file_words(fp):

            # Initialize list
            if len(word_list) < tuple_length:
                word_list.append(word)
                continue

            word_map[tuple(word_list)].append(word)
            word_list = word_list[1:] + [word]



    tuple_counts = [len(val) for key, val in ]
