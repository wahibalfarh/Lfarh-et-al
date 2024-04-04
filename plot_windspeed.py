#####################################################################
#                      IMPORT LIBRAIRIES                            #
#####################################################################
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib import colors
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd


########### Read Data ###########

### dx = 200m
ncfile200= xr.open_dataset("/gpfs/work/p20024/lfarh/ADRIA/DIAG2D/ADRIA.2.SEG04.002DIA2D.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
### dx = 1000m
ncfile1000= xr.open_dataset("/tmpdir/lfarh/COARE/DIAG/COARE.1.SEG01.014DIA.nc", mask_and_scale=True, decode_times=True, decode_coords=True)

 
######## Read variables ##########
time_model = ncfile1000.coords['time']
#MSLP = ncfile1000.data_vars['MSLP'][0,:,:]
LON = ncfile1000.data_vars['LON']
LAT = ncfile1000.data_vars['LAT']
ZS =  ncfile1000.data_vars['ZS'] 
XHAT = ncfile1000.data_vars['XHAT']
YHAT = ncfile1000.data_vars['YHAT']

########   Read and compute wind speed ####### 
U = ncfile1000.data_vars['UM10']
V = ncfile1000.data_vars['VM10']
WIND = np.sqrt( U**2 + V**2 )

### Assign coordinates
for field in ZS, WIND:
    field.coords['ni'] = ZS.coords['longitude'][0,:].values
    field.coords['nj'] = ZS.coords['latitude'][:,0].values

########Figure########
fig = plt.figure()
ax = plt.axes()

windspeed = plt.contourf(LON,LAT,WIND[0,:,:], cmap='Spectral_r', levels=range(0,42,1) )
ZS.plot.contourf(cmap='terrain',levels=[0,10,20,50,100,200,500,1000,2000])
MSLP.where(ZS==0).plot.contour(colors='dimgrey', levels=range(950,1050,2) )

### Add wind vectors/barbs
interval_x = int( WIND['ni'].size / 10 )
interval_y = int( WIND['nj'].size / 10 )
#ax.quiver( WIND['ni'][1:-1:interval_x], WIND['nj'][1:-1:interval_y], U[0,1:-1:interval_y,1:-1:interval_x], V[0,1:-1:interval_y,1:-1:interval_x], color=('green'))

### Domain on land
rect = patches.Rectangle((2.05, 38.05), 8.92, 6.7, linewidth=3, edgecolor='black', facecolor='none')
### Domain sea
rect2 = patches.Rectangle((4.89, 39.7),4.78 ,3.6,  linewidth=3, edgecolor='black', facecolor='none')
ax.add_patch(rect)
ax.add_patch(rect2)

plt.text(5, 42.95, 'D2', fontsize=16, color='black')
plt.text(2.1, 44.4, 'D1', fontsize=16, color='black')

plt.title('')
plt.xlabel('Longitude',fontsize=12)
plt.ylabel('Latitude', fontsize = 12)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.savefig('10m-Windspeed_1530_dx1000-200.png')

