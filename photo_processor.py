import numpy as np
import matplotlib.pyplot as plt

width, height = (2,2)
resistance  = [[None for i in range(2)] for j in range(2)]
maxresistance = 0.0
f_q = [[None for i in range(2)] for j in range(2)]

for i in range(height):
    for j in range(width):
        resistance[i][j] =  input()
        while((resistance[i][j]) == ""):
            print("try again")
            resistance[i][j] = input()
        resistance[i][j] = int(resistance[i][j])
        maxresistance = max(maxresistance, resistance[i][j])
        
for i in range(height):
    for j in range(width):
        resistance[i][j] = resistance[i][j] * 255 / maxresistance

f_q = np.around(resistance)
print(resistance)
print(f_q)

plt.imshow(f_q, 'gray')
plt.show()