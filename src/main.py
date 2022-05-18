# import csv
# import nltk
# import json
# nltk.download()
from random import randint, choice
# from this import d
# from webbrowser import get
from wavl import WAVL
from nltk.corpus import words
from typing import Any
import itertools

def tokenize(word: Any) -> str:
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()

def load_data(path: Any, wavl: WAVL) -> None:
    # f = open(path, 'rt')
    # f = open(path)
    # dic = json.load(f)
    # dic = csv.reader(f)
    dic = words.words()
    # i, j = 0, 0
    for word in dic:
        # i+= 1
        word = tokenize(word)
        if not wavl.search(word):
            # j += 1
            wavl.insert(word)
    # print(i, j)

def search(wavl: WAVL) -> None:
    query = input("What word u want to search: ")
    while (query != "q"):
        print(wavl.search(query))
        query = input("What word u want to search: ")

def alphabet_generator() -> list:
    alpha = ""
    vowels = "aeiou"
    tier1 = "aeionprst"
    tier2 = "ubcdfghlmv"
    tier3 = "jkqwxyz"
    common = "nprst"
    medium = "bcdfghlmv"
    rare = "jkqwxyz"
    abc = "bcdfghjklmnpqrstvwxyz"

    for i in range(8):
        a = randint(0, 9)
        if a in [0, 4, 8, 9]:
            alpha += choice(tier1)
        else:
            if a in [1, 2, 3, 7]:
                alpha += choice(tier2)
            elif a in [5, 6]:
                alpha += choice(tier3)
            # else:
            #     alpha.append(rare[randint(0, 6)])
            # alpha.append(vowels[randint(0, 4)])
    return alpha

def word_check(word: str, done: list, wavl: WAVL) -> bool:
    if wavl.search(word):
        wavl.remove(word)
        done.append(word)
        return True
    return False

def getallperms(letters: str): #letters is a string of letters
    lst = []
    for i in range(3,len(letters)+1):
        perms = list(itertools.permutations(letters,i))
        lst = lst + perms
    return lst #lst is list of tuples, each tuple is a permuatation

def truewords(perms): #perms is permutations list from getallperms function
    permutations = []
    for perm in perms:
        permutations.append("".join(perm))
    foundlst = list(set(permutations).intersection(set(x.lower() for x in words.words())))
    # print(len(foundlst))
    # print(foundlst)
    if len(foundlst) >= 49:
        return True, len(foundlst)
    return False, len(foundlst)

def main():
    print("Loading data...")
    print("Loaded data successfully")
    while True:
        alph = alphabet_generator()
        print(alph)
        perm = getallperms(alph)
        run, _length = truewords(perm)
        while not run:
            alph = alphabet_generator()
            print(alph)
            perm = getallperms(alph)
            run, _length = truewords(perm)
        done = list()
        points = 0
        word = input()
        while word != "q":
            if word_check(word, done, wavl):
                points += 5
                print("Valid entry", points)
            else:
                if word in done:
                    print("Duplicate entry not allowed")
                else:
                    print("Invalid word", points)
            word = input()
        for i in done:
            wavl.insert(i)

main()