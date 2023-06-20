Itemincart = 0

if Itemincart != 2:
    pass
    #raise(Exception("products cart not matching"))

#assert(Itemincart >= 2)
try:
    with open('test1.txt', 'r') as reader:
        reader.read()

except:
    print("somehow reached here")

try:
    with open('test1.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally: ################it is executed in fail and pass both cases. ex - cleaning cookies
    print("cleaning up resources")