import string
textfile = open("sometext.txt", "r")
dictionary = {}
for line in textfile:
    line.strip()
    line.lower()
    line = line.translate(line.maketrans("", "",string.punctuation))
    words = line.split(" ")
    for word in words:
        if word in dictionary:
            dictionary[word] = dictionary[word]+1
        else:
            dictionary[word] = 1

for key in list(dictionary.keys()):
    print(key, " ", dictionary[key])

textfile.close()