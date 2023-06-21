import itslive
import json
import matplotlib.pyplot as plt

# fetching the data usiing the itslive python package
list_of_timeseries = itslive.cubes.get_time_series(points=[(-43.37,60.1166)],variables = [ 'v', 'date_dt']) 
response_for_first_point = list_of_timeseries[0]

# list of dates (x axis)
midDateList = response_for_first_point['time_series']['date_dt']['mid_date'].data

# list of velocities (y axis)
vList = response_for_first_point['time_series']['v'].data

# plotting the data using matplotlib
fig, ax = plt.subplots()
ax.scatter(midDateList, vList)
ax.set_xlabel('date', fontsize=15)
ax.set_ylabel('speed (m/year)', fontsize=15)
ax.set_title('ITS_LIVE Ice Flow Speed m/yr', fontsize=20)

# plt.show()

# if you want to save the plot as a png file
plt.savefig('plot.png')