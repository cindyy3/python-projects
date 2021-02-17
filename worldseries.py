import operator
myfile = open("/Users/cindyyang/Documents/python/world series winners.txt", "r")
file2 = list(myfile.readlines())

dictionary = {}

for i in file2:
    if (i.rstrip("\n") in dictionary):
        dictionary[i.rstrip("\n")] += 1
    else:
        dictionary[i.rstrip("\n")] = 1  

print(dictionary)

team = raw_input("enter an MLB team: ")

print("the", team, "have won the world series", dictionary[team], "times.")
sorteddictionary = sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True)

print(list(sorteddictionary[0]))
