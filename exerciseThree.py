myList = ['a', 'b', 'a', 'c', 'd', 'a', 'd', 'z']

elementsInList = len(myList)
print(elementsInList) #Elements in list print


print(myList.count('d')) #Finds the index of the first 'd' in the array


myList.insert(4, 'a')
print(myList, "\n")  #Adds another 'a' in front of the 'c'

#Import counter
from collections import Counter
print(Counter(myList), "\n")

index = 0
while(index <= elementsInList):
    print(myList[index])
    index += 1
