import word_category_counter as wc
import csv, os, sys

def read_file(f):
	infile=open(f,'r',encoding="utf8")
	inlines=infile.readlines()
	return inlines

def write_csv(filename, rows, header_fields=None):
    with open(filename, 'w', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile)
        if header_fields:
            writer.writerow(header_fields)
        for row in rows:
            writer.writerow(row)

def get_liwc_scores(wc, rows):
	categories = set()
	all_scores = []
	count=0
	#print(len(rows))
	for sent in rows:
		count+=1
		liwc_scores = wc.score_text(sent)
		categories |= set(liwc_scores.keys())
	#print("counted",count)
	category_list = sorted(list(categories))
	count2=0
	for sent in rows:
		liwc_scores = wc.score_text(sent)
		#print(liwc_scores)
		#all_scores += [[row[col_name]] + [liwc_scores.get(category, 0.0) for category in category_list]]
		#print(all_scores)
		all_scores += [[liwc_scores.get(category, 0.0) for category in category_list]]
		#print(all_scores)
		#print(all_scores)
		count2+=1
	print("count2=",count2)
	return all_scores, category_list


def main(infname,outfname):
	#ip_filename = sys.argv[1]
	#col_name = sys.argv[2]
	#op_filename = sys.argv[3]

	ip_filename = infname
	#col_name = colname
	op_filename = outfname
	wc.load_dictionary(wc.default_dictionary_filename())
	ip_rows = read_file(ip_filename)
	ip_scores, category_list = get_liwc_scores(wc, ip_rows)
	write_csv(op_filename, ip_scores, category_list)

#lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
#tbbt=['Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']

lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel','Raj','Leonard','Sheldon','Penny','Howard','Bernadette','Amy']
for el in lx:
    print("Processing....",el)
    infname='../character_data/just_'+el.lower()+'.txt'
    outfname='../intermediate/liwc_'+el.lower()+'.csv'
    main(infname,outfname)