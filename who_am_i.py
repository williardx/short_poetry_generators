#!/usr/local/bin/python
#Poem generator that asks you what you are
#and then tells you everything that you are.

'''
TO DO
* allow for multiple words
* factor in different parts of speech
* potentially only take first 5 words?
'''

import random, time
from nltk.corpus import wordnet as wn

def is_a(what):
    '''
    Returns list of words that hyponyms of each other
    using NLTK WordNet.
    '''
    words = []
    word_synsets = wn.synsets(what)
    if word_synsets == []:
        return False
    else:      
        word = random.choice(word_synsets)
        hypernyms = word.hypernym_paths()
        hypernyms_choice = random.choice(hypernyms)
        for synset in hypernyms_choice:
            words.append(synset.lemma_names)
        return sum(words, [])

def starts_with_vowel(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return word[0] in vowels

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
    if hnym_list == False:
        print "You are an unknown word. Try again."
    else:
        hnym_list.reverse()
        for word in hnym_list:
            if '_' in word:
                word = remove_underscores(word)
            print "You are " + article(word) + ' ' + word
            time.sleep(1.5)

if __name__ == "__main__":
    word = raw_input("What are you?\n\n> ")
    print "\n"
    poem(is_a(word))
