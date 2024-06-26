#####################################################################
#                      IMPORT LIBRAIRIES                            #
#####################################################################
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

#=============================================================================#
#                             READ Simulations files                          #
#=============================================================================#
ncfile_coare = xr.open_dataset("/gpfs/work/p20024/lfarh/SHIFT12-18/SHIFT12.1.SEG01.OUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_andrea = xr.open_dataset("/gpfs/work/p20024/lfarh/Paramétrisations_flux/ANDRE/MESONH/ANDRE.1.SEG01.OUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_ecume = xr.open_dataset("/gpfs/work/p20024/lfarh/Paramétrisations_flux/NECUM/MESONH/NECUM.1.SEG01.OUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_wasp = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents_1km/WASP2/MESONH/WASP2.1.SEG01.OUTPUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_nosen = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents_1km/NOSEN/MESONH/NOSEN.1.SEG01.OUTPUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_nolat = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents_1km/NOLAT/MESONH/NOLAT.1.SEG01.OUTPUT.nc", mask_and_scale = True, decode_times = True)
#=============================================================================#
ncfile_nomom = xr.open_dataset("/tmpdir/lfarh/New_flux_turbulents_1km/NOMOM/MESONH/NOMOM.1.SEG01.OUTPUT.nc", mask_and_scale = True, decode_times = True)


PGD = xr.open_dataset("/tmpdir/pantillo/PGD/PGD_1KM_750x750_V544.nc", mask_and_scale = True, decode_times = True)
ZS = PGD.data_vars["ZS"]#[240:641,180:581]

times = ncfile_coare.coords['time']
times_list = list(times.values)

### Calculate 99 percentile for Coare 
Perc99_list_coare_mslp_sea = []

for Inst_coare in range(len(times_list)):
    MSLP_coare = np.array(ncfile_coare.data_vars['PABSTLOW'][Inst_coare, :, :])/100
    ### keep data over sea only
    MSLP_coare_sea = MSLP_coare[np.where(ZS==0)]
    ### compute percentiles
    Perc99_list_coare_mslp_sea.append(np.percentile(MSLP_coare_sea,0))

### Calculate 99 percentile for Andrea
Perc99_list_andrea_mslp_sea = []

for Inst_andrea in range(len(times_list)):
    MSLP_andrea = np.array(ncfile_andrea.data_vars['PABSTLOW'][Inst_andrea, :, :])/100
    ### keep data over sea only
    MSLP_andrea_sea = MSLP_andrea[np.where(ZS==0)]
    ### compute percentiles
    Perc99_list_andrea_mslp_sea.append(np.percentile(MSLP_andrea_sea,0))

### Calculate 99 percentile for Ecume
Perc99_list_ecume_mslp_sea = []

for Inst_ecume in range(len(times_list)):
    MSLP_ecume = np.array(ncfile_ecume.data_vars['PABSTLOW'][Inst_ecume, :, :])/100
    ### keep data over sea only
    MSLP_ecume_sea = MSLP_ecume[np.where(ZS==0)]
    ### compute percentiles
    Perc99_list_ecume_mslp_sea.append(np.percentile(MSLP_ecume_sea,0))

### Calculate 99 percentile for Wasp
Perc99_list_wasp_mslp_sea = []
for Inst_wasp in range(len(times_list)):
    MSLP_wasp = np.array(ncfile_wasp.data_vars['PABSTLOW'][Inst_wasp, :, :])/100
    ### keep data over sea only
    MSLP_wasp_sea = MSLP_wasp[np.where(ZS==0)]
    ### compute percentiles
    Perc99_list_wasp_mslp_sea.append(np.percentile(MSLP_wasp_sea,0))
    
### Plot figure    
fig, ax1 = plt.subplots(figsize=(12,8))
ax1.plot(times_list,Perc99_list_coare_mslp_sea,linewidth=3,color='green',linestyle='--',label="COARE sea")
ax1.plot(times_list,Perc99_list_andrea_mslp_sea,linewidth=3,color='blue',linestyle='--',label="ANDREA sea")
ax1.plot(times_list,Perc99_list_ecume_mslp_sea,linewidth=3,color='red',linestyle='--',label="ECUME sea")
ax1.plot(times_list,Perc99_list_wasp_mslp_sea,linewidth=3,color='orange',linestyle='--',label="WASP sea")


plt.xlabel('Time (UTC)', fontsize=16)
plt.title('1th percentile', loc='left', fontsize=16)
plt.yticks(fontsize=16)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.xticks(fontsize=16)
plt.legend(fontsize=14)
plt.ylabel('Pression (hPa)',fontsize=16)
plt.savefig('Percentile_pressure_sea.png')
