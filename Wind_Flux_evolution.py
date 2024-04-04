import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import pandas as pd

#########################################
###     Read Meso-NH data at 1530     ###
#########################################

ncfile_andrea = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NDREA/NDREA.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_ecume = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/ECUME/ECUME.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_wasp = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/WASP/WASP2.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_nosen = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOSEN/NOSEN.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_nolat = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOLAT/NOLAT.2.SEG01.002DIA3D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_coare = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/COARE/ADRIA.2.SEG04.002DIA2D.zoom.nc", mask_and_scale=True, decode_times=True)
ncfile_nomom = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents/NOMOM/NOMOM.2.SEG02.001DIA2D.nc", mask_and_scale=True, decode_times=True)

### Zommed domain
left = 8.3
bottom = 41.62
right = 8.55
top = 41.8

### Read coordinates
longitude = ncfile_coare.coords['longitude'][0,:].values
latitude = ncfile_coare.coords['latitude'][:,0].values

### Zoom
x0 = np.searchsorted( longitude, left )
x1 = np.searchsorted( longitude, right )
y0 = np.searchsorted( latitude, bottom )
y1 = np.searchsorted( latitude, top )

### Read variables of each simulation 
ch_latente1 = ncfile_coare.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente1 = ch_latente1.where(ch_latente1!=999)
U1 = ncfile_coare.data_vars['UM10'][0,y0:y1,x0:x1]
V1 = ncfile_coare.data_vars['VM10'][0,y0:y1,x0:x1]
WIND1 = np.sqrt( U1**2 + V1**2 )
FMU1 = ncfile_coare.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV1 = ncfile_coare.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM1 = np.sqrt( FMU1**2 +FMV1**2 )

ch_latente2 = ncfile_andrea.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente2 = ch_latente2.where(ch_latente2!=999)
U2 = ncfile_andrea.data_vars['UM10'][0,y0:y1,x0:x1]
V2 = ncfile_andrea.data_vars['VM10'][0,y0:y1,x0:x1]
WIND2 = np.sqrt( U2**2 + V2**2 )
FMU2 = ncfile_andrea.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV2 = ncfile_andrea.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM2 = np.sqrt( FMU2**2 +FMV2**2 )

ch_latente3 = ncfile_ecume.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente3 = ch_latente3.where(ch_latente3!=999)
U3 = ncfile_ecume.data_vars['UM10'][0,y0:y1,x0:x1]
V3 = ncfile_ecume.data_vars['VM10'][0,y0:y1,x0:x1]
WIND3 = np.sqrt( U3**2 + V3**2 )
FMU3 = ncfile_ecume.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV3 = ncfile_ecume.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM3 = np.sqrt( FMU3**2 +FMV3**2 )

ch_latente4 = ncfile_wasp.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente4 = ch_latente4.where(ch_latente4!=999)
U4 = ncfile_wasp.data_vars['UM10'][0,y0:y1,x0:x1]
V4 = ncfile_wasp.data_vars['VM10'][0,y0:y1,x0:x1]
WIND4 = np.sqrt( U4**2 + V4**2 )
FMU4 = ncfile_wasp.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV4 = ncfile_wasp.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM4 = np.sqrt( FMU4**2 +FMV4**2 )

ch_latente5 = ncfile_nosen.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente5 = ch_latente5.where(ch_latente5!=999)
U5 = ncfile_nosen.data_vars['UM10'][0,y0:y1,x0:x1]
V5 = ncfile_nosen.data_vars['VM10'][0,y0:y1,x0:x1]
WIND5 = np.sqrt( U5**2 + V5**2 )
FMU5 = ncfile_nosen.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV5 = ncfile_nosen.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM5 = np.sqrt( FMU5**2 +FMV5**2 )

ch_latente6 = ncfile_nolat.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente6 = ch_latente6.where(ch_latente6!=999)
U6 = ncfile_nolat.data_vars['UM10'][0,y0:y1,x0:x1]
V6 = ncfile_nolat.data_vars['VM10'][0,y0:y1,x0:x1]
WIND6 = np.sqrt( U6**2 + V6**2 )
FMU6 = ncfile_nolat.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV6 = ncfile_nolat.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM6 = np.sqrt( FMU6**2 +FMV6**2 )

ch_latente7 = ncfile_nomom.data_vars['LE_SEA'][y0:y1,x0:x1]
Latente7 = ch_latente7.where(ch_latente7!=999)
U7 = ncfile_nomom.data_vars['UM10'][0,y0:y1,x0:x1]
V7 = ncfile_nomom.data_vars['VM10'][0,y0:y1,x0:x1]
WIND7 = np.sqrt( U7**2 + V7**2 )
FMU7 = ncfile_nomom.data_vars['FMU_SEA'][y0:y1,x0:x1]
FMV7 = ncfile_nomom.data_vars['FMV_SEA'][y0:y1,x0:x1]
FM7 = np.sqrt( FMU7**2 +FMV7**2 )

### Plot figure
fig, ax1 = plt.subplots()

scatter1 = ax1.scatter(WIND1[::5, ::5], FM1[::5, ::5], color='green', s=0.5, label="Coare")
scatter2 = ax1.scatter(WIND2[::5, ::5], FM2[::5, ::5], color='royalblue', s=0.5, label="Andreas")
scatter3 = ax1.scatter(WIND3[::5, ::5], FM3[::5, ::5], color='orchid', s=0.5, label="Ecume")
scatter4 = ax1.scatter(WIND4[::5, ::5], FM4[::5, ::5], color='orange', s=0.5, label="Wasp")

scatters = [scatter1, scatter2, scatter3, scatter4]
labels = [scatter.get_label() for scatter in scatters]
handler = plt.legend(handles=scatters, labels=labels, fontsize=12)

for legend_handle in handler.legendHandles:
    legend_handle.set_sizes([40])

ax1.set_xlabel("10m-wind speed ($m.s^{-1}$)",fontsize=12)
ax1.set_xlim(10,50)
#ax1.set_ylabel("Latent heat flux ($W.m^{-2}$)",fontsize=12)
ax1.set_ylabel("Momentum flux ($m².s^{-2}$ )",fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.savefig('Evolution_Momentum_15h30_param.png')

