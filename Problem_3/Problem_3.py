# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Function to determine prime numbers and to find the prime factor of a value.

factors = []
def IsPrimeNumber(value):
    for a in range(2,value):
        if(value % a) == 0:
           return False
    return True

def MultipleList(list):
    result = 1
    for x in list:
         result = result * x
    return result
def IsFactorListMatchTheTargetNumber(Factors, TargetNumber):
    total = 0
    for a in Factors:
        print(a)
        print(total)
        if(total == 0):
           total = TargetNumber / a
           print("{} - {}".format(a, total))
        else:
           total = total / a
           print("{} - {}".format(a, total))
    print(total)
    if (total == 1):
        return True
    else:
        return False
def DoesFactorsMultipleToTargetValue(factorList, targetValue):
    result = MultipleList(factorList)
    print("Result: {} == Target Value: {}".format(result, targetValue))
    if(result == targetValue):
       return True
    else:
        return False
    
def FindLargetsPrimeFactorForNumber(LargestPrimeFactorNumber):
    counter = 5

    while True:
          if(IsPrimeNumber(counter) == True and counter != 1):
             factors.append(counter)
          elif (counter == 1):
                factors.append(counter)
          counter += 1

          if IsFactorListMatchTheTargetNumber(factors, LargestPrimeFactorNumber) == True:
             break

          
          #results = MultipleList(factors)
          #if results > LargestPrimeFactorNumber:
             #return []

          #if DoesFactorsMultipleToTargetValue(factors, LargestPrimeFactorNumber) == True:
          #   break
    return factors
#list = [5, 7, 13,29]
#print(IsFactorListMatchTheTargetNumber(list,13195))
#print(MultipleList(list))
LargestPrimeFactorNumber = 600851475143
answer = FindLargetsPrimeFactorForNumber(LargestPrimeFactorNumber)

print(answer)

           
