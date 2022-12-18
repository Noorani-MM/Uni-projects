def is_multiple(multiple, number):
    return number % multiple == 0

for i in range(3):
    number = int(input("Enter a number : "))
    multiple = int(input("Enter a multiple : "))
    sequence = "=" if is_multiple(multiple, number) else "!="
    print("{0} * x {1} {2}".format(multiple, sequence, number))