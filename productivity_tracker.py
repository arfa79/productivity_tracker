import matplotlib.pyplot as plt
#file = open("note.txt",)
# new idea !! connect the git api to app
hours=[6,7,6,6,7,6,4.5,6,7,5,2,2,6,6]

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

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

