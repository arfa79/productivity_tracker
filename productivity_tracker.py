import matplotlib.pyplot as plt
#file = open("note.txt",)

hours=[6,7,6,6]

days=[1,2,3,4]

plt.plot(days ,hours)

# naming the x axis
plt.xlabel('days')
# naming the y axis
plt.ylabel('hours')
  
# giving a title to my graph
plt.title('productivity tracker')
  
# function to show the plot
plt.show()

#file.close()

