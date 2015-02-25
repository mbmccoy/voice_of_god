from collections import defaultdict
import gzip
import random

import textwrap

def generate_ngrams(filename, tuple_length):

    def file_words(file_pointer):
        """Generator for words in a file"""
        for line in file_pointer:
            for word in line.split():
                yield word

    ngrams = defaultdict(lambda: set())

    with open(filename, 'r') as fp:
        word_list = []
        for word in file_words(fp):
            if len(word_list) < tuple_length:
                word_list.append(word)
                continue
            ngrams[tuple(word_list)].add(word)
            word_list = word_list[1:] + [word]
    return ngrams


class GodZip(object):

    hallelujah = "Sayeth the Lord:\n\n"
    amen = "\n\n\nAmen.\n"

    def __init__(self, tuple_length=3, line_width=50):
        self.line_width = line_width
        self.tuple_length = tuple_length
        self.god_grams = generate_ngrams('data/bible-kjv.raw.txt', tuple_length)
        self.capital_tuples = [key for key, value in self.god_grams.items()
                               if key[0][0].isupper()]

    def encode(self, string_or_bytes):
        """Encode unicode string or bytes into into Holy speech"""

        if not isinstance(string_or_bytes, bytes):
            data = string_or_bytes.encode()
        else:
            data = string_or_bytes
        gz_data = gzip.compress(data, 9)

        speech_of_god = list(random.choice(self.capital_tuples))
        for byte in gz_data:
            while byte != 0:
                holy_tuple = tuple(speech_of_god[-self.tuple_length:])
                holy_words = self.god_grams[holy_tuple]
                if len(holy_words) < 2:  # Make sure that we have some words to choose
                    speech_of_god.append(list(holy_words)[0])
                    continue

                bit, byte = byte % 2, byte >> 1

                if bit:
                    chosen_word = random.choice(list(holy_words)[::2])
                else:
                    chosen_word = random.choice(list(holy_words)[1::2])
                speech_of_god.append(chosen_word)

        holy_sentences = ' '.join(speech_of_god).split('. ')
        annotated_speech_of_god = '.\n\n'.join(
            [
                '\n'.join(textwrap.wrap("[{}] ".format(idx) + holy_phrase, width=self.line_width))
                for idx, holy_phrase in enumerate(holy_sentences)
            ]
        )

        return self.hallelujah + annotated_speech_of_god + self.amen

    def decode(self):
        pass


if __name__ == '__main__':
    x = GodZip()
    print(x.encode('Hello world!'))
