num = input("Enter a two digit number!")

def myfirstfunction(number):
    num_to_str = str(number)
    if(len(num_to_str) > 2):
        print("the given number contains more than 2 digits!")
    else :
        res = int(num_to_str[0]) + int(num_to_str[1])
        print(f'res is: {res}')

myfirstfunction(num)
