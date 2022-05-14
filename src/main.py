import csv
from temp import WAVL

f = open('urbandict-csv.csv', 'rt')
dic = csv.reader(f)
wavl = WAVL()
def tokenize(word):
    new = ""
    for i in word:
        if i not in "[]\'":
            new += i
    return new.lower()
for word in dic:
    # word = word.lower()
    word = tokenize(word)
    wavl.insert(word)
query = input("What word u want to search")
while (query != "q"):
    print(wavl.search(query))
    query = input("What word u want to search")
# wavl.inorder()