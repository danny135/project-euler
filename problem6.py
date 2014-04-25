def sq(n):
    sum_square = 0
    square_sum = 0

    numbers = range(1, n+1)
    for i in numbers:
        sum_square += i*i

    for i in numbers:
        square_sum += i
    square_sum *= square_sum
    return sum_square - square_sum

print sq(100)
