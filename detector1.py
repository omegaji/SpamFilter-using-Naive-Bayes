import _pickle as c
import os
from sklearn import *
from collections import Counter


def load(clf_file):
    with open(clf_file,"rb") as fp:
        print(fp)
        clf = c.load(fp)
    return clf
print("hehhhhh")

def make_dict():
    direc = r"C:\Users\sujoy\OneDrive\Desktop\bigDataproject\email\\"
    files = os.listdir(direc)
    print("wwwwwwwwwwwwwwwww")
    files.pop()
    files.pop()
    print(files)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)
    for email in emails:

        if email[42:-1] != 'code':
            f = open(email,encoding="latin-1")
            blob = f.read()
            words += blob.split(" ")

        print (c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)




clf = load("text-classifier.mdl")
d = make_dict()


while True:
    features = []
    inp = input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    if res[0]==0:
        print("NOT SPAM")
    else:
        print(" SPAM")
