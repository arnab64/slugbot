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


def run_mpqa():
	mpqa_file = sys.argv[3]

	opp_data = []
	with open(mpqa_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sent = row[1]
			label = int(row[4])
			if label == 1:
				opp_data += [[name,sent,"pos"]]
			elif label == -1:
				opp_data += [[name,sent,"neg"]]
			else:
				opp_data += [[name,sent,"neutral"]]
	return opp_data

def run_liwc():
	liwc_file = sys.argv[3]

	opp_data = []
	with open(liwc_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		next(label_reader)
		for row in label_reader:
			name = row[0]
			sent = row[1]
			label = int(row[7])
			if label == 1:
				opp_data += [[name,sent,"pos"]]
			elif label == -1:
				opp_data += [[name,sent,"neg"]]
			else:
				opp_data += [[name,sent,"neutral"]]
	return opp_data

def run_afinn_conno():
	other_file = sys.argv[3]

	opp_data = []
	with open(other_file, 'rU') as csvfile:
		label_reader = csv.reader(csvfile)
		for row in label_reader:
			name = row[0]
			sent = row[1]
			label = int(row[2])
			if label == 1:
				opp_data += [[name,sent,"pos"]]
			elif label == -1:
				opp_data += [[name,sent,"neg"]]
			else:
				opp_data += [[name,sent,"neutral"]]
	return opp_data

def main():
	output_name = sys.argv[1]
	type_run = sys.argv[2]

	if type_run == "mpqa":
		output = run_mpqa()	
	elif type_run == "liwc":
		output = run_liwc()	
	elif type_run == "afinn":
		output = run_afinn_conno()
	else:
		print("Error: Invalid Type")
		return

	print_csv(output_name,output)

main()