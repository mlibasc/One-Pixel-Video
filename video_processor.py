import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#variable initialization 
width = 5
height = 3
frame = 50
#index of photoresistor array
idx = 0 
i = 0

# resistance and conductance data array initialization
video_res = [[[0 for k in range(width)] for j in range(height)] for i in range(frame)]
video_con = [[[0 for k in range(width)] for j in range(height)] for i in range(frame)]

#function for animating through each frame
def updatefig(*args):
    global i
    if(i < frame-1):
        i += 1
    else:
        i = 0
    im.set_array(video_con[i])
    return im,

#grabbing photoresistor values from csv file and storing into a data array
#possible animation files to run (1st iteration to last): stick_man_waving.csv, stick_man_waving_detailed.csv, arm_wave.csv
with open('arm_wave.csv', newline='\n') as csvfile:
    data = list(csv.reader(csvfile))

#reorganization of data into an array of frames
for i in range(height):
    for j in range(width):
        for k in range(frame):
            video_res[k][i][j] = float(data[0][idx])
            video_con[k][i][j] = 1/float((data[0][idx]))
            idx += 1

#normalizing the data to 0 to 255 for each frame
for i in range(frame):
    maxcon = 0
    maxres = 0
    #finding max resistance values and max conductance values
    for j in range(width):
        for k in range(height):
            maxcon = max(maxcon, video_con[i][k][j])
            maxres = max(maxres, video_res[i][k][j])
    #normalizing resistance and conductance to 255 
    for j in range(height):
        for k in range(width):
            video_con[i][j][k] = video_con[i][j][k] * 255 / maxcon
            video_res[i][j][k] = video_res[i][j][k] * 255 / maxres

video_res = np.around(video_res)
video_con = np.around(video_con)

#setting up the animation
fig = plt.figure()
i = 0
im = plt.imshow(video_con[0], 'gray', animated=True)
#creating animation
ani = animation.FuncAnimation(fig, updatefig, blit=True)
plt.show()
