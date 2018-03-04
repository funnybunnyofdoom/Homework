import pickle

MobileSuits = {'Amuro Ray':'RX-78 Gundam','Char Aznable':'Red Zaku II','Kou Uraki':'Gundam GP-01','Gaia':'Rick Dom'} #Build the dictionary

file = open('MS.dat', 'wb') #Open the file to write
pickle.dump(MobileSuits, file) #use picke to dump the dictionary into a file.
file.close() #Close the file
