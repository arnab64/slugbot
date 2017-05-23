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

def main():
	sent_file = sys.argv[1]
	lexicon_file = sys.argv[2]


	lexicon_pos = []
	lexicon_neg = []
	with open(lexicon_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			word = row[0].split("_")[0]
			label = row[1]
			if label == "positive":
				lexicon_pos += [word]
			if label == "negative":
				lexicon_neg += [word]

	output = []
	with open(sent_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sent = text_printable(row[1])
			words = nltk.word_tokenize(sent)

			pos_score = 0
			neg_score = 0
			
			for word in words:
				if word in lexicon_pos:
					pos_score += 1
				if word in lexicon_neg:
					neg_score += 1

			if neg_score < pos_score:
				output += [[name,sent,1]]
			elif neg_score > pos_score:
				output += [[name,sent,-1]]
			else:
				output += [[name,sent,0]]

	print_csv(sent_file[:-4]+"_Connotation_Emotions.csv", output)

main()