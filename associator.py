#!/usr/local/bin/python
#Word "free association" engine -- given a word and the number 
#of words you want, the associator gives you a list of words where
#each word is semantically related to its nearest neighbor.

import random
from nltk.corpus import wordnet as wn

def get_nyms(word, nym_method):
    '''
    Gets the *-nym of a word. Methods include
    'hyponym', 'hypernym', 'part_meronym', etc.
    Check nltk for documentation
    '''
    synsets = wn.synsets(word)
    nym_list = []
    for entry in synsets:
        nym_names = []
        nyms = getattr(entry, nym_method)()
        #print nyms
        for n in nyms:
            names = n.lemma_names
            #print names
            for name in names:
                nym_names.append(name)
                #print name
        nym_list.append(nym_names)
        #print nym_list
    return sum(nym_list, [])

def remove_underscores(word):
    l = word.split("_")
    return " ".join(l)
        
def make_associations(word, n=20):
    '''
    Generate list of free associations.
    '''
    nyms = ["part_meronyms", "substance_meronyms", "member_holonyms",
            "entailments", "hyponyms", "hypernyms"]
    next_word = word
    wordlist = [next_word]
    for i in range(n):
        next_nym_list = []
        for nym in nyms:
            next_nym_list.append(get_nyms(next_word, nym))
        next_nym = sum(next_nym_list, [])
        if len(next_nym) <= 1:
            return wordlist
        else:
            while next_word in wordlist:
                next_word = random.choice(next_nym)
        wordlist.append(next_word)

    return wordlist


if __name__ == "__main__":
    word = raw_input("Enter an input word.\n\n> ")
    n = raw_input("How many associations would you like?\n\n> ")
    if wn.synsets(word) == []:
        print "Unknown word. Try again."
    else:
        print "\n"
        nymlist = make_suggestions(word,int(n))
        for nym in nymlist:
            print remove_underscores(nym)
        print "\n"
