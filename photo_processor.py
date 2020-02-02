import numpy as np
import matplotlib.pyplot as plt

#variable initialization
width, height = (5,8)

#resistance and conductance data array initialization
resistance  = [[0 for i in range(width)] for j in range(height)]
conductance = [[0 for i in range(width)] for j in range(height)]
maxresistance, maxconductance = (0.0,0.0)
f_q = [[0 for i in range(width)] for j in range(height)]
f_q_conductance = [[0 for i in range(width)] for j in range(height)]

#asks user for resistance input from a photoresistor pointed at their image
for i in range(height):
    for j in range(width):
        resistance[i][j] =  input()
        while((resistance[i][j]) == ""):
            print("try again")
            resistance[i][j] = input()
        #casts resistance values to int and calculates the conductance
        resistance[i][j] = int(resistance[i][j])
        conductance[i][j] = 1/resistance[i][j]
        maxresistance = max(maxresistance, resistance[i][j])
        maxconductance = max(maxconductance, conductance[i][j])
        
#normalizes resistance and conductance to 255
for i in range(height):
    for j in range(width):
        resistance[i][j] = resistance[i][j] * 255 / maxresistance
        conductance[i][j] = conductance[i][j] * 255 / maxconductance

f_q = np.around(resistance)
f_q_conductance = np.around(conductance)

#displays resistance and conductance images
plt.imshow(f_q, 'gray')
plt.show()
plt.imshow(f_q_conductance, 'gray')
plt.show()
