import re
import collections


dic = {}
char = []
rematch = []
file=open('titanic.txt','r')
count = 50


m = file.read()

match = re.findall(r'\s\s\s+\w.+', m)  #Find charactors from text
l = len(match)

for i in range(l):
    rematch.append(match[i].strip())   #remove white spaces
print ('rematch is: ', rematch)
for item in rematch[:]:
    if item == 'CUT TO:':
        rematch.remove(item)
print(rematch)

dic = {rematch.count(x):x for x in rematch}  # Building a dictionary from the list to count and rid of duplicates.
print ('dic is:', dic)
a, b = dic.keys(), dic.values()



