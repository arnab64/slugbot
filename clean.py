import string

class preprocessing:
	def __init__(self):
		self.x = 1;

	def voiceover(self,inpf):
		with open(inpf) as fin:
			line = fin.readlines()
			print(line)

	def del_words(self,inpf,outf):
		delete_list = ["CUT TO\n", " (V.O.)","FADE TO BLACK:\n"]
		
		
		f = open(inpf,"r+")
		d = f.readlines()
		f.seek(0)
		for i in d:
			if i!="\n":
				f.write(i)

		f.truncate()
		f.close()


		fin = open(inpf,"r+")
		fout = open("intermediate.txt", "w+")

		for line in fin:
			for word in delete_list:
				line = line.replace(word, "")
			fout.write(line)
		fin.close()
		fout.close()

		fin = open("intermediate.txt","r")
		fout = open(outf,"w")

		fin.seek(0)
		fout.seek(0)

		d = fin.readlines()
		x =[]
		toggle = 0

		for i in d:
			if i.isupper() == False:
				i = i.replace("\n","")
				x.append(i)
			else:
				temp = ' '.join(x)
				fout.write(temp)
				fout.write("\n")
				i = i.replace("\n","")
				fout.write(i)
				fout.write(": ")
				x = []
				
inpf = 'fightclub_dialog.txt'
outf = 'output.txt'
clean = preprocessing()
clean.voiceover(outf)
clean.del_words(inpf,outf)