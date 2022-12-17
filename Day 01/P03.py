clock = input("Enter clock (example => 2:25:33) : ")

splited = clock.split(":")

hour = int(splited[0])
minute = int(splited[1])
secound = int(splited[2])

result = (hour * 3600) + (minute * 60) + secound

print("Your clock into secound is {0}".format(result))