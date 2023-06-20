#file = open('test.txt')

#file.close()

##no need to close file explicitly
#program to read the file in a list and reverse the list and write back to the file
with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)




