import re
import csv
import nltk
from nltk import pos_tag
from nltk import word_tokenize

class tag_questions:
    def __init__(self,fname,ofname):
        #self.inlines=
        self.fname=fname
        #self.read_csv(fname)
        self.pronouns=['i','me','we','us','you','they','she','he','it','them']
        fin=open('data_central/tag_questions.txt','r')
        
        ftext=fin.read()
        self.verb_list = ftext.split()
        self.ofile=open(ofname,'w')

    #def read_csv(self,fname):

            #return list(reader)
            #return reader

    def tagq(self,line):
        a=line.split()
        counter=0
        lenx=len(a)
        for j in range(lenx):
            if a[j].lower() in self.verb_list:
                if j+1!=lenx:            
                    next1 = a[j+1]
                    b = (next1)[-1]
                    if next1[-1] == '?':
                        thisw = next1[:-1]
                        if thisw in self.pronouns:
                            counter = counter +1
                else:
                    continue;
        return counter

    def control(self):
        infile=open(self.fname,'r')
        inlines=infile.readlines()
        count=0
        for line in inlines:            #inlines:
            count+=1
            scr=self.tagq(line)   
            self.ofile.write(str(scr)+'\n')
        print("count=",count)

lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
    print("Processing....",el)
    infname='character_data/just_'+el.lower()+'.txt'
    outfname='data_central/tag_questions_'+el.lower()+'.txt'
    t1=tag_questions(infname,outfname)
    t1.control()