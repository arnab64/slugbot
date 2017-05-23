Installation Guide:

To run this code you need to install Python and then the NLTK toolkit.


You can download Python from this link:
https://www.python.org/downloads/

This system uses Python3.


After you have installed Python, you can download NLTK from this link:
http://www.nltk.org/install.html

_____________________________________________________________________________


Input file:

Your input file is a csv file with two columns where the first column contains the name of the text. The name of the text is either denoted by a file name or a number. These names do not need to be unique. The second column has the text that you want to analyze. You can have as many rows as you want. 

**Note that the file should not have a header row. 



If you have a directory instead of a file you can input the following command from the command line to create the file in the format needed:

python get_input_file.py dir_name/ output_name


where dir_name/ is the name of the directory 
and output_name is the name that you want to give the output file. 



_____________________________________________________________________________


Running the code:

The following command runs the code:

sh __all_info.sh text_file dir_name


where text_file is the name of the file with your data WITHOUT the ".csv", so if the name is blogs_sentences.csv, text_file is blogs_sentences
and dir_name is the name of the directory where you will store this information. This directory does not need to exist beforehand. 


LIWC categories:

To run the LIWC categories code:

python code/get_liwc_cat.py text_file
(Can use python2 or python3)




_____________________________________________________________________________

Output:

You will get a csv file in your new directory called all_info.csv that has the following 8 columns:

File Name, Text, Marked Text, LIWC, MPQA, AFINN, Connotation, Consensus

File Name - the name of the text given in the input file
Text - the original, unmodified text
Marked Text - the text with the polarities from the lexicons assigned to each word
LIWC - the label given by the LIWC lexicon
MPQA - the label given by the MPQA lexicon
AFINN - the label given by the AFINN lexicon
Connotation - the label given by the Connotation lexicon
Consensus - the "consensus" label which is as follows:
	If the majority (3 or 4) of the classifiers give a consistent pos, neg or neutral label then that is the "consensus" label
	If there is no consensus label then it is labeled as none


There is also a directory called supplemental_info that has the individual outputs of the lexicons and additional information used to create the all_info.csv. Looking at the information in this directory is not necessary but you are welcome to if you would like.


_____________________________________________________________________________

Sources:
LIWC
J. W. Pennebaker, L. E. Francis, and R. J. Booth, 2001.
LIWC: Linguistic Inquiry and Word Count.

MPQA
T. Wilson, J. Wiebe, and P. Hoffmann, 2005. Recognizing Contextual Polarity in Phrase-Level Sentiment Analysis. Proc. of HLT-EMNLP-2005.

AFINN
F. Nielsen, 2011. AFINN. Informatics and Mathematical Modelling, Technical University of Denmark.

Connotation
S. Feng, J.S. Kang, P. Kuznetsova, and Y. Choi, 2013. Connotation Lexicon: A Dash of Sentiment Beneath the Surface Meaning. Association for Computational Linguistics (ACL).

