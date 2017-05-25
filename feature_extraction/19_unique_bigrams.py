import csv

NUM = 10 #number of bigrams taken per character

class common_bigram:
	def __init__(self):
		self.dx = {}

	def create(self,inp): #make list of each row of csv: [[word1, word2], frequency]
		with open(inp,'r') as fin:
			#csvread = csv.reader(fin)
			#data = list(list(row) for row in csv.reader(fin, delimiter = ','))
			inlines = fin.readlines()
			l = []
			for i in range(NUM):
				line=inlines[i]
				itx=line.split()
				l.append([itx[0],itx[1],int(itx[2])])
		return l

	def common(self,l1,l2): #find common bigrams over all 6 lists
		temp = []
		for i in range(len(l1)):
			for j in range(i+1,len(l2)):
				if l1[i][0] == l2[j][0]:
					temp.append(l1[i])
		return temp

	def clean(self,l1,l2): #remove common bigrams from each list where l1 = list of all common, l2 = each of 6 lists
		for i in l1:
			for j in l2:
				if i[0] == j[0]:
					l2.remove(j)
		return l2

	def final_output(self,lists):
		final_list = []
		temp = []
		L = []
		common_words = []
		
		for i in range(len(lists)):
			for j in range(i+1,len(lists)):
				L.append(self.common(lists[i],lists[j]))

		for x in range(len(L)):
			for y in L[x]:
				common_words.append(y)		
		
		for i in range(len(lists)):
			temp = self.clean(common_words,lists[i])
			lists[i] = temp
		
		for character in lists:
			for i in character:
				final_list.append(i)
		final_list.sort(key=lambda x: x[1], reverse = True)
		
		for i in final_list:
			print(i)
		
		with open('unique_bigrams.csv','w') as fout:
			writer = csv.writer(fout)
			writer.writerows(final_list)

obj = common_bigram()
char_list = ['chandler','joey','monica','phoebe','rachel','ross']
lists = []
for i in char_list:
	inp = 'intermediate/cbigrams_' + i +'.txt'
	lists.append(obj.create(inp))				#appends the top 10 bigrams of every characters to lists
obj.final_output(lists)




