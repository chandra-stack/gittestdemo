with open('chandra.txt','r') as reader:
    contents=reader.readlines()
    for line in reader.readlines():
        print(line)

    with open('chandra.txt','w') as writer:
        for newline in reversed(contents):
            print(newline)
            writer.write(newline)


