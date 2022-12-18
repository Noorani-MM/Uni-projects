def maximum(*numbers):
    max = numbers[0]
    print("list: ", end="")

    for number in numbers:
        if number > max:
            max = number
        print(number,end=" ")
    
    return max


max = maximum(1,2,3,5)
print(" => {0} is maximum in list".format(max))
max = maximum(25,3,8,1,7,1,76,36,85)
print(" => {0} is maximum in list".format(max))
max = maximum(14,202,142,585,196)
print(" => {0} is maximum in list".format(max))
max = maximum(33,69,47,1,25,44)
print(" => {0} is maximum in list".format(max))