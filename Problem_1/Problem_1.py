# Multiples of 3 and 5
#---------------------
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
numberCount = 1000 # Use this number to find all multiples under the numberCount
total = 0 # summerize the total count of multiples under 1000
# loop between 1 and 1000
for count in range(1,numberCount):
    if count != 0: # can't divide by 0
       # if the % value is equal to 0 for 3 or 5, then add it to the total.
       if (count % 3) == 0 or (count % 5) == 0:
           total += count

#def FindAllMultiplesOfTragetNumber(TargetNumber):
#    sumTotal = 0 
#    for a in range(1,numberCount):
#        if(a % TargetNumber) == 0:
#           sumTotal += a
#    return sumTotal
# We're using 3, 5 and 15 here because 15 is the lowest common denominator between 3 and 5, so we will add 3 + 5 to 8 and then subtract from 15 to get the value.
#print(FindAllMultiplesOfTragetNumber(3) + FindAllMultiplesOfTragetNumber(5) - FindAllMultiplesOfTragetNumber(15))
print("Answer: {}".format(total))
