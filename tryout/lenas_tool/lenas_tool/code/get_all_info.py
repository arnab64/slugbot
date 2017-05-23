import os, sys, csv, re

def print_csv(name,array):
	b = open(name,'w')
	a = csv.writer(b)
	a.writerows(array)
	b.close()

def read_csv(file_name):
	data = []
	with open(file_name, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sentence = row[1]
			label = row[2]
			data += [[name,sentence,label]]
	return data

def read_mod(file_name):
	data = []
	with open(file_name, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sentence = row[1]
			data += [[name,sentence]]
	return data


def get_majority(lexicons):
	pos_num = lexicons.count("pos")
	neg_num = lexicons.count("neg")
	neutral_num = lexicons.count("neutral")

	if pos_num > neg_num and pos_num > neutral_num:
		return "pos"
	if neg_num > pos_num and neg_num > neutral_num:
		return "neg"
	if neutral_num > pos_num and neutral_num > neg_num:
		return "neutral"
	return "none"



def get_output(output,all_liwc_data,all_mpqa_data,all_afinn_data,all_conno_data,mod_sent_data,num_sent):
	for x in range(0,num_sent):
		liwc_data = all_liwc_data[x]
		mpqa_data = all_mpqa_data[x]
		afinn_data = all_afinn_data[x]
		conno_data = all_conno_data[x]
		mod_sent = mod_sent_data[x][1]

		name = liwc_data[0]
		sentence = liwc_data[1]

		liwc = liwc_data[2]
		mpqa = mpqa_data[2]
		afinn = afinn_data[2]
		conno = conno_data[2]

		consensus = get_majority([liwc,mpqa,afinn,conno])

		output += [[name,sentence,mod_sent,liwc,mpqa,afinn,conno,consensus]]

	return output

def main():
	liwc_file = sys.argv[1]
	mpqa_file = sys.argv[2]
	afinn_file = sys.argv[3]
	conno_file = sys.argv[4]
	mod_sent_file = sys.argv[5]

	liwc_data = read_csv(liwc_file)
	mpqa_data = read_csv(mpqa_file)
	afinn_data = read_csv(afinn_file)
	conno_data = read_csv(conno_file)
	mod_sent_data = read_mod(mod_sent_file)


	num_sent = len(liwc_data)


	output = [["File Name","Text","Marked Text","LIWC","MPQA","AFINN","Connotation","Consensus"]]
	output = get_output(output,liwc_data,mpqa_data,afinn_data,conno_data,mod_sent_data,num_sent)

	print_csv("all_info.csv",output)



main()