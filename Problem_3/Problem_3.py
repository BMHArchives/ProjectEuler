# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


from functools import reduce
import math
factors = []
# Function to determine prime numbers and to find the prime factor of a value.
def FindLargetsPrimeFactorsForTargetNumber(TargetNumber):
    largestFactorNumber = 2
    factors = []
    # Start the process to determining the largets factor number
    while largestFactorNumber > 1:
          # if the remainder value from dividing the target number 
          # from the currentfactor number equals 0, then divided 
          # the target number by the current factor number saved
          # it back to its original variable.
          if TargetNumber % largestFactorNumber == 0:
             TargetNumber = int(TargetNumber / largestFactorNumber)
          else:
              # Update the largest factor number variable
              largestFactorNumber += 1

          # if the target number equals to 0, then return
          # the factor number back to the client.
          if(TargetNumber == 1):
             return largestFactorNumber


TestNumber = 600851475143
answer = FindLargetsPrimeFactorsForTargetNumber(TestNumber)
print("The largets prime factor for the number {} is {}".format(TestNumber, answer))

           
