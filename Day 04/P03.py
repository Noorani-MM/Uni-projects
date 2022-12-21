import numpy as np

matris = np.array([[0] * 5] * 3)

for row in range(3):
    for cell in range(5):
        print(matris[row])
        matris[row][cell] = int(input("Enter a number for matris: "))
    
    print(matris[row])

print(matris.T)