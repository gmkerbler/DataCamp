#!/bin/env/python3
#import matplotlib.pyplot for making plots 
import matplotlib.pyplot as plt

#Create random list of counts
counts = [1, 1, 3, 4, 5, 6, 7, 6, 8, 11, 16, 1, 17, 17, 15, 19]

#plot a histogram to view data distribution, change bins to 15 (default is 10)
plt.hist(counts, bins = 15)

plt.title("Histogram to look at distribution of data")

plt.show()
