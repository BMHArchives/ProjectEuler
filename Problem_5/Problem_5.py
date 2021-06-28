# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def FindTheSmallestPostiveNumberThatIsEvenlyDivisibleByAllTheNumbersFromOneToTwenty():
    
    found = False
    # use the number from 1 to 10 and increment this number unitl we found the correct answer.
    i = 2520 
    isDivisable = True
    while found == False:
          i += 2520
          isDivisable = True
          for a in range(11,21): # we start at 11 since we know the answer from 1 to 10.
              if(i%a != 0):
                 isDivisable = False
                 break
          if (isDivisable == True):
              found = True
    
    print("The smallest postive number that is evenly divisible by all numbers from 1 to 20 is: {}".format(i))

FindTheSmallestPostiveNumberThatIsEvenlyDivisibleByAllTheNumbersFromOneToTwenty()