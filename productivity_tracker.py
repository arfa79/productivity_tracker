import matplotlib.pyplot as plt
#file = open("note.txt",)
# new idea !! connect the git api to app
hours=[6,7,6,6,7,6,4.5,6,7,5,2,2,6,6,2,8,5,3,7,3,8,6,5,5,6,6,8,7,4,1,7,4,4,6,3,5,6,6]

days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]

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

