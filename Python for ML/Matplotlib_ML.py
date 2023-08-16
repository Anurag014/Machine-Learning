# Matplotlib - Use for making plots

import matplotlib.pyplot as plt
import numpy as np

# Using numpy library to get data for x, y, z

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# print(x)
# print(y)
# print(z)

# plt.plot(x,y)    # Plots the graph with x on x-axis and y on y-axis
# plt.show()       # Use to see graph

# plt.plot(x,z)    # Plots the graph with x on x-axis and z on y-axis
# plt.show()

# Adding title, x-axis and y-axis labels

'''plt.plot(x,z)
plt.xlabel('Angle')         # labels the x-axis
plt.ylabel('Cos value')     # labels the y-axis
plt.title('Cosine wave')    # Give title to graph
plt.show()'''

# Plotting parabola

x = np.linspace(-10, 10, 20)
y = x**2
'''plt.plot(x,y)
plt.show()'''

# Plotting same parabola using different symbols and color

'''plt.plot(x, y, 'r.')     # plot(x, y, 'r.') specifies red colour with . symbol
plt.show()'''

'''plt.plot(x, y, 'g*')        # here 'g*' specifies plot with green color and * symbol  
plt.show()'''

# Plotting muliple graph

'''x = np.linspace(-5, 5, 50)
plt.plot(x, np.sin(x), 'r.')
plt.plot(x, np.cos(x), 'g--')
plt.show()'''

                                    # Bar plot

fig = plt.figure()     # This creates the empty plot
ax = fig.add_axes([0, 0, 1, 1])    # As we have created empty figure we need to define
                                   # axes first two 0's define origin and two 1's define height and width
languages = ['English', 'French', 'Spanish', 'Latin', 'German']
people = [100, 50, 150, 40, 70]
ax.bar(languages, people)          # Plots the bar graph
plt.xlabel('LANGUAGES')
plt.ylabel('PEOPLES')
plt.show()

                                    # Pie chart

'''ax.pie(people, labels= languages, autopct= '%1.1f%%')   # autopct tells the floating point value to be taken with specified precision
plt.show()'''

                                    # Scatter plot

'''x = np.linspace(0, 10, 30)
y = np.sin(x)
z = np.cos(x)
ax.scatter(x, y, color = 'g')
ax.scatter(x, z, color = 'r')
plt.show()'''

                                    # 3d scatter plot

fig1 = plt.figure()
ax = plt.axes(projection = '3d')
z = 20 * np.random.random(100)
x = np.sin(z)
y = np.cos(z)
ax.scatter(x, y, z, c = z, cmap = 'Blues')
plt.show()