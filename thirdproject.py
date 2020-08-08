file = open('chandra.txt')
#print(file.read())

#print(file.readline())

for line in file.readlines():
    print(line)


file.close()



