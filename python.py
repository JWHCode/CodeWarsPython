# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
    total = 0
    for x in range(num):
        total += x+1 # range goes from 0 to num-1
    if total > 0:
        return total
    else:
        return 1
