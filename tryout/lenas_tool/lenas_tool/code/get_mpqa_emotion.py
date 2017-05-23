import shutil
import os
import sys
import re
import csv

def f(entry):
	return entry[entry.find("=")+1:]

#clue_type: strongsubj, weaksubj
#clue_polarity: positive, negative, neutral

#sent_file format: filename, pattern, patterninfo, sentence, fulltext
#given sentences_csv, make a new file with all sentences that contain subjective cues

#Usage: python check_subj_in_sentences.py sentencefile opfile

ip_file = "lexicons/subjclueslen1-HLTEMNLP05.tff"
sent_file = sys.argv[1]
#op_file = sys.argv[2]

subj_file = open(ip_file)
subj_read = subj_file.read().split("\n")

sent_input = []
with open(sent_file, 'rU') as csvfile:
	label_reader = csv.reader(csvfile)
	for row in label_reader:
		sent_input += [row]

pos_strong = set()
pos_weak = set()
neg_strong = set()
neg_weak = set()

for subj_clue in subj_read:
	subj_clue_info = subj_clue.split(" ")
	if len(subj_clue_info) > 6:
		clue_type, clue_len, clue, clue_pos, clue_stemmed, clue_polarity, clue_priorpolarity = subj_clue_info
	else:
		clue_type, clue_len, clue, clue_pos, clue_stemmed, clue_priorpolarity = subj_clue_info

	clue_priorpolarity = f(clue_priorpolarity)
	clue_type = f(clue_type)
	clue = f(clue)

	if clue_priorpolarity == "positive" and clue_type == "strongsubj":
		pos_strong.add(clue)
	elif clue_priorpolarity == "positive" and clue_type == "weaksubj":
		pos_weak.add(clue)
	elif clue_priorpolarity == "negative" and clue_type == "strongsubj":
		neg_strong.add(clue)
	elif clue_priorpolarity == "negative" and clue_type == "weaksubj":
		neg_weak.add(clue)

neg_strong.remove("fun")

sentence_subj_matches = []
dictionaries = {"pos_strong":pos_strong, "pos_weak":pos_weak, "neg_strong":neg_strong, "neg_weak":neg_weak, 
				"positive":pos_strong|pos_weak, "negative":neg_strong|neg_weak}

for sent in sent_input:
	title = sent[0]
	text_read = sent[1]

	text_words = text_read.split(" ")
	text_words = [x.lower() for x in text_words]
	matches = {}
	matches_strings = {}
	for name,value in dictionaries.items():
		matches[name] = set([word for word in text_words if word in value])
		matches_strings[name] = " : ".join(matches[name])

	if len(matches["positive"]) > len(matches["negative"]): x = 1
	elif len(matches["positive"]) < len(matches["negative"]): x=-1
	else: x=0


	#if (matches["pos_strong"] or matches["pos_weak"]) and (matches["neg_strong"] or matches["neg_weak"]):
	sentence_subj_matches.append([title,text_read, len(matches["positive"]), len(matches["negative"]), x])# ,matches_strings["positive"],matches_strings["negative"]])


b = open(sent_file[:-4]+"_MPQA_Emotions.csv", "w")
a = csv.writer(b)
a.writerows(sentence_subj_matches)
b.close()