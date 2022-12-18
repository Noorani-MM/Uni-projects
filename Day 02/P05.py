a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

x1 = (-b + (b ** 2 - (4 * a * c) ** 0.5)) / (2*a)
x2 = (-b - (b ** 2 - (4 * a * c) ** 0.5)) / (2*a)

print("X1 = {0}, X2 = {1}".format(x1, x2))