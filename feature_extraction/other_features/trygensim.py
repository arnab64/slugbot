import gensim, os, tempfile
from collections import defaultdict
from gensim import corpora
from six import iteritems

class MyCorpus(object):
    def __init__(self):
        self.documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",              
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"] 
        self.TEMP_FOLDER = tempfile.gettempdir()
        self.stoplist = set('for a of the and to in'.split())

    def __iter__(self):
        for line in open('mycorpus.txt'):
            yield dictionary.doc2bow(line.lower().split())

    def remcom(self):
        # remove common words and tokenize
        
        texts = [[word for word in document.lower().split() if word not in self.stoplist]
                 for document in self.documents]
        # remove words that appear only once
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1
        texts = [[token for token in text if frequency[token] > 1] for text in texts]
        self.dictionary = corpora.Dictionary(texts)
        self.dictionary.save(os.path.join(self.TEMP_FOLDER, 'deerwester.dict'))

        from pprint import pprint  # pretty-printer
        pprint(texts)
        print(self.dictionary.token2id)

        new_doc = "Human computer interaction"
        new_vec = self.dictionary.doc2bow(new_doc.lower().split())
        print(new_vec)


    def second(self):
        # collect statistics about all tokens
        dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))

        # remove stop words and words that appear only once
        stop_ids = [dictionary.token2id[stopword] for stopword in self.stoplist 
                    if stopword in dictionary.token2id]
        once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]

        # remove stop words and words that appear only once
        dictionary.filter_tokens(stop_ids + once_ids)

        # remove gaps in id sequence after words that were removed
        dictionary.compactify()
        print(dictionary)        

mc=MyCorpus()
mc.remcom()
mc.second()