#!/usr/local/bin/python
#Poem generator that asks you what you are
#and then tells you everything that you are.

import random
from nltk.corpus import wordnet as wn

def is_a(what):
    '''
    Returns list of words that hyponyms of each other
    using NLTK WordNet.
    '''
    words = []
    word_synsets = wn.synsets(what)
    word = random.choice(word_synsets)
    hypernyms = word.hypernym_paths()
    hypernyms_choice = random.choice(hypernyms)
    for synset in hypernyms_choice:
        words.append(synset.lemma_names)
    return reduce(list.__add__, words)

def starts_with_vowel(word):
    return word.startswith('a') or \
           word.startswith('e') or \
           word.startswith('i') or \
           word.startswith('o') or \
           word.startswith('u')

def article(word):
    if starts_with_vowel(word):
        return 'an'
    else:
        return 'a'

def remove_underscores(word):
    l = word.split("_")
    return " ".join(l)
        
def poem(hnym_list):
    '''
    Generates "poem" from hyponyms.
    '''
    hnym_list.reverse()
    for word in hnym_list:
        if '_' in word:
            word = remove_underscores(word)
        print "You are " + article(word) + ' ' + word

if __name__ == "__main__":
    word = raw_input("What are you?\n\n> ")
    print "\n"
    poem(is_a(word))
