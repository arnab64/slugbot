import shutil
import os
import sys
import word_category_counter as wc
from collections import Counter, defaultdict
import csv

sent_file = sys.argv[1]

sent_input = []
with open(sent_file, 'rU') as csvfile:
	label_reader = csv.reader(csvfile)
	for row in label_reader:
		sent_input += [row]

wc.load_dictionary(wc.default_dictionary_filename())

csv_op = [["Filename","Sentence", "Positive Emotion", "Negative Emotion", "Sadness", "Anger", "Anxiety"]]
for pair in sent_input:
	name = pair[0]
	sentence = pair[1]
	liwc = wc.score_text(sentence)
	if liwc["Positive Emotion"] > liwc["Negative Emotion"]:
		x = 1
	elif liwc["Positive Emotion"] < liwc["Negative Emotion"]:
		x = -1
	else: x = 0

	csv_op += [[name, sentence, liwc["Positive Emotion"], liwc["Negative Emotion"], liwc["Sadness"], liwc["Anger"], liwc["Anxiety"],x]]

b = open(sent_file[:-4]+"_LIWC_Emotions.csv", "w")
a = csv.writer(b)
a.writerows(csv_op)
b.close()