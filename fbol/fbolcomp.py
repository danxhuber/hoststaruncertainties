import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.stats import mad_std
import bin

plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 3
plt.rcParams['xtick.minor.size'] = 3
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 3
plt.rcParams['ytick.minor.size'] = 3
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['axes.linewidth'] = 3
plt.rcParams['font.size']=18
plt.rcParams['mathtext.default']='regular'
plt.rcParams['lines.markersize']=8
plt.rcParams['xtick.major.pad']='6'
plt.rcParams['ytick.major.pad']='8'
plt.rcParams['ytick.minor.visible'] = 'True'
plt.rcParams['xtick.minor.visible'] = 'True'
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['ytick.right'] = 'True'
plt.rcParams['xtick.top'] = 'True'

pctocm=3.08567758128e18
lsun=3.839e33 

lol=0.88
upl=1.12

# cross-match of Casagrande+2011 and Stassun+2017
data=ascii.read('1592769150940A.csv',delimiter=',',guess=False)

# cross-match of McDonald+2017 and Stassun+2017
data2=ascii.read('1606098237932A.csv',delimiter=',',guess=False)
fbol=(lsun*data2['L'])/((data2['D']*pctocm)**2*4.*np.pi)

# MIST K-band fbols for Stassun+2017 sample
data3=ascii.read('mistbcomp.csv')

plt.ion()
plt.clf()

plt.subplot(3,1,2)
xarr=data['Teff']
yarr=data['Fbol']/data['Fbol2']
um=np.where((yarr > 0.5) & (yarr < 1.5) & (xarr > 4000.))[0]
xarr=xarr[um]
yarr=yarr[um]
plt.plot(xarr,yarr,'o',label='',alpha=0.5,ms=5,color='grey')
resx,resy,resz=bin.bin_time(xarr,yarr,100)
plt.errorbar(resx,resy,yerr=resz,fmt='-o',color='red')
plt.ylabel('f$_{bol,SED}$/f$_{bol,IRFM}$')
plt.plot([4000.,8000.],[1,1],ls='dashed',color='black')
plt.xlim([4000.,7000.])
plt.ylim([lol,upl])
plt.tick_params(axis='x',labelbottom=False) 
plt.text(6700,1.07,'(b)',fontsize=24)
print(np.median(yarr),mad_std(yarr))

plt.subplot(3,1,1)
xarr=data2['Teff']
yarr=data2['Fbol']/fbol
um=np.where((yarr > 0.5) & (yarr < 1.5) & (xarr > 4000.))[0]
xarr=xarr[um]
yarr=yarr[um]
plt.plot(xarr,yarr,'o',label='',alpha=0.5,ms=5,color='grey')
resx,resy,resz=bin.bin_time(xarr,yarr,100)
plt.errorbar(resx,resy,yerr=resz,fmt='-o',color='red')
plt.ylabel('f$_{bol,SED}$/f$_{bol,SED}$')
plt.plot([4000.,8000.],[1,1],ls='dashed',color='black')
plt.xlim([4000.,7000.])
plt.ylim([lol,upl])
plt.tick_params(axis='x',labelbottom=False) 
plt.text(6700,1.07,'(a)',fontsize=24)
print(np.median(yarr),mad_std(yarr))

plt.subplot(3,1,3)
xarr=data3['teff']
yarr=data3['fbol_sed']/data3['fbol_bc']
um=np.where((yarr > 0.5) & (yarr < 1.5) & (data3['rad'] < 3))[0]
um=np.where((yarr > 0.5) & (yarr < 1.5) & (xarr > 4000.))[0]
xarr=xarr[um]
yarr=yarr[um]
plt.plot(xarr,yarr,'o',label='',alpha=0.5,ms=5,color='grey')
resx,resy,resz=bin.bin_time(xarr,yarr,100)
plt.errorbar(resx,resy,yerr=resz,fmt='-o',color='red')
plt.ylabel('f$_{bol,SED}$/f$_{bol,BC(K)}$')
plt.plot([4000.,8000.],[1,1],ls='dashed',color='black')
plt.xlim([4000.,7000.])
plt.ylim([lol,upl])
plt.xlabel('Effective Temperature (K)')
plt.text(6700,1.07,'(c)',fontsize=24)
print(np.median(yarr),mad_std(yarr))


