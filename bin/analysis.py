# -*- coding: utf-8 -*-
# author:      Luisa Neves
# project:     Phonemic Analysis
# file:        analysis.py - module to analyzed the parsed
#              input
# description: Analyzes a body of data and the two target 
#              phonemes in order to describe the distribution
#              and features of the two phonemes with respect
#              to the data set.
import math

def analyze(phoneme1, phoneme2, words):
    """Driver to call various analytical functions on the data set."""
    env1 = []
    env2 = []
    majority = math.ceil(len(words)/2)

    # convert phonemes to unicode
    phoneme1 = unicode(phoneme1, 'utf-8')
    phoneme2 = unicode(phoneme2, 'utf-8')

    for word in words:
        # convert word to unicode
        # ip = unicode(word.ipa, 'utf-8')
        e1 = environment(phoneme1, word.ipa)
        e2 = environment(phoneme2, word.ipa)
        for pair in e1:
            if pair is not None: env1.append(pair)
        for pair in e2:
            if pair is not None: env2.append(pair)

    # print("Environments...")
    # print('\nEnvironment of [' + phoneme1 + ']:')
    # print(env1)
    print(prettyEnvironment(env1).encode('utf-8'))

    # print('\nEnvironment of [' + phoneme2 + ']:')
    # print(env2)
    print(prettyEnvironment(env2).encode('utf-8'))

    if overlap(env1, env2, 1):
        if meaning():
            # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in free variation.')
            print('Overlap on left and right, but meanings are the same.')
            print('free variation')
            print('')
        else:
            # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in contrastive distribution.')
            # print('The two phonemes are allophones of different phonemes.')
            print('Overlap on left and right.')
            print('contrastive distribution')
            print('allophones of separate phonemes')
    else:
        # print('[' + phoneme1 + '] and [' + phoneme2 + '] are in complementary distribution.')
        # print('The two phonemes are allophones of the same phoneme.')
        if oneSidedOverlap(env1, env2, 1):
            print('Overlap on one side but not the other.')
        else: print('No overlap.')
        print('complementary distribution')
        print('allophones of the same phoneme')
        # reasoning - elsewhere vs. pattern (?)

    return None

def environment(phoneme, word):
    """Returns the environment of the given phoneme as a list."""
    env = []
    temp = []
    index = -1


    if phoneme in word:
        while True:
            try:
                index = word.index(phoneme, index+1)
                # print index
                env.append('#') if index is 0 else env.append(word[index-1])
                env.append('#') if index is (len(word)-1) else env.append(word[index+1])
            except ValueError, e:
                index = -1
                break

            # else:
            #     # insert character found before phoneme
            #     env.append('#') if index is 0 else env.append(word[index-1])
            #     # if index is 0:
            #     #     print('#')
            #     # else:
            #     #     print(word[index-1])


            #     # insert character found after phoneme
            #     env.append('#') if index is (len(word)-1) else env.append(word[index+1])
            #     # if index is (len(word)-1):
            #     #     print('#')
            #     # else:
            #     #     print(word[index+1])

    else:
        env = None

    if env is not None and len(env) > 2:
        for i in range(len(env)):
            if i % 2 is 0:
                temp.append(env[i:i+2])
    else:
        temp.append(env)

    env = temp
    return env

def prettyEnvironment(env):
    """Returns a pretty-printed (LIN110 exercise) version of the environment for a phoneme."""
    resultString = u''
    pairsSoFar = []
    for pair in env:
        # only print(it if this is not a duplicate pair
        if pair not in pairsSoFar:
            resultString += pair[0] + u"_" + pair[1] + u", "
            pairsSoFar.append(pair)
    # delete the last command and space
    # print type(resultString)
    # print type(resultString[:-2])
    return resultString[:-2]


def overlap(env1, env2, majority):
    """Returns true if the environments of the two phonemes overlap."""
    count = 0

    for pair1 in env1:
        for pair2 in env2:
            if pair1 == pair2: count += 1

    if count >= majority: return True

    return False

def oneSidedOverlap(env1, env2, majority):
    """Returns true if the environments of the two phonemes overlap on at least one side."""
    count = 0

    for pair1 in env1:
        for pair2 in env2:
            if pair1[0] == pair2[0] or pair1[1] == pair2[1]:
                count += 1
    return count >= majority

def meaning():
    """Returns true if substituting one phoneme for the other produces the same meaning."""
    return False
