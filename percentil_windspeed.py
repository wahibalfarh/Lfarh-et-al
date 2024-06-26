import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
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

Perc99_list_coare = []
Perc99_list_coare_sea = []
Perc99_list_coare_land = []

times_list = list(times.values)

for Inst_coare in range(len(times)):
    U_coare = np.array(ncfile_coare.data_vars['UTLOW'][Inst_coare, :, :])
    V_coare = np.array(ncfile_coare.data_vars['VTLOW'][Inst_coare, :, :])
    WindSpeed_coare = np.sqrt(U_coare**2 + V_coare**2)
    ### keep data over sea/land only
    WindSpeed_coare_sea = WindSpeed_coare[np.where(ZS==0)]
    WindSpeed_coare_land = WindSpeed_coare[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_coare.append(np.percentile(WindSpeed_coare,99))
    Perc99_list_coare_sea.append(np.percentile(WindSpeed_coare_sea,99))
    Perc99_list_coare_land.append(np.percentile(WindSpeed_coare_land,99))
   
Perc99_list_andrea = []
Perc99_list_andrea_sea = []
Perc99_list_andrea_land = []  

for Inst_andrea in range(len(times)):
    U_andrea = np.array(ncfile_andrea.data_vars['UTLOW'][Inst_andrea, :, :])
    V_andrea = np.array(ncfile_andrea.data_vars['VTLOW'][Inst_andrea, :, :])
    WindSpeed_andrea = np.sqrt(U_andrea**2 + V_andrea**2)
    ### keep data over sea/land only
    WindSpeed_andrea_sea = WindSpeed_andrea[np.where(ZS==0)]
    WindSpeed_andrea_land = WindSpeed_andrea[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_andrea.append(np.percentile(WindSpeed_andrea,99))
    Perc99_list_andrea_sea.append(np.percentile(WindSpeed_andrea_sea,99))
    Perc99_list_andrea_land.append(np.percentile(WindSpeed_andrea_land,99))   

Perc99_list_ecume = []
Perc99_list_ecume_sea = []
Perc99_list_ecume_land = []

for Inst_ecume in range(len(times)):
    U_ecume = np.array(ncfile_ecume.data_vars['UTLOW'][Inst_ecume, :, :])
    V_ecume = np.array(ncfile_ecume.data_vars['VTLOW'][Inst_ecume, :, :])
    WindSpeed_ecume = np.sqrt(U_ecume**2 + V_ecume**2)
    ### keep data over sea/land only
    WindSpeed_ecume_sea = WindSpeed_ecume[np.where(ZS==0)]
    WindSpeed_ecume_land = WindSpeed_ecume[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_ecume.append(np.percentile(WindSpeed_ecume,99))
    Perc99_list_ecume_sea.append(np.percentile(WindSpeed_ecume_sea,99))
    Perc99_list_ecume_land.append(np.percentile(WindSpeed_ecume_land,99))

Perc99_list_wasp = []
Perc99_list_wasp_sea = []
Perc99_list_wasp_land = []

for Inst_wasp in range(len(times)):
    U_wasp = np.array(ncfile_wasp.data_vars['UTLOW'][Inst_wasp, :, :])
    V_wasp = np.array(ncfile_wasp.data_vars['VTLOW'][Inst_wasp, :, :])
    WindSpeed_wasp = np.sqrt(U_wasp**2 + V_wasp**2)
    ### keep data over sea/land only
    WindSpeed_wasp_sea = WindSpeed_wasp[np.where(ZS==0)]
    WindSpeed_wasp_land = WindSpeed_wasp[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_wasp.append(np.percentile(WindSpeed_wasp,99))
    Perc99_list_wasp_sea.append(np.percentile(WindSpeed_wasp_sea,99))
    Perc99_list_wasp_land.append(np.percentile(WindSpeed_wasp_land,99))

###############################################################################"
Perc99_list_nosen = []
Perc99_list_nosen_sea = []
Perc99_list_nosen_land = []

for Inst_nosen in range(len(times)):
    U_nosen = np.array(ncfile_nosen.data_vars['UTLOW'][Inst_nosen, :, :])
    V_nosen = np.array(ncfile_nosen.data_vars['VTLOW'][Inst_nosen, :, :])
    WindSpeed_nosen = np.sqrt(U_nosen**2 + V_nosen**2)
    ### keep data over sea/land only
    WindSpeed_nosen_sea = WindSpeed_nosen[np.where(ZS==0)]
    WindSpeed_nosen_land = WindSpeed_nosen[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_nosen.append(np.percentile(WindSpeed_nosen,99))
    Perc99_list_nosen_sea.append(np.percentile(WindSpeed_nosen_sea,99))
    Perc99_list_nosen_land.append(np.percentile(WindSpeed_nosen_land,99))

Perc99_list_nolat = []
Perc99_list_nolat_sea = []
Perc99_list_nolat_land = []

for Inst_nolat in range(len(times)):
    U_nolat = np.array(ncfile_nolat.data_vars['UTLOW'][Inst_nolat, :, :])
    V_nolat = np.array(ncfile_nolat.data_vars['VTLOW'][Inst_nolat, :, :])
    WindSpeed_nolat = np.sqrt(U_nolat**2 + V_nolat**2)
    ### keep data over sea/land only
    WindSpeed_nolat_sea = WindSpeed_nolat[np.where(ZS==0)]
    WindSpeed_nolat_land = WindSpeed_nolat[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_nolat.append(np.percentile(WindSpeed_nolat,99))
    Perc99_list_nolat_sea.append(np.percentile(WindSpeed_nolat_sea,99))
    Perc99_list_nolat_land.append(np.percentile(WindSpeed_nolat_land,99))

Perc99_list_nomom = []
Perc99_list_nomom_sea = []
Perc99_list_nomom_land = []

for Inst_nomom in range(len(times)):
    U_nomom = np.array(ncfile_nomom.data_vars['UTLOW'][Inst_nomom, :, :])
    V_nomom = np.array(ncfile_nomom.data_vars['VTLOW'][Inst_nomom, :, :])
    WindSpeed_nomom = np.sqrt(U_nomom**2 + V_nomom**2)
    ### keep data over sea/land only
    WindSpeed_nomom_sea = WindSpeed_nomom[np.where(ZS==0)]
    WindSpeed_nomom_land = WindSpeed_nomom[np.where(ZS!=0)]
    ### compute percentiles
    Perc99_list_nomom.append(np.percentile(WindSpeed_nomom,99))
    Perc99_list_nomom_sea.append(np.percentile(WindSpeed_nomom_sea,99))
    Perc99_list_nomom_land.append(np.percentile(WindSpeed_nomom_land,99))

### Plot figure

plt.plot(times_list,Perc99_list_coare_sea,color='green',linestyle='-',label="Coare ")
plt.plot(times_list,Perc99_list_andrea_sea,color='royalblue',linestyle='-',label="Andreas")
plt.plot(times_list,Perc99_list_ecume_sea,color='orchid',linestyle='-',label="Ecume")
plt.plot(times_list,Perc99_list_wasp_sea,color='orange',linestyle='-',label="Wasp")

plt.xlabel('Time (UTC)', fontsize=12)
plt.ylabel('10m Wind speed ($\mathregular{m\, s^{-1}}$)', fontsize=12)
plt.title('99th percentile', loc='left', fontsize=12)
plt.yticks(fontsize=12)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.xticks(fontsize=12)
plt.legend(fontsize=12)

plt.savefig('99Percentile_Wind10m_sea.png')
