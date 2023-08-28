from matplotlib import pyplot as plt
import os 

x_values = [1, 2, 3, 4, 5, 6, 7]

y_values = [60, 80, 61, 73, 58, 100, 84]

fig, ax = plt.subplots(nrows=1, ncols=1)
fig = plt.figure()
fig.set_facecolor('#386061')  
plt.xlabel('days')
plt.ylabel('Weight')
plt.bar(x_values, y_values, color= '#61735e', alpha=1) 
plt.grid(axis='y', linestyle='--') 



plt.savefig('fitnessApp\kivy_gui\images\plot.png')
plt.show()