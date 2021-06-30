# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

def IsPrimeNumber(num):
    # define a flag variable
    isPrimeNumber = True

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                isPrimeNumber = False
                # break out of loop
                break
    else:
        isPrimeNumber = False
    return isPrimeNumber
nthPrimeNumber = 10002
primeNumberFound = False
counter = 1
realNumber = 1
primeNumbers = []
while primeNumberFound == False:
      if(IsPrimeNumber(realNumber) == True):
         primeNumbers.append(realNumber)
         counter += 1
      
      realNumber += 1
      if counter == nthPrimeNumber:
         primeNumberFound = True
         print("10,001th prime number is {}".format(primeNumbers[-1]))
         break

         
