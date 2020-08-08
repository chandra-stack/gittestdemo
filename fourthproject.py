with open('chandra.txt','r') as read:
    content=read.readlines()
    print(content)
    with open('chandra.txt','w') as write:
        for line in reversed(content):
            print(line)
            write.write(line)


