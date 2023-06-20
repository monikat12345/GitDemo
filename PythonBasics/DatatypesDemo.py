values = [2, 3, "Thursday", 4.5, 10] #this is a list

print(values[0])

print(values[2])

print(values[-1])  ## last index of list

print(values[1:3]) #index at place 3 will be excluded

values.insert(4, "Friday")
print(values)
values.append("end") ##appends at the end
print(values)
values[2] = "newday" ##updated value of second item
print(values)
del values[0]##delete item from 0th index
print(values)

########################tuple - value of list can not be updated
tvalues = (5, 7, "newT", 7.8,  20)
print(tvalues[2])

#tvalues[1] = 9 #TypeError: 'tuple' object does not support item assignment

print(tvalues)

#dictionary - key value pair

dvalues = {1:"first", 2: "second", "Third":3}
print(dvalues["Third"])
print(dvalues[1])

####ceeate dictionary at run time

rundict = {}
rundict["firstname"] = "GOOD"
rundict["lastname"] = "DAY"
print(rundict)
print(rundict["firstname"])
