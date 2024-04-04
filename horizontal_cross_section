#####################################################################
#                      IMPORT LIBRAIRIES                            #
#####################################################################
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import sys
import wrf


### cross-section height in meters
height = 200

### Domain on interest 
left = 8.3
bottom = 41.62
right = 8.56
top = 41.8

### Location of the vertical section
lon_start =  8.38
lat_start = 41.758
lon_end = 8.55
lat_end = 41.68

#########################################
###     Read Meso-NH data at 1530     ###
#########################################

#ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/COARE/ADRIA.2.SEG04.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NDREA/NDREA.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/ECUME/ECUME.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/WASP/WASP2.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOSEN/NOSEN.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile  = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOLAT/NOLAT.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOMOM/NOMOM.2.SEG02.001DIA3D.nc", mask_and_scale=True, decode_times=True)
#ncfile= xr.open_dataset("/gpfs/work/p20024/lfarh/ADRIA/ADRIA.2.SEG04.001DIA3D.nc", mask_and_scale=True, decode_times=True, decode_coords=True)

### Read coordinates
time = ncfile.coords['time']
longitude = ncfile.coords['longitude'][0,:].values
latitude = ncfile.coords['latitude'][:,0].values

### Define zoom
x0 = np.searchsorted( longitude, left )
x1 = np.searchsorted( longitude, right )
y0 = np.searchsorted( latitude, bottom )
y1 = np.searchsorted( latitude, top )

### Read varible of interest
VAR = ncfile.data_vars['MRC'][0,:,y0:y1,x0:x1]


###  Read and compute wind speed
U = ncfile.data_vars['UT'][0,:,y0:y1,x0:x1]
V = ncfile.data_vars['VT'][0,:,y0:y1,x0:x1]
WIND = np.sqrt( U.values**2 + V.values**2 )

### Coordinates
U.coords['ni_u'] = U.coords['longitude_u'][0,:].values
U.coords['nj_u'] = U.coords['latitude_u'][:,0].values

V.coords['ni_v'] = V.coords['longitude_v'][0,:].values
V.coords['nj_v'] = V.coords['latitude_v'][:,0].values

### Read orography
#ZS =  ncfile.data_vars['ZS'][y0:y1,x0:x1]

### read altitude
ALT =  Rcfile.data_vars['ALT'][:,y0:y1,x0:x1]

### assign coordinates
for field in ALT,VAR:
    field.coords['ni'] = longitude[x0:x1]
    field.coords['nj'] = latitude[y0:y1]

###################################
###    Compute cross-section    ###
###################################

### interpolate
VAR_section = wrf.interplevel( field3d=VAR, vert=ALT, desiredlev=height )
WIND_section = wrf.interplevel( field3d=WIND, vert=ALT, desiredlev=height_wind )

### assign coordinates
WIND_section['dim_1'] = VAR_section['nj'].values
WIND_section['dim_2'] = VAR_section['ni'].values
WIND_section.name = 'Wind speed ($m.s^{-1}$)'

#################################
###        Plot figure        ###
#################################

### open figure
plt.figure()
ax = plt.axes()

def CustomColormap(Name = 'default'):
   if Name == 'test':
       ChoosedBlue =  'lightblue'
       CustCmap = colors.LinearSegmentedColormap.from_list('',
                                                     ['lightgrey',
                                                      ChoosedBlue,
                                                      ChoosedBlue,
                                                      ChoosedBlue,
                                                      'lightskyblue',
                                                      'lightskyblue',
                                                      'khaki',
                                                      'khaki',
                                                      'gold',
                                                      'blueviolet',
                                                      'blueviolet',
                                                      'rebeccapurple',
                                                      'rebeccapurple'
                                                         ])   




       my_cmap = CustCmap(np.arange(CustCmap.N))
       my_cmap[:, -1] = np.linspace(0.3, 1, CustCmap.N)
       CustCmap = ListedColormap(my_cmap)


   return CustCmap


CustCmap = CustomColormap('test')

### Plot surfaces
WIND_section.plot.contourf( cmap = CustCmap, levels=np.arange(20,65,0.5))

### Add orography
ZS[1:-1,1:-1].plot.contour( colors="black",levels=[0])

### Location of the vertical section
plt.plot( [lon_start,lon_end], [lat_start,lat_end], linewidth=2, color='black' )

### Add wind vectors
vecteurs = ax.quiver(U['ni_u'][20:150:30], U['nj_u'][20:150:30], U[0,20:150:30,20:150:30], V[0,20:150:30,20:150:30], color='crimson',scale =200)

		
plt.legend(title='NoM',loc=2)
plt.savefig('CH_Nommf_WIND_1530.pdf')

