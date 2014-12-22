# -*- coding: utf-8 -*-
# author:      Luisa Neves
# project:     Phonemic Analysis
# file:        word.py - class to return a Word object
# description: Given an English word, this file returns a
#              new Word object, which consists of the original
#              English word and the Arpabet transcription of 
#              the word.
import nltk

class Word:

    def __init__(self, word):
        self.word = word
        self.arpa = self.arpabet(word)
        self.ipa = self.ipa(self.arpa)

    def __str__(self):
        s = ''
        return "Word: " + self.word + " -> Arpabet: [" + s.join(self.arpa) + "]"

    def arpabet(self, word):
        """Returns the Arpabet transcription of a given word as an array of symbols."""
        arpabet = nltk.corpus.cmudict.dict()

        return arpabet[word][0]

    def ipa(self, arpa):
      """Returns the IPA transcription of a given word."""
      trans = []

      for symbol in arpa:
          if symbol[-1].isdigit(): symbol = symbol[:-1] # remove Arpabet stress indicator

          # VOWELS
          # monopthongs
          if symbol == 'AO':
              trans.append(u'ɔ')
          elif symbol == 'AA':
              trans.append(u'ɑ')
          elif symbol == 'IY':
              trans.append(u'i')
          elif symbol == 'UW':
              trans.append(u'u')
          elif symbol == 'EH':
              trans.append(u'ɛ')
          elif symbol == 'IH':
              trans.append(u'ɪ')
          elif symbol == 'UH':
              trans.append(u'ʊ')
          elif symbol == 'AH': # overlap with AX (?)
              trans.append(u'ʌ')
          elif symbol == 'AX':
              trans.append(u'ə')
          elif symbol == 'AE':
              trans.append(u'æ')

          # dipthongs
          elif symbol == 'EY':
              trans.append(u'eɪ')
          elif symbol == 'AY':
              trans.append(u'aɪ')
          elif symbol == 'OW':
              trans.append(u'oʊ')
          elif symbol == 'AW':
              trans.append(u'aʊ')
          elif symbol == 'OY':
              trans.append(u'ɔi')

          # R-colored vowels
          elif symbol == 'ER':
              trans.append(u'ɝ')
          elif symbol == 'AXR':
              trans.append(u'ɚ')
          elif symbol == 'EH': # and next symbol == 'R'
              trans.append(u'ɛr')
          elif symbol == 'UH': # and next symbol == 'R'
              trans.append(u'ʊr')
          elif symbol == 'AO': # and next symbol == 'R'
              trans.append(u'ɔr')
          elif symbol == 'AA': # and next symbol == 'R'
              trans.append(u'ɑr')
          elif symbol == 'IH': # and next symbol == 'R'
              trans.append(u'ɪr')
          elif symbol == 'IY': # and next symbol == 'R'
              trans.append(u'ɪr')
          elif symbol == 'AW': # and next symbol == 'R'
              trans.append(u'aʊr')

          # CONSONANTS
          # stops
          elif symbol == 'P':
              trans.append(u'p')
          elif symbol == 'B':
              trans.append(u'b')
          elif symbol == 'T':
              trans.append(u't')
          elif symbol == 'D':
              trans.append(u'd')
          elif symbol == 'K':
              trans.append(u'k')
          elif symbol == 'G':
              trans.append(u'g')

          # affricates
          elif symbol == 'CH':
              trans.append(u'tʃ')
          elif symbol == 'JH':
              trans.append(u'dʒ')

          # fricatives
          elif symbol == 'F':
              trans.append(u'f')
          elif symbol == 'V':
              trans.append(u'v')
          elif symbol == 'TH':
              trans.append(u'θ')
          elif symbol == 'DH':
              trans.append(u'ð')
          elif symbol == 'S':
              trans.append(u's')
          elif symbol == 'Z':
              trans.append(u'z')
          elif symbol == 'SH':
              trans.append(u'ʃ')
          elif symbol == 'ZH':
              trans.append(u'ʒ')
          elif symbol == 'HH':
              trans.append(u'h')

          # nasals
          elif symbol == 'M':
              trans.append(u'm')
          elif symbol == 'EM':
              # trans.append(u'm̩')
              trans.append(u'm')
          elif symbol == 'N':
              trans.append(u'n')
          elif symbol == 'EN':
              # trans.append(u'n̩')
              trans.append(u'n')
          elif symbol == 'NG':
              trans.append(u'ŋ')
          elif symbol == 'ENG':
              # trans.append(u'ŋ̍')
              trans.append(u'ŋ')


          # liquids
          elif symbol == 'L':
              trans.append(u'ɫ')
          elif symbol == 'EL':
              # trans.append(u'ɫ̩')
              trans.append(u'ɫ')
          elif symbol == 'R':
              trans.append(u'ɹ')
          elif symbol == 'DX':
              trans.append(u'ɾ')
          elif symbol == 'NX':
              # trans.append(u'ɾ̃')
              trans.append(u'ɾ')


          # semivowels
          elif symbol == 'Y':
              trans.append('j')
          elif symbol == 'W':
              trans.append('w')
          elif symbol == 'Q':
              trans.append('ʔ')
    
      # print "hello"
      # print trans
      transString = u''
      for t in trans:
        transString = (transString + t)
      print transString.encode('utf-8')
      # convert to unicode
      # ustr = u'';
      # for t in trans:
      #   ustr += t.decode('unicode-escape')
      return trans
