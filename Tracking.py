# -*- coding: utf8 -*-

#========================================================#
#========================================================#

# --- Imports ---
import pandas as pd
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import sys
# --- --- --- ---
path1 = '/gpfs/work/p20024/lfarh/Paramétrisations_flux/ANDRE/MESONH/'
files1 =['ANDRE.1.SEG01.OUT.002.nc','ANDRE.1.SEG01.OUT.005.nc','ANDRE.1.SEG01.OUT.007.nc',
'ANDRE.1.SEG01.OUT.010.nc','ANDRE.1.SEG01.OUT.012.nc','ANDRE.1.SEG01.OUT.015.nc','ANDRE.1.SEG01.OUT.017.nc','ANDRE.1.SEG01.OUT.020.nc','ANDRE.1.SEG01.OUT.022.nc',
'ANDRE.1.SEG01.OUT.025.nc','ANDRE.1.SEG01.OUT.027.nc','ANDRE.1.SEG01.OUT.030.nc','ANDRE.1.SEG01.OUT.032.nc','ANDRE.1.SEG01.OUT.035.nc','ANDRE.1.SEG01.OUT.037.nc',
'ANDRE.1.SEG01.OUT.040.nc','ANDRE.1.SEG01.OUT.042.nc','ANDRE.1.SEG01.OUT.045.nc','ANDRE.1.SEG01.OUT.047.nc','ANDRE.1.SEG01.OUT.050.nc','ANDRE.1.SEG01.OUT.052.nc',
'ANDRE.1.SEG01.OUT.055.nc','ANDRE.1.SEG01.OUT.057.nc','ANDRE.1.SEG01.OUT.060.nc']

#path1 = '/gpfs/work/p20024/lfarh/SHIFT12-18/'
#files1 =['SHIFT.1.SEG01.OUT.062.nc','SHIFT.1.SEG01.OUT.065.nc','SHIFT.1.SEG01.OUT.067.nc',
#'SHIFT.1.SEG01.OUT.070.nc','SHIFT.1.SEG01.OUT.072.nc','SHIFT.1.SEG01.OUT.075.nc','SHIFT.1.SEG01.OUT.077.nc','SHIFT.1.SEG01.OUT.080.nc','SHIFT.1.SEG01.OUT.082.nc',
#'SHIFT.1.SEG01.OUT.085.nc','SHIFT.1.SEG01.OUT.087.nc','SHIFT.1.SEG01.OUT.090.nc','SHIFT.1.SEG01.OUT.092.nc','SHIFT.1.SEG01.OUT.095.nc','SHIFT.1.SEG01.OUT.097.nc',
#'SHIFT.1.SEG01.OUT.100.nc',
#'SHIFT.1.SEG01.OUT.102.nc','SHIFT.1.SEG01.OUT.105.nc','SHIFT.1.SEG01.OUT.107.nc','SHIFT.1.SEG01.OUT.110.nc','SHIFT.1.SEG01.OUT.112.nc','SHIFT.1.SEG01.OUT.115.nc',
#'SHIFT.1.SEG01.OUT.117.nc','SHIFT.1.SEG01.OUT.120.nc']



PGD = xr.open_dataset("/tmpdir/pantillo/PGD/PGD_1KM_750x750_V544.nc", mask_and_scale = True, decode_times = True)
zs = PGD.data_vars['ZS']


#####
PABSTLOW_list = []
date_list = []
Ystr_list = []
Mstr_list = []
Dstr_list = []
hstr_list = []

######
Col_name = []
    
lon_adr1,lat_adr1 = [],[]
for ncfile1 in files1 :
    # netcdf file begin always by 5 lettres of the simu
    # if not anymore, make a name_list and work with indexes
    Col_name.append(ncfile1[0:5])
    dataset = xr.open_dataset(path1+ncfile1,mask_and_scale=True, decode_times=True, decode_coords=True)
    time = dataset.coords['time']
    Lon = dataset.coords["longitude"]#.values
    Lat = dataset.coords["latitude"]#.values
    ZS = PGD.data_vars["ZS"]
    PABSTLOW0 = dataset.data_vars["PABSTLOW"]
    PABSTLOW0 = PABSTLOW0.where( ZS==0 )
    PABSTLOW = PABSTLOW0.isel(time=0).values
#    print(dataset.data_vars["DTCUR"].values," : ", np.nanmin(PABSTLOW))
    lon_adr1.append(float(Lon[np.where(PABSTLOW==np.nanmin(PABSTLOW))]))
    lat_adr1.append(float(Lat[np.where(PABSTLOW==np.nanmin(PABSTLOW))]))

traj1 = np.concatenate((np.array([lon_adr1]),np.array([lat_adr1])),axis=0)

print(traj1)
print(PABSTLOW)
