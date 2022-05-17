# import csv
# import nltk
# import json
# nltk.download()
from random import randint, randrange
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
    alpha = []
    vowels = "aeiou"
    common = "nprst"
    medium = "bcdfghlmv"
    rare = "jkqwxyz"
    abc = "bcdfghjklmnpqrstvwxyz"

    for i in range(12):
        a = randint(0, 9)
        if a in [0, 4, 8]:
            alpha.append(vowels[randint(0, 4)])
        else:
            if a in [1, 2, 3, 7]:
                alpha.append(common[randint(0, 4)])
            elif a in [5, 6]:
                alpha.append(medium[randint(0, 8)])
            else:
                alpha.append(rare[randint(0, 6)])
            # alpha.append(vowels[randint(0, 4)])
    return alpha

def word_check(word: str, done: list, wavl: WAVL) -> bool:
    if wavl.search(word):
        wavl.remove(word)
        done.append(word)
        return True
    return False

# def words_possible(words, wavl):
#     for i in range(len(words)):
#         for j in range(len(words) - 1):

def getallperms(letters: list, wavl: WAVL): #letters is a string of letters
    lst = []
    str = " ".join([i for i in letters])
    for i in range(3,len(str)+1):
        perms = list(itertools.permutations(str,i))
        lst = lst + perms
    count = 0
    print(lst[0])
    # for i in list:
    #     if wavl.search(i):
    #         count += 1
    return count #lst is list of tuples, each tuple is a permuatation

def main():
    print("Loading data...")
    wavl = WAVL()
    load_data('urbandict-csv.csv', wavl)
    print("Loaded data successfully")
    # search(wavl)
    # for i in range(5):
    while True:
        alph = alphabet_generator()
        print(alph)
        # print(getallperms(alph, wavl))
        done = list()
        points = 0
        word = input()
        while word != "q":
            if word_check(word, done, wavl):
                points += 5
                print("Valid entry", points)
            else:
                print("Invalid entry", points)
            word = input()
        for i in done:
            wavl.insert(i)

main()
