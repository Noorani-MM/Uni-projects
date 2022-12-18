week = ["Saturday", "Sunday","Moonday","Tuesday","Wednesday","Thursday","Friday"]

day = int(input("Enter day number: "))

if day > 7 or day < 1 :
    print("Chose one invalid !")
else:
    print(week[day - 1])