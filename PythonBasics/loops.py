a=2
if a==2:
    print("This is true")
    print("It does match")
else:
    print("This is false")

print("we are now out of condition")

#for loop

items = [3,6,1,8,9]
for i in items:
    print(i)
    print(items)
    print(i*2)
print("end of first")
# sum of first five natural numbers 1+2+3+4+5
numsum=0
for num in range(1,6):
    #print(num)
    numsum=numsum+num
print(numsum)

num2=0
for num in range(1,10,2):############step of 2 - 1+3+5+7+9
    #print(num)
    num2=num2+num
print(num2)

for num in range(1,12,5):############step of 5 - 1,6,11
    print(num)

for num in range(9):############print 0-8
    print(num)
