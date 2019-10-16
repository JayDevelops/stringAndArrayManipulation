myArray = [3, 6, 4, 7, 2, 17, 4, 9]

print(myArray[3])
myArray.append(8)

print(myArray[8])

myArray.insert(2, 33) #adds a 33 in front of the second "2" position
print(myArray)


myArray.sort() #sorts the array in order, according to the data object value
print(myArray)


myArray.pop() #takes out the last array object
myArray.pop() #takes out the last array object
myArray.pop() #takes out the last array object
print(myArray)


#now we add the numbers inside the array
index = 1
while(index <= len(myArray)):
    print(myArray[index - 1])
    index += 1
