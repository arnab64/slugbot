import os, sys, csv, nltk, re

data_file = sys.argv[1]

pos_data = []
neg_data = []
with open(data_file, 'rU') as csvfile:
	label_reader = csv.reader(csvfile)		
	for row in label_reader:
		pair = row[0].split("\t")
		if "31" in pair[1:]:
			pos_data += [[pair[0]]]
		elif "32" in pair[1:]:
			neg_data += [[pair[0]]]

b = open(data_file.replace(".txt","_neg.txt"),'w')
a = csv.writer(b)
a.writerows(neg_data)
b.close()

b = open(data_file.replace(".txt","_pos.txt"),'w')
a = csv.writer(b)
a.writerows(pos_data)
b.close()