#####################################################################
#                      IMPORT LIBRAIRIES                            #
#####################################################################
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import sys
import wrf

#####################################################################
#                      READ DATA AT 1530 UTC                        #
#####################################################################
### COARE3 ###
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/COARE/ADRIA.2.SEG04.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
#ncfile2D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/COARE/ADRIA.2.SEG04.002DIA2D.zoom.nc", mask_and_scale=True, decode_times=True)

### ANDREAS ###
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NDREA/NDREA.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)

### ECUME6 ###
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/ECUME/ECUME.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)

### WASP ###
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/WASP/WASP2.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)

### NoH ###
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOSEN/NOSEN.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)

### NoLE
#ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOLAT/NOLAT.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)

### NoM ###
ncfile3D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOMOM/NOMOM.2.SEG02.001DIA3D.nc", mask_and_scale=True, decode_times=True)
ncfile2D = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOMOM/NOMOM.2.SEG02.001DIA2D.nc", mask_and_scale=True, decode_times=True)

### location of the vertical section ###
lon_start =  8.38
lat_start = 41.758
lon_end = 8.55
lat_end = 41.68

### shorten cross-section
factor = 0.66
lon0 = (lon_start+lon_end)/2.
lat0 = (lat_start+lat_end)/2.
dlon = (lon_end-lon_start)/2.
dlat = (lat_end-lat_start)/2.
#lon_start = lon0 - factor*dlon
#lat_start = lat0 -factor*dlat
#lon_end = lon0 + factor*dlon
#lat_end = lat0 + factor*dlat

### read coordinates
longitude = ncfile3D.coords['longitude'][0,:].values
latitude = ncfile3D.coords['latitude'][:,0].values
time = ncfile3D.coords['time']
LON = ncfile3D.coords['longitude']
LAT = ncfile3D.coords['latitude']
XHAT = ncfile3D.data_vars['XHAT']
YHAT = ncfile3D.data_vars['YHAT']
ALT = ncfile3D.data_vars['ALT']

### define zoom
x0 = np.searchsorted( longitude, lon_start )
x1 = np.searchsorted( longitude, lon_end )
y0 = np.searchsorted( latitude, lat_start )
y1 = np.searchsorted( latitude, lat_end )

### read variables 
VAR = ncfile2D.data_vars['HBLTOP'][0,:,:]
MRC = ncfile3D.data_vars['MRC'][0,:,:,:]
WT = ncfile3D.data_vars['WT'][0,:,:,:]
### compute wind speed
U = ncfile3D.data_vars['UT'][0,:,:,:]
V = ncfile3D.data_vars['VT'][0,:,:,:]
WIND = np.sqrt( U.values**2 + V.values**2 )

### compute wind components tangent and normal to the cross-section
#delta_x = x1 - x0
#delta_y = y1 - y0
#delta_xy = (delta_x**2 + delta_y**2)**0.5
#n_x = delta_x/delta_xy
#n_y = delta_y/delta_xy
### or define tangent and normal directions manually
angle = 58 ### wind direction
#angle = 49 ### rolls direction
n_x = np.cos(np.deg2rad(angle-90.))
n_y = np.sin(np.deg2rad(angle-90.))
wind_tangent = U.values * n_x + V.values * n_y
wind_normal = V.values * n_x - U.values * n_y

### define vertical levels
height_min = 0   # in m
height_max = 1600  # in m
height_interval = 50   # in m
height = np.linspace( height_min, height_max, height_interval )

### interpolate 3D
WIND_section = wrf.vertcross( field3d=WIND, vert=ALT.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1), levels=height )
WT_section = wrf.vertcross( field3d=WT.values, vert=ALT.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1), levels=height )
MRC_section = wrf.vertcross( field3d=MRC.values, vert=ALT.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1), levels=height )
wind_tangent_section = wrf.vertcross( field3d=wind_tangent, vert=ALT.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1), levels=height )
wind_normal_section = wrf.vertcross( field3d=wind_normal, vert=ALT.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1), levels=height )

### interpolate 2D
LON_section = wrf.interpline( field2d=LON.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1) )
VAR_section = wrf.interpline( field2d=VAR.values, start_point=wrf.CoordPair(x0,y0), end_point=wrf.CoordPair(x1,y1) )

### assign coordinates
distance_max = np.sqrt( (XHAT[x1]-XHAT[x0])**2 + (YHAT[y1]-YHAT[y0])**2 ) * 1.e-3   # in km
distance = np.linspace( 0, distance_max, WIND_section.sizes['dim_1'] )

WT_section.name = 'Vertical Wind speed (m/s)'
WT_section['dim_0'] = height
WT_section['dim_1'] = distance
#WT_section['dim_1'] = LATLON_section.values

WIND_section.name = 'Wind speed ($m.s^{-1}$)'
WIND_section['dim_0'] = height
WIND_section['dim_1'] = distance
#WIND_section['dim_1'] = LATLON_section.values

MRC_section.name = 'MRC'
MRC_section['dim_0'] = height
MRC_section['dim_1'] = distance
#MRC_section['dim_1'] = LATLON_section.values

wind_tangent_section.name = 'Tangent wind (m/s)'
wind_tangent_section['dim_0'] = height
wind_tangent_section['dim_1'] = distance

wind_normal_section.name = 'Normal wind (m/s)'
wind_normal_section['dim_0'] = height
wind_normal_section['dim_1'] = distance


### open figure
plt.figure()
ax = plt.axes()

###Customize colormap
def CustomColormap(Name = 'default'):
    if Name == 'Test':
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
    
CustCmap = CustomColormap('Test')


### plot surfaces
#surfaces = WIND_section.plot.contourf( cmap=CustCmap, levels=np.arange(20,59,0.5))
#surfaces = MRC_section.plot.contourf( cmap='Pastel1_r', levels=np.arange(0,0.5,0.01))
#surfaces = WT_section.plot.contourf( cmap='bwr', levels=np.arange(-3.5,3.7,0.1))
surfaces = wind_normal_section.plot.contourf( cmap=CustCmap, levels=np.arange(20,65,0.5))


### add contours
#contours1 = WT_section.plot.contour( colors='black', levels=[1],linewidth=0.5)
#ax.clabel( contours1, fmt='%1.0f')

#contours2 = WT_section.plot.contour( colors='black' ,levels=[-1])
#ax.clabel( contours2, fmt='%1.0f')

#contours3 = MRC_section.plot.contour( colors='magenta' ,levels=[0.01,0.1,1.], linewidth=3)
#ax.clabel( contours3, fmt='%1.0f')

plot_hbltop = plt.plot(distance, VAR_section, color ='red',linewidth=3)
#plt.text(7.8, 350, 'CCB', fontsize=20, color='black')

#cf = ax.contourf(MRC_section,color=['green'],levels=[0.1,10]) 
#cloud = MRC_section.plot.contourf(cmap='Greens' ,levels=[0.1,10])

### add wind vectors/barbs
interval_x = 2
interval_z = 2
factor_z = 5
ax.quiver(WT_section['dim_1'][::interval_x],WT_section['dim_0'][::interval_z],
          wind_tangent_section[::interval_z,::interval_x],
          WT_section[::interval_z,::interval_x]*factor_z, color='k')


plt.legend(title='NoM',loc=2)
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Height (m)")
plt.savefig( 'CV_COARE_MRC_1530_angle'+str(angle)+'.png' )


	


