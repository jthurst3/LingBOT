# -*- coding: utf-8 -*-
# author:      Luisa Neves
# project:     Phonemic Analysis
# file:        scanner.py - module to scan the input
# description: Parses an input file to determine and
#              separate the two target phonemes and
#              the list of words. Also calls the analysis
#              functions.
from word import Word
from analysis import analyze

def run(phonemes, words):
    """Driver to call parsing and comparing functions."""
    phoneme1, phoneme2 = parse_phoneme(phonemes)

    # print(phoneme1)
    # print(phoneme2)
    # print(words)
    # print('Target phonemes: [' + phoneme1 + '], [' + phoneme2 + ']')
    # print('Data set: ')
    # print(words)
    # for each word in words, return word-trans pair
    # wt_pairs = [Word(w) for w in words]
    # for w in wt_pairs: print(w)

    transcribed_words = [Word(w) for w in words]
    analyze(phoneme1, phoneme2, transcribed_words)

def parse_phoneme(line):
    """Parses first line of the file into the two target phonemes."""
    phonemes = line.partition(' ')
    phoneme1 = phonemes[0]
    phoneme2 = phonemes[2]
    return(phoneme1, phoneme2)
