import operator
myfile = open("/Users/cindyyang/Desktop/shakespeare.txt", "r")
line = myfile.read().strip("\n")

contentlist = line.split()
print("word count:", len(contentlist))

dictionary = {}
count = 0
uniquewords = 0

for i in contentlist:
    if (i in dictionary):
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        uniquewords += 1
dict2 = sorted(dictionary, key = dictionary.get)
print('number of unique words:', len(dictionary))

sorteddictionary = sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True)

newvalues = []
for i in range(50):
    x = sorteddictionary.pop(0)
    newvalues.append(x)


print(newvalues)
