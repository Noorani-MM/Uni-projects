count = 0

for i in range(10):
    number = int(input("Enter a number {0}: ".format((i + 1))))

    count = count + 1 if number % 4 == 0 else count

print("Count of number which divide by 4 is equal 0: ", count)