from collections import defaultdict
import re
import random
import pickle


def file_words(file_pointer):
    """Generator for words in a file"""
    regex = re.compile('[^a-zA-Z.]')
    for line in file_pointer:
        for word in line.split():
            #word = regex.sub('', word.lower())
            if word:
                yield word


if __name__ == '__main__':
    filename = 'data/bible-kjv.raw.txt'
    tuple_length = 4

    word_map = defaultdict(lambda: set())

    with open(filename, 'r') as fp:
        word_list = []
        for word in file_words(fp):

            # Initialize list
            if len(word_list) < tuple_length:
                word_list.append(word)
                continue

            word_map[tuple(word_list)].add(word)
            word_list = word_list[1:] + [word]

    word_map = {key: val for key, val in word_map.items() if len(val) > 0}

    output_length = 100
    word_of_god = list(random.choice(list(word_map.keys())))

    while len(word_of_god) < output_length:
        this_tup = tuple(word_of_god[-tuple_length:])
        next_word = random.choice(list(word_map[this_tup]))
        word_of_god.append(next_word)

    print(' '.join(word_of_god))

    with open('bible_phrases.pkl', 'wb') as fp:
        pickle.dump(word_map, fp)
