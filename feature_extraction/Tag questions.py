import re
import nltk
from nltk import pos_tag
from nltk import word_tokenize
file = open("C:\\Users\\shide\\Desktop\\MS Project\\just_phoebe.txt")
pronouns=['I','me','we','us','you','they','she','he','it','them']
counter = 0

with open("C:\\Users\\shide\\Desktop\\MS Project\\tag_questions.txt") as f: #split the verbs in list
    l =[word for line in f for word in line.split()]

for line in file:
    a=line.split()
    for j in range(len(a)):
     if a[j].lower() in l:
         next1 = a[j + 1]
         b = (next1)[-1]
         if next1[-1] == '?':
             thisw = next1[:-1]
             if thisw in pronouns:
                 counter = counter +1
print (counter)


