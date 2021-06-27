# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
def FindLargestPalindromeMadeByThreeDigitNumber():
    results = []
    for a in range(100,1000):
        for b in range(100,1000):
            product = a * b 
            productReverse = str(product)[::-1]
            if str(product) == productReverse:
               results.append(product)

    print("The largest palindrome made from the product of two 3-digit numbers is: {}".format(max(results)))

FindLargestPalindromeMadeByThreeDigitNumber()
