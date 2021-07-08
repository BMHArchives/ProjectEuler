
def FindSumOfPrimeNumbersByTargetNumber(TargetNumber):
    multiples = set()

    for i in range(2, TargetNumber+1):
        if(i not in multiples):
           yield i
           multiples.update(range(i*i, TargetNumber+1, i))

iter = 0
targetNumber = 2000000
ml = list(FindSumOfPrimeNumbersByTargetNumber(targetNumber))
for x in ml:
    iter = int(x) + iter

print('The sum of all the primes below two million is {}'.format(iter))
              