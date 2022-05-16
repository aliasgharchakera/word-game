import csv
import nltk
import json
nltk.download()
from random import randint, randrange
from wavl import WAVL

from nltk.corpus import words

def tokenize(word):
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()

def loadData(path, wavl):
    # f = open(path, 'rt')
    f = open(path)
    dic = json.load(f)
    # dic = csv.reader(f)
    # dic = words.words()
    for word in dic:
        word = tokenize(word)
        if not wavl.search(word):
            wavl.insert(word)

def search(wavl):
    query = input("What word u want to search")
    while (query != "q"):
        print(wavl.search(query))
        if wavl.search(query):
            wavl.remove(query)
            print("query removed from tree")
        query = input("What word u want to search")

def alphabet_generator():
    alpha = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(12):
        alpha.append(abc[randint(0, 25)])
    return alpha

# def words_possible(words, wavl):
#     for i in range(len(words)):
#         for j in range(len(words) - 1):

            

print("Loading data...")
wavl = WAVL()
loadData('urbandict-csv.csv', wavl)
print("Loaded data successfully")
search(wavl)
# wavl.inorder()
# for i in range(5):
#     alph = alphabet_generator()
#     print(alph)