import os, sys, csv, nltk, re

def print_csv(name,array):
	b = open(name,'w')
	a = csv.writer(b)
	a.writerows(array)
	b.close()

def text_printable(text):
	text = text.replace('\xc2\xbd','1/2').replace('\xc2\x91','\'').replace('\xc2\x92','\'').replace('\xc2\x93','\"').replace('\xc2\x94','\"')
	text = re.sub(r'[^\x00-\x7F]+','', text).replace("\n", " ")
	return text

def read_dict(file_name):
	data = []
	with open("lexicons/lexicons_pos_neg/"+file_name, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			data += [row[0]]
	return data

afinn_neg = read_dict("AFINN-111_neg.txt")
afinn_pos = read_dict("AFINN-111_pos.txt")
conno_neg = read_dict("connotation_lexicon_a.0.1_neg.txt")
conno_pos = read_dict("connotation_lexicon_a.0.1_pos.txt")
liwc_neg = read_dict("LIWC2015_English_Flat_neg.txt")
liwc_pos = read_dict("LIWC2015_English_Flat_pos.txt")
mpqa_neg = read_dict("subjclueslen1-HLTEMNLP05_neg.txt")
mpqa_pos = read_dict("subjclueslen1-HLTEMNLP05_pos.txt")


def get_indicators(sentence):
	words = nltk.word_tokenize(sentence)
	old_words = []
	for word in words:
		if word in old_words: continue
		indicators = []
		if word in afinn_neg:
			indicators += ["AN_"]
		if word in afinn_pos:
			indicators += ["AP_"]
		if word in conno_neg:
			indicators += ["CN_"]
		if word in conno_pos:
			indicators += ["CP_"]
		if word in mpqa_neg:
			indicators += ["MN_"]
		if word in mpqa_pos:
			indicators += ["MP_"]
		if word in liwc_neg:
			indicators += ["LN_"]
		if word in liwc_pos:
			indicators += ["LP_"]

		mod_word = word + "*"
		while mod_word != "*" and (not "LN_" in indicators or not "LP_" in indicators):
			if mod_word in liwc_neg:
				indicators += ["LN_"]
			if mod_word in liwc_pos:
				indicators += ["LP_"]
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
	return sentence


def main():
	data_file = sys.argv[1]

	count = 0
	output = []
	with open(data_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			count += 1
			#print count
			name = row[0]
			sentence = text_printable(row[1])
			mod_sentence = get_indicators(sentence)
			output += [[name,mod_sentence]]


	print_csv(data_file.replace(".csv","_indicators.csv"),output)



main()