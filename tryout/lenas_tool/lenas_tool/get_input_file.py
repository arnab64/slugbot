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
	text_dir = sys.argv[1]
	output_name = sys.argv[2]

	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

	if not text_dir[-1] == "/": text_dir += "/"

	text_names = os.listdir(text_dir)

	output = []
	for name in text_names:
		print name
		text_file = open(text_dir+name)
		#print name
		text_read = text_printable(text_file.read())
		#print text_read
		sentences = tokenizer.tokenize(text_read)
		for sent in sentences:
			output += [[name,sent]]


	print_csv(output_name,output)

main()