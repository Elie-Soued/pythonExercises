#  Write a function FizzBuzz that takes a variable n and for every number i from 1 to n, print:
#  "fizz" if i is a multiple of 3
#  "buzz" if i is a multiple of 5
#  "fizzbuzz" if i is a multiple of 15
#   i in any other case
#   Bonus make FizzBuzz recursive


def fizzbuzz(n):
    if(n == 0):
        return
    if(n % 15 == 0):
        print("Fizzbuzz")
    elif(n % 5 == 0):
        print("Fizz")
    elif( n % 3 == 0):
        print("Buzz")
    else:
        print(n)
    
    return fizzbuzz(n-1)



fizzbuzz(100)
