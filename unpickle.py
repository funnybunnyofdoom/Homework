import pickle

file = open('MS.dat','rb')
DICT = pickle.load(file)
print(DICT)
file.close()
