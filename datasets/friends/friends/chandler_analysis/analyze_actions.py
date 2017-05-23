import nltk

txtx="And I just want a million dollars!"
text = nltk.word_tokenize(txtx)

print(nltk.pos_tag(text))