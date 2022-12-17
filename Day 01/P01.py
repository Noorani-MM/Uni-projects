result = 0

for i in range(3):
    number = int(input("Enter number {0}: ".format((i+1))))
    cube = number ** 3
    print("{0} is {1}".format(number, cube))
    result += cube

print("Result is : ", result)