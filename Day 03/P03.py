def gcd(number1, number2):
    list_number1 = []
    list_number2 = []

    for i in range(2, (number1 + 1)):
        if number1 % i == 0:
            list_number1.append(i)
        
    for i in range(2, (number2 + 1)):
        if number2 % i == 0:
            list_number2.append(i)
    
    common = list(set(list_number1).intersection(list_number2))

    if len(common) > 0:
        max = common[0]

        for number in common:
            if number > max:
                max = number
        
        return max
    
    return False


number_1 = int(input("Enter  number 1 : "))
number_2 = int(input("Enter  number 2 : "))

max = gcd(number_1, number_2)

if max:
    print("Maximum of divisor is ",max)
else:
    print("There is no divisor")
