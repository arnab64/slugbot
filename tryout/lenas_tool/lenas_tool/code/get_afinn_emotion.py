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
	
	afinn = dict(map(lambda kv: (kv[0],int(kv[1])), 
                     [ line.split('\t') for line in open("lexicons/AFINN-111.txt") ]))

	output = []
	with open(sent_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sent = text_printable(row[1])
			words = nltk.word_tokenize(sent)
			score = 0

			for word in words:
				if word in afinn:
					score += afinn[word]

			if score > 0:
				output += [[name,sent,1]]
			elif score < 0:
				output += [[name,sent,-1]]
			else:
				output += [[name,sent,0]]

	print_csv(sent_file[:-4]+"_AFINN_Emotions.csv", output)
main()