def is_palindrome(st):
    return str(st) == str(st)[::-1]

def lp3():
    largest = None
    for i in range(900,1000):
        for j in range(900, 1000):
            product = i*j
            if is_palindrome(product) and largest < product:
                largest = product
    return largest