import nltk,sys


def word_count(inp,outp):
	fin = open(inp,'r')
	fout = open(outp,'w')
	lines = fin.readlines()
	total_words = 0
	total_char = 0
	for index, value in enumerate(lines):
		for w in value.split():
			total_char += len(w)
		words = len(value.split())
		total_words += words
		fout.write('{}\n'.format(words))

	fout.write('\n{}\n{}'.format(total_words,total_char/total_words))

def lex_freq(inp,outp):
	
	fout = open(outp,'w')
	with open (inp, "r") as fin:
		data=fin.read().replace('\n', ' ')
	data = data.split(' ')
	
	dist = nltk.FreqDist(data).most_common()
	for word,freq in dist:
		fout.write('{} : {}\n'.format(word,freq))


char_list=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for l in char_list:
	
	#infname='character_data/'+el+'_all.txt'
	outp1 = 'words_'+l.lower()+'.txt'
	outp2 = 'freq_'+l.lower()+'.txt'
	inp='just_'+l.lower()+'.txt'
	word_count(inp,outp1)
	lex_freq(inp,outp2)

	