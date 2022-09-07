import pickle

infile = open("datastore_dict", "rb")

datastore = pickle.load(infile)

print(datastore)