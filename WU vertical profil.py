###########################################################################################################
# Vertical profiles of resolved and turbulent vertical fluxes of zonal momentum #
###########################################################################################################

### Import librairies
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt



### define variable
varname_res= 'RES_WU'
varname_sbg= 'SBG_WU'

###########################
#    Read Meso-NH data    #
###########################
mnh_coare= xr.open_dataset("/tmpdir/lfarh/ADRIA/COAFL/ADRIA.2.COAFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_andrea= xr.open_dataset("/tmpdir/lfarh/ADRIA/ANDFL/ADRIA.2.ANDFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_ecume= xr.open_dataset("/tmpdir/lfarh/ADRIA/ECMFL/ADRIA.2.ECMFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)
mnh_wasp= xr.open_dataset("/tmpdir/lfarh/ADRIA/WSPFL/ADRIA.2.WSPFL.000.nc", mask_and_scale=True, decode_times=True, decode_coords=True)

### read data
res_coare = mnh_coare.data_vars[varname_res+'___PROC1'][0,0,:,0,0]
res_andrea = mnh_andrea.data_vars[varname_res+'___PROC1'][0,0,:,0,0]
res_ecume = mnh_ecume.data_vars[varname_res+'___PROC1'][0,0,:,0,0]
res_wasp = mnh_wasp.data_vars[varname_res+'___PROC1'][0,0,:,0,0]

sbg_coare = mnh_coare.data_vars[varname_sbg+'___PROC1'][0,0,:,0,0]
sbg_andrea = mnh_andrea.data_vars[varname_sbg+'___PROC1'][0,0,:,0,0]
sbg_ecume = mnh_ecume.data_vars[varname_sbg+'___PROC1'][0,0,:,0,0]
sbg_wasp = mnh_wasp.data_vars[varname_sbg+'___PROC1'][0,0,:,0,0] 

somme_coare = res_coare+sbg_coare
somme_andrea = res_andrea+sbg_andrea
somme_ecume = res_ecume+sbg_ecume
somme_wasp = res_wasp+sbg_wasp

### read coordinates
levels_coare = mnh_coare.data_vars[varname_res+'___TRAJZ'][0,0,:]
levels_andrea = mnh_andrea.data_vars[varname_res+'___TRAJZ'][0,0,:]
levels_ecume = mnh_ecume.data_vars[varname_res+'___TRAJZ'][0,0,:]
levels_wasp = mnh_wasp.data_vars[varname_res+'___TRAJZ'][0,0,:]   

levels_coare_sbg = mnh_coare.data_vars[varname_sbg+'___TRAJZ'][0,0,:]
levels_andrea_sbg = mnh_andrea.data_vars[varname_sbg+'___TRAJZ'][0,0,:]
levels_ecume_sbg = mnh_ecume.data_vars[varname_sbg+'___TRAJZ'][0,0,:]
levels_wasp_sbg = mnh_wasp.data_vars[varname_sbg+'___TRAJZ'][0,0,:]

### plot vertical profiles ###
################################
fig, ax = plt.subplots(figsize=(6,8))

ax.plot(res_coare, levels_coare, c='green',linestyle='--', label='RES_WU')
ax.plot(res_andrea,levels_andrea, c='royalblue',linestyle='--')
ax.plot(res_ecume, levels_ecume, c='orchid',linestyle='--')
ax.plot(res_wasp,levels_wasp, c='orange',linestyle='--')


ax.plot(sbg_coare, levels_coare_sbg, c='green',linestyle=':', label='SBG_WU')
ax.plot(sbg_andrea,levels_andrea_sbg, c='royalblue',linestyle=':')
ax.plot(sbg_ecume, levels_ecume_sbg, c='orchid',linestyle=':')
ax.plot(sbg_wasp,levels_wasp_sbg, c='orange',linestyle=':')

ax.plot(somme_coare, levels_coare_sbg, c='green', linewidth=3, label ='RES + SBG')
ax.plot(somme_andrea,levels_andrea_sbg, c='royalblue',linewidth=3)
ax.plot(somme_ecume, levels_ecume_sbg, c='orchid',linewidth=3)
ax.plot(somme_wasp,levels_wasp_sbg, c='orange',linewidth=3)


#plt.axhline(y = 730, color = 'green', linestyle = '-', linewidth=1, label = 'Boundary-layer height')
#plt.axhline(y = 509, color = 'royalblue', linestyle = '-', linewidth=1)
#plt.axhline(y = 693, color = 'orchid', linestyle = '-', linewidth=1)
#plt.axhline(y = 1360, color = 'royalblue', linestyle = '-', linewidth=1)

ax.axvline(0,color="grey",linewidth=2)


# ask matplotlib for the plotted objects and their labels
lines, labels = ax.get_legend_handles_labels()
#lines2, labels2 = ax2.get_legend_handles_labels()
#ax2.legend(lines + lines2, labels + labels2, loc=0)


plt.ylim(0,1200)
ax.set_xlabel('<WU> (m$^{2}$ s$^{-2}$ )',fontsize=12)
#ax.set_xlabel('Wind speed (m/s)')
#ax.set_ylabel('Height (m)',fontsize=12)
plt.ylabel('Height (m)',fontsize=12)
plt.legend(loc=2,fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.legend()
plt.savefig('profile_simulation_WU_RES_SBG_param.png')
plt.savefig('profile_simulation_WU_RES_SBG_param.pdf')

plt.close()
