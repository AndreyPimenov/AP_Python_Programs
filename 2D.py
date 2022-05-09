# This project is related to spectra interpretation for my thesis:
# 1. Read 1st column from the txt file
# 2. Read 2nd column from the txt file
# 3. Build the graph
# 4. Split this grpah in period for 400 sm-1
# 5. demonstrate this

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

#Array of Raman Spectroscopy
Axis_x, Axis_y, Density, Energy, Num_eqn = np.array([]), np.array([]),np.array([]),np.array([]),np.array([])

# Preparation function to read the files:
way = 'C:/Users/andrey.pimenov/Desktop/AP_KWORK/FILES/'
len = 25600
# data_init = 9

with open(way + 'fort.q0000') as f1:
    for i in range(9):
        f1.readline()

    for line in range (9, (len + 9), 1):
        STR = f1.readline()

        if (STR == ("\n" or '')):
            STR = f1.readline()

        Axis_x = np.append(Axis_x, STR[6:18])
        Axis_y = np.append(Axis_y, STR[22:37])
        Density = np.append(Density, STR[39:55])
        Energy = np.append(Energy, STR[60:71])
        Num_eqn = np.append(Num_eqn, STR[78:90])



plt.figure(figsize=(15,60), dpi= 80)
plt.title("Density" ) #+ str(set) + '-' + str(seria))
#plt.plot(Axis_y, Density)

plt.xlabel("X axis")
plt.ylabel("Y axis")
#plt.imshow(Density)

for i in range(len):
    if float(Density[i]) > 0:
        plt.scatter(Axis_y[i],Axis_x[i])


# # detrending the signal:
#x_detrend = signal.deconvolve(Axis_x)
#y_detrend = signal.deconcolve(Axis_y)
# x_detrend = signal.detrend(ARS_x)
# y_detrend = signal.detrend(ARS_y)

# n = 256
# u = np.linspace(0, 1, n)
# x, y = np.meshgrid(u, u)
# z = np.zeros((n, n, 3))
# z[:, :, 0] = x
# z[:, :, 2] = y

# plt.figure()
# plt.imshow(Density)
# plt.show()


plt.show()
