def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)

def fibonacci(number):

    if number == 0:
        return 0
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)

def factorial(n):
    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
