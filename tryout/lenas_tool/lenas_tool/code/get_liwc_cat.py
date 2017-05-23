import shutil
import os
import sys
import word_category_counter as wc
from collections import Counter, defaultdict
import csv
import nltk
from nltk.tokenize import RegexpTokenizer


def read_dict(file_name):
	data = []
	with open("lexicons/liwc_cat/"+file_name, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			data += [row[0]]
	return data


liwc_pro = read_dict("LIWC2015_English_Flat_pro.txt")
liwc_conj = read_dict("LIWC2015_English_Flat_conj.txt")
liwc_inf = read_dict("LIWC2015_English_Flat_inf.txt")



def get_indicators(sentence):
	words = nltk.word_tokenize(sentence)
	old_words = []
	pro_count = 0
	conj_count = 0
	inf_count = 0
	for word in words:
		if word in old_words: continue
		indicators = []
		if word.lower() in liwc_pro:
			indicators += ["LP_"]
			pro_count += 1
		if word.lower() in liwc_conj:
			indicators += ["LC_"]
			conj_count += 1
		if word.lower() in liwc_inf:
			indicators += ["LI_"]
			inf_count += 1

		mod_word = word.lower() + "*"
		while mod_word != "*" and (not "LC_" in indicators or not "LP_" in indicators or not "LI_" in indicators):
			if mod_word in liwc_pro:
				indicators += ["LP_"]
				pro_count += 1
			if mod_word in liwc_conj:
				indicators += ["LC_"]
				conj_count += 1
			if mod_word in liwc_inf:
				indicators += ["LI_"]
				inf_count += 1
			mod_word = mod_word[:-2]+"*"

		if old_words == []:
			for ind in indicators:
				sentence = ind + sentence
		else:
			ind_word = word
			for ind in indicators:
				ind_word = ind + ind_word

			if ind_word != word:
				sentence = sentence.replace(" "+ word," " +ind_word)

		old_words += [word]
	return sentence, pro_count, conj_count, inf_count





sent_file = sys.argv[1]

sent_input = []
with open(sent_file, 'rU') as csvfile:
	label_reader = csv.reader(csvfile)
	for row in label_reader:
		sent_input += [row]


tokenizer = RegexpTokenizer(r'\w+')
csv_op = [["Filename","Sentence","Marked Sentence","Num sentences","Average words per sentence", "Total Pronouns", "Conjunctions", "Informal"]]
for pair in sent_input:
	name = pair[0]
	sentence = pair[1]
	mod_sentence,pro_count,conj_count,inf_count = get_indicators(sentence)
	num_sentences = len(nltk.sent_tokenize(sentence))
	tokens = len(tokenizer.tokenize(sentence))

	
	csv_op += [[name, sentence,mod_sentence,num_sentences,1.0*tokens/num_sentences, pro_count,conj_count,inf_count]]

b = open(sent_file[:-4]+"_LIWC_Cats.csv", "w")
a = csv.writer(b)
a.writerows(csv_op)
b.close()