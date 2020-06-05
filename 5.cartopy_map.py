import pandas as pd 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 
import matplotlib.pyplot as plt 

birddata = pd.read_csv("bird_tracking.csv") 
bird_names = pd.unique(birddata.bird_name) 

# To move forward, we need to specify a 
# specific projection that we're interested 
# in using. 
proj = ccrs.Mercator() 

plt.figure(figsize=(10,10)) 
ax = plt.axes(projection=proj) 
ax.set_extent((-25.0, 20.0, 52.0, 10.0)) 
ax.add_feature(cfeature.LAND) 
ax.add_feature(cfeature.OCEAN) 
ax.add_feature(cfeature.COASTLINE) 
ax.add_feature(cfeature.BORDERS, linestyle=':') 
for name in bird_names: 
	ix = birddata['bird_name'] == name 
	x,y = birddata.longitude[ix], birddata.latitude[ix] 
	ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name) 
plt.legend(loc="upper left") 
plt.show() 
