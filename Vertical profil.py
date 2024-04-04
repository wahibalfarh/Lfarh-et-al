
### Import librairies
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import sys

### define variable
varname = 'SBG_KM'
#varname = 'MEAN_THV'

###########################
#    Read Meso-NH data    #
###########################

mnh_coare= xr.open_dataset("/tmpdir/lfarh/ADRIA/000/COAFL/ADRIA.2.COAFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_andrea= xr.open_dataset("/tmpdir/lfarh/ADRIA/000/ANDFL/ADRIA.2.ANDFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_ecume= xr.open_dataset("/tmpdir/lfarh/ADRIA/000/ECMFL/ADRIA.2.ECMFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_wasp= xr.open_dataset("/tmpdir/lfarh/ADRIA/000/WSPFL/ADRIA.2.WSPFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)

### read data
var_coare = mnh_coare.data_vars[varname+'___PROC1'][0,0,:,0,0]
var_andrea = mnh_andrea.data_vars[varname+'___PROC1'][0,0,:,0,0]
var_ecume = mnh_ecume.data_vars[varname+'___PROC1'][0,0,:,0,0]
var_wasp = mnh_wasp.data_vars[varname+'___PROC1'][0,0,:,0,0]

### read coordinates
levels_coare = mnh_coare.data_vars[varname+'___TRAJZ'][0,0,:]
levels_andrea = mnh_andrea.data_vars[varname+'___TRAJZ'][0,0,:]
levels_ecume = mnh_ecume.data_vars[varname+'___TRAJZ'][0,0,:]
levels_wasp = mnh_wasp.data_vars[varname+'___TRAJZ'][0,0,:]

### plot vertical profiles ###
################################
fig, ax = plt.subplots(figsize=(6,8))

ax.plot(var_coare, levels_coare, c='green',linestyle='-',label='Coare')
ax.plot(var_andrea,levels_andrea, c='royalblue',linestyle='-',label='Andreas')
ax.plot(var_ecume, levels_ecume, c='orchid',linestyle='-',label='Ecume')
ax.plot(var_wasp,levels_wasp , c='orange',linestyle='-',label='Wasp')

# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()

plt.ylim(0,1200)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.set_xlabel('Momentum eddy diffusivity (m$^2$ s$^{-1}$)')

#ax.set_xlabel('Wind speed ($\mathregular{m\, s^{-1}}$)',fontsize=12)
#ax.set_xlabel('Mean virtual potential temperature (k)',fontsize=12)
#ax.set_ylabel('Height (m)')

#ax.set_xlabel('Downdraft resolved TKE ($\mathregular{m^{2}\, s^{-2}}$)',fontsize=12)
#ax.set_xlabel('Downdraft cloud water ($\mathregular{kg\, kg^{-1}}$)',fontsize=12)

#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ylabel('Height (m)',fontsize=12)
plt.legend(loc=2,fontsize=12)
ax.legend()
plt.savefig('profile_simulation_param_SBG_KM.png')



plt.close()
