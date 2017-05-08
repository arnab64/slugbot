import numpy as np

data = np.loadtxt('data_central/train/sentiment_train_chandler.txt')
print(data.shape)
print(np.std(data, axis=0))

