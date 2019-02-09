'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_of_natural_multiples_of_three_or_five():
    sum = 0 # running sum
    qualified_numbers = [x for x in range(1000) if x % 5  == 0 or x % 3 == 0]
    for num in qualified_numbers:
        sum += num
    return sum

