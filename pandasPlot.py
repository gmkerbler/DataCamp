#import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#load data as a pandas dataframe
df = pd.DataFrame(pd.read_csv('**ADD RELEVANT FILE NAME HERE**'))

# Plot all columns (default)
df.plot()
plt.show()
plt.clf()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()
plt.clf()

# Plot just the Dew Point data
column_list1 = ["Dew Point (deg F)"]
df[column_list1].plot()
plt.show()
plt.clf()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()

