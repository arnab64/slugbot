inf=open('data_central/train_test/tbbt_train_penny.txt','r')
inl=inf.readlines()
for j in range(len(inl)):
    print(len(inl[j].split(',')))