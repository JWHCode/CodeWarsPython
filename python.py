# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
    total = 0
    for x in range(num):
        total += x+1 # range goes from 0 to num-1
    if total > 0:
        return total
    else:
        return 1

#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    returnString = ""
    for x in text:
        if str.isalpha(x):
            returnString += str(ord(x.lower())-96) + " "
        else:
            pass
    return returnString.strip()
