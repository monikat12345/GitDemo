file = open('test.txt')
#read n number of characters from contents of file and if not provided then whole content will be read
#print(file.read(4)) #pointer will reach at 4th letter

#print(file.readline())#read one single line
#print(file.readline())

#Method 1 to print line by line using readline method
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()

######################method 2 to read file
for line in file.readlines():
    print(line)
file.close()