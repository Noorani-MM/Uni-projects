numbers = [0] * 10 
counter = {}

for i in range(10):
    numbers[i] = int(input("Enter a number : "))

for number in numbers:
    if str(number) in counter.keys():
        counter["{0}".format(number)] = counter["{0}".format(number)] + 1
    else:
        counter["{0}".format(number)] = 1

max = 0
result = ""
for number in counter.keys():
    if max < counter[str(number)]:
        result = "Number : {0} , Count : {1}".format(number,counter[str(number)])
        max = counter[str(number)]

print(result)
