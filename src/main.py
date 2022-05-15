import csv
from temp import WAVL

def tokenize(word):
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()

def loadData(path, wavl):
    f = open(path, 'rt')
    dic = csv.reader(f)
    for word in dic:
        # word = word.lower()
        word = tokenize(word)
        wavl.insert(word)
print("Loading data...")
wavl = WAVL()
loadData('urbandict-csv.csv', wavl)
print("Loaded data successfully")
query = input("What word u want to search")
while (query != "q"):
    print(wavl.search(query))
    query = input("What word u want to search")
# wavl.inorder()