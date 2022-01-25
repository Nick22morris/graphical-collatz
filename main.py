import numpy as np
import matplotlib.pyplot as plt
 
num = 27
og = num
cors = []
cors.append(num)
print(num)
while num!=1:
	check = num%2
	
	if check == 1:
		num = (num*3)+1
	else:
		num = num/2
	print(num)
	cors.append(num)
print("done")

length = len(cors)
# data to be plotted
x = np.arange(0, length)
y = np.array(cors)
# plotting
title = "3x+1 Problem with "
plt.title(title + str(og))
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="green")
plt.show()
