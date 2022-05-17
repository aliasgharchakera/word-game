# import nltk
import random
import itertools
# nltk.download("words")
from nltk.corpus import words


def getallperms(letters): #letters is a string of letters
    lst = []
    for i in range(2,len(letters)+1):
        perms = list(itertools.permutations(letters,i))
        lst = lst + perms
    return lst



string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str = ""
for i in range(8):
    str = str + random.choice(string)

#print(getallperms(str))
print(getallperms(str))
