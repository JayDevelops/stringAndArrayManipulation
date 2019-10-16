fox = "A Red Fox"
chasedBird = " chased a Blue bird"
greenMeadow = " across a Green meadow."

print(fox, chasedBird, greenMeadow, "\n")


wholeSentence = fox + chasedBird + greenMeadow #String Contantonation
print(wholeSentence)
print(wholeSentence.lower()) #lowercases the entire string
print(wholeSentence.upper()) #UPPERCASES THE ENTIRE STRING

#Prints out the letters R, B, and G
print(wholeSentence[2])
print(wholeSentence[19])
print(wholeSentence[24])
print(wholeSentence[38], "\n")

#Prints out the character length, including the spaces, in the string
print(len(wholeSentence), "\n")

#Prints out substrings of Red, Green, and blue

print(wholeSentence[2:5])
print(wholeSentence[19:23])
print(wholeSentence[38:43])
