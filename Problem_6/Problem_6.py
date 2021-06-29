# Sum square difference
# The sum of the squares of the first ten natural numbers is, 385 - 1^2+2^2+....10^2 = 385
# The square of the sum of the first ten natural numbers is, 3025 - 1+2+3.....+10)^2 == 55^2 = 3025
# Hence the difference between the sum of the squares of the first 
# ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Generate a list of numbers from 1 to 100.
limitNumber = 100
natualNumbers = list(range(1,limitNumber + 1))

# loop throug the natualNumbers list and take the power of each number and then sum up the answers.
sumOfSquares = 0
squareOfSums = 0
squareOfSumsTotal = 0
for a in natualNumbers:
    sumOfSquares += a**2
    squareOfSumsTotal += a
    
squareOfSums = squareOfSumsTotal**2
print("The sum of squares for all natual numbers between 1 and {} is {}".format(limitNumber, sumOfSquares))
print("The square of sum for all natual numbers between 1 and {} is {}".format(limitNumber, (squareOfSums)))
print("The difference between the square of sum and sum of squares is {} - {} = {}".format(squareOfSums, sumOfSquares, (squareOfSums - sumOfSquares)))


