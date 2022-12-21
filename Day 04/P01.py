students = [0]*10


def SetStudentScore():
    global students
    for i in range(10):
        students[i] = int(input("Enter student {0} score: ".format((i+1))))

def getAvarage():
    sum = 0
    for studnet in students:
        sum += studnet
    
    avarage = sum / 10

    return avarage

def countLessThanAvarage():
    avarage = getAvarage()
    global students
    count = 0

    for student in students:
        if student < avarage:
            count += 1
    
    return count

while True: 
    print("Chose your option")

    chose = int(input(""" [1] Set student score
 [2] get avarage
 [3] count less than avarage
 [0] To exit
 Your choise : """))

    if chose == 1:
        SetStudentScore()
    elif chose == 2:
        avarage = getAvarage()
        print("The avarage of this class is: ", avarage)
    elif chose == 3:
        count = countLessThanAvarage()
        print("Count score which are less than avarage is: ", count)
    else:
        print("project close")
        break
    print()
    print()
    