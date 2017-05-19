import word_category_counter as wc
import csv, os, sys


def read_csv(f):
	with open(f, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		return list(reader)


def write_csv(filename, rows, header_fields=None):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        if header_fields:
            writer.writerow(header_fields)
        for row in rows:
            writer.writerow(row)


def get_liwc_scores(wc, rows, col_name):
	categories = set()
	all_scores = []
	for row in rows:
		liwc_scores = wc.score_text(row[col_name])
		categories |= set(liwc_scores.keys())
	category_list = sorted(list(categories))
	for row in rows:
		liwc_scores = wc.score_text(row[col_name])
		#print(liwc_scores)
		all_scores += [[row[col_name]] + [liwc_scores.get(category, 0.0) for category in category_list]]
		#print(all_scores)
	return all_scores, category_list


def main():
	ip_filename = sys.argv[1]
	col_name = sys.argv[2]
	op_filename = sys.argv[3]

	wc.load_dictionary(wc.default_dictionary_filename())

	ip_rows = read_csv(ip_filename)
	ip_scores, category_list = get_liwc_scores(wc, ip_rows, col_name)
	write_csv(op_filename, ip_scores, ["text"] + category_list)

main()