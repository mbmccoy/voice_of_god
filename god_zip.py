from collections import defaultdict
import gzip
import random

import textwrap


class Heresy(Exception):
    """You have defiled the word of God!"""
    pass


def bits(byte_string):
    """Generates a sequence of bits from a byte stream"""
    for byte in byte_string:
        for bit_num in range(8):
            # Extract bit from byte
            byte, bit = byte >> 1, byte % 2
            yield bit


def generate_ngram_dict(filename, tuple_length):
    """Generate a dict with ngrams as key following words as value

    :param filename:  Filename to read from.
    :param tuple_length: The length of the ngram keys
    :return:  Dict of the form {ngram: [next_words], ... }
    """

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

    return {key: tuple(val) for key, val in ngrams.items()}


class GodZip(object):
    """Turn unholy bits into holy words!"""

    hallelujah = "Sayeth the Lord:\n\n"
    amen = "\n\nAmen."

    def __init__(self, tuple_length=3, line_width=70, compress=True):
        self.compress = compress
        self.line_width = line_width
        self.tuple_length = tuple_length
        self.god_grams = generate_ngram_dict('data/bible-kjv.raw.txt', tuple_length)
        self.capital_tuples = [key for key, value in self.god_grams.items()
                               if key[0][0].isupper()]

    def praise(self, unholy_bytes):
        """Encode unholy bytes or unholy unicode into Holy text"""

        if not unholy_bytes:
            raise Heresy("Thou shalt not be silent in the face of the Lord!")

        if not isinstance(unholy_bytes, bytes):
            unholy_bytes = unholy_bytes.encode()

        if self.compress:
            unholy_bytes = gzip.compress(unholy_bytes)

        # Start with a capitalized tuple
        speech_of_god = list(random.choice(self.capital_tuples))

        for bit in bits(unholy_bytes):
            holy_tuple = tuple(speech_of_god[-self.tuple_length:])
            holy_words = self.god_grams[holy_tuple]

            # Make sure that we have some words to choose from
            while len(holy_words) <= 1:
                chosen_word = holy_words[0]
                speech_of_god.append(chosen_word)
                holy_tuple = tuple(speech_of_god[-self.tuple_length:])
                holy_words = self.god_grams[holy_tuple]

            # Select from even indices if bit == 0, odd if bit == 1
            chosen_word = random.choice(holy_words[bit::2])
            speech_of_god.append(chosen_word)

        holy_sentences = ' '.join(speech_of_god).split('. ')
        annotated_speech_of_god = '.\n\n'.join(
            [
                '\n'.join(textwrap.wrap("[{}] ".format(idx + 1) + holy_phrase, width=self.line_width))
                for idx, holy_phrase in enumerate(holy_sentences)
            ]
        )
        return self.hallelujah + annotated_speech_of_god + self.amen

    def reveal_from_words(self, holy_words):
        """Decode a list of holy words into unholy bytes."""
        try:
            holy_tuple = tuple(holy_words[:self.tuple_length])
        except:
            raise Heresy("You mock the word of God!")

        unholy_bytes = b''
        unholy_num = 0
        bit_counter = 0
        for holy_word in holy_words[self.tuple_length:]:
            try:
                holy_ngram_list = self.god_grams[holy_tuple]
            except:
                raise Heresy("Thou shalt not modify the word of God!")

            holy_tuple = tuple(holy_tuple[1:] + (holy_word,))

            if len(holy_ngram_list) <= 1:
                continue

            try:
                unholy_bit = holy_ngram_list.index(holy_word) % 2
            except:
                raise Heresy("Not one word of God shall be changed!")

            unholy_num |= unholy_bit << bit_counter
            bit_counter += 1
            if bit_counter % 8 == 0:
                unholy_bytes += bytes([unholy_num])
                unholy_num = 0
                bit_counter = 0

        if self.compress:
            unholy_bytes = gzip.decompress(unholy_bytes)

        return unholy_bytes

    def reveal(self, annotated_speech):
        """Decode holy speech into bytes"""

        split_annotated_speech = annotated_speech.split('\n\n')

        # Check for hallelujah and amen
        if split_annotated_speech[0] != self.hallelujah.strip() \
                or split_annotated_speech[-1] != self.amen.strip():
            raise Heresy("Your praise is insufficient!")

        # Remove hallelujah and amen
        try:
            holy_annotated_sentences = split_annotated_speech[1:-1]
        except:
            raise Heresy("The word of God will not be silenced!")

        # Remove line annotations
        try:
            holy_words = ' '.join([sentence.split('] ')[1]
                                   for sentence in holy_annotated_sentences]).split()
        except:
            raise Heresy("How dare you imitate the word of God!")

        return self.reveal_from_words(holy_words)


def hex_expand(byte_str):
    return ':'.join('{:02x}'.format(byte) for byte in byte_str)


if __name__ == '__main__':
    god = GodZip(compress=False)

    hello_world = "Hello world!"
    print("I praise unto God: %s\n\n" % hello_world)
    holy_hello_world = god.praise(hello_world)
    print(holy_hello_world)

    assert(hello_world == god.reveal(holy_hello_world).decode())
