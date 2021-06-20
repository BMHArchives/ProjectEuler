# Multiples of 3 and 5
#---------------------
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
numberCount = 1000
total = 0
for count in range(1,numberCount):
    if count != 0:
       if (count % 3) == 0 or (count % 5) == 0:
           total += count
       
print("Answer: {}".format(total))
