import pandas as pd 
import matplotlib.pyplot as plt 
import datetime 
import numpy as np 

birddata = pd.read_csv("bird_tracking.csv") 
bird_names = pd.unique(birddata.bird_name) 

timestamps = [] 
for k in range(len(birddata)): 
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S")) 

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index) 

times = birddata.timestamp[birddata.bird_name == "Eric"] 
elapsed_time = [time-times[0] for time in times] 

plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1)) 
plt.xlabel(" Observation ") 
plt.ylabel(" Elapsed time (days) ") 
plt.show() 
