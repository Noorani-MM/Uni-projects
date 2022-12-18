def timer(number):
    if number == 1:
        return 1
    print(number)
    return timer(number - 1)

number = int(input("Enter number : "))
print(timer(number))