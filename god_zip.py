from collections import defaultdict
import gzip
import random

import textwrap


class Heresy(Exception):
    """You have defiled the word of God!"""
    pass


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
    return {key: list(val) for key, val in ngrams.items()}


class GodZip(object):

    hallelujah = "Sayeth the Lord:\n\n"
    amen = "\n\nAmen."

    def __init__(self, tuple_length=3, line_width=70):
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

                # Encode using method zero
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

    def decode_words(self, holy_words):
        """Decode a list of holy words into unholy bytes."""

        try:
            holy_tuple = tuple(holy_words[:self.tuple_length])
        except:
            raise Heresy("You mock the word of God!")

        unholy_bytes = b''
        unholy_num = 0
        bit_counter = 0
        for holy_word in holy_words[self.tuple_length:]:

            bit_counter += 1
            if bit_counter % 8 == 0:
                unholy_bytes += bytes([unholy_num])
                unholy_num = 0
            try:
                holy_ngram_list = self.god_grams[holy_tuple]
            except:
                raise Heresy("Thou shalt not modify the word of God!")

            try:
                unholy_bit = holy_ngram_list.index(holy_word) % 2
            except:
                raise Heresy("Not one word of God shall be changed!")

            print(bit_counter % 8, unholy_num, unholy_bit)
            unholy_num += (unholy_num << 1) + unholy_bit
            holy_tuple = tuple(holy_tuple[1:] + (holy_word,))

        print(unholy_bytes.decode())

    def decode(self, annotated_speech):
        """Decode holy speech into bytes"""

        split_annotated_speech = annotated_speech.split('\n\n')

        # Remove hallelujah and amen
        if split_annotated_speech[0] not in self.hallelujah \
                or split_annotated_speech[-1] not in self.amen:
            raise Heresy("Your praise is insufficient!")

        try:
            holy_annotated_sentences = split_annotated_speech[1:-1]
        except:
            raise Heresy("The word of God will not be silenced!")

        try:
            holy_words = ' '.join([sentence.split('] ')[1]
                                   for sentence in holy_annotated_sentences]).split()
        except:
            raise Heresy("How dare you imitate the word of God!")

        return self.decode_words(holy_words)

if __name__ == '__main__':
    x = GodZip()
    holy_hello_world = x.encode('Hello world!')
    print(holy_hello_world)
    x.decode(holy_hello_world)


