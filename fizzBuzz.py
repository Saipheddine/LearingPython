# FizzBuzz Problem

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz\n")
    elif (i % 3 == 0):
        print("Fizz\n")
    elif (i % 5 == 0):
        print("Buzz\n")
    else:
        print("{}\n".format(i))        
