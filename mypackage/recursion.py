def sum_array(array):

    '''Return sum of all items in array'''
    return sum(array)

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
    return a

def factorial(n):
    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    return word[::-1]
