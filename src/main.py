# import csv
# import nltk
# import json
# nltk.download()
from random import randint, randrange
from wavl import WAVL
from nltk.corpus import words
from typing import Any

def tokenize(word: Any) -> str:
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()

def loadData(path: Any, wavl: WAVL):
    # f = open(path, 'rt')
    # f = open(path)
    # dic = json.load(f)
    # dic = csv.reader(f)
    dic = words.words()
    i, j = 0, 0
    for word in dic:
        i+= 1
        word = tokenize(word)
        if not wavl.search(word):
            j += 1
            wavl.insert(word)
    # print(i, j)

def search(wavl: WAVL) -> None:
    query = input("What word u want to search: ")
    while (query != "q"):
        print(wavl.search(query))
        query = input("What word u want to search: ")

def alphabet_generator():
    alpha = []
    vowels = "aeiou"
    abc = "bcdfghjklmnpqrstvwxyz"

    for i in range(12):
        a = randint(0, 1)
        if a:
            alpha.append(abc[randint(0, 20)])
        else:
            alpha.append(vowels[randint(0, 4)])
    return alpha

def wordcheck(word: str, done: list, wavl: WAVL) -> bool:
    if wavl.search(word):
        wavl.remove(word)
        done.append(word)
        return True
    return False

# def words_possible(words, wavl):
#     for i in range(len(words)):
#         for j in range(len(words) - 1):

            

print("Loading data...")
wavl = WAVL()
loadData('urbandict-csv.csv', wavl)
print("Loaded data successfully")
search(wavl)
for i in range(5):
    alph = alphabet_generator()
    print(alph)