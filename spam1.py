import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import _pickle as c


def save(clf, name):
    with open(name, 'wb') as fp:
        c.dump(clf, fp)
    print ("saved")


def make_dict():
    direc = r"C:\Users\omega\Desktop\spam_detector\\"
    files = os.listdir(direc)
    #print("wwwwwwwwwwwwwwwww")
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


def make_dataset(dictionary):
    direc =  r"C:\Users\omega\Desktop\spam_detector\\"
    files = os.listdir(direc)
    
    files.pop()
    files.pop()
    print(files)
    emails = [direc + email for email in files]
    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        if email[42:-1] != 'code':
            f = open(email,encoding="latin-1")
            words = f.read().split(' ')
            for entry in dictionary:
                data.append(words.count(entry[0]))
            feature_set.append(data)

            if "ham" in email:
                labels.append(0)
            if "spam" in email:
                labels.append(1)
        print (c)
        c = c - 1
    return feature_set, labels


d = make_dict()
features, labels = make_dataset(d)
print("h")
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)
print("hs");

clf = MultinomialNB()
print(len(features))
print(len(labels))
clf.fit(x_train, y_train)


preds = clf.predict(x_test)
print (accuracy_score(y_test, preds))
save(clf, "text-classifier.mdl")
