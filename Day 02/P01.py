number = int(input("Enter a number (0 to exit): "))
result = 0

while number != 0:
    cube = number ** 3
    print ("{0} ^ 3 = {1}".format(number, cube))
    result += cube
    number = int(input("Enter a number (0 to exit): "))

print("Result is {0}".format(result))