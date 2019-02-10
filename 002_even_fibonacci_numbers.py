def sum_even_fib_numbers_less_than_equal_to_four_mil():
    firstNum = 1
    secondNum = 2
    sum = firstNum + secondNum
    numbers = [firstNum, secondNum, sum]
    while sum < 4000000 :
        firstNum = secondNum
        secondNum = sum
        sum = firstNum + secondNum
        numbers.append(sum)
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

