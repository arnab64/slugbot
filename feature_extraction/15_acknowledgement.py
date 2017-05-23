import re
import nltk
from nltk import pos_tag
from nltk import word_tokenize


class acknowledgement:
    def __init__(self,infname,ofname):
        self.infname=infname
        ack=open('data_central/acknowledgement.txt','r')
        for word in ack:
            b = word.split()
        self.target= open(ofname,'w')

    def process(self):
        f=self.inf.readlines()
        for line in f:
            for i in range(len(b)):
                if b[i] in line:
                    count = 1
                    #target.write("1")
                    break
                else:
                    count = 0
            if count == 1:
                self.target.write("1")
            else:
                self.target.write("0")
            self.target.write("\n")    
        self.target.close() 
        self.ack.close()  

lx=['Monica','Phoebe','Ross','Chandler','Joey','Rachel']
for el in lx:
    infname='character_data/justtwo_'+el.lower()+'.txt'
    outfname='data_central/acknowledgement_'+el.lower()+'.txt'
    ackk=acknowledgement(infname,outfname)
    ackk.process()