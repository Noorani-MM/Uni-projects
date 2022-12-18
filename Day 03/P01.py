def maximum(num1, num2, num3):
    max = num1
    if max < num2:
        max = num2
    if max < num3:
        max = num3
    return max


number_1 = int(input("Enter number 1: "))
number_2 = int(input("Enter number 2: "))
number_3 = int(input("Enter number 3: "))

print("Maximum of all the input numbers is {0}".format(maximum(number_1, number_2, number_3)))