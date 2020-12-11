import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.stats import mad_std
import h5py, os
from scipy.interpolate import RegularGridInterpolator

# cross-match of Stassun+2017 and 2MASS
data=ascii.read('1606119084338A.csv')
thet=data['Theta*']/1e6/206265.

gconst = 6.6726e-8
r_sun = 6.9599e10
m_sun = 1.9891e33	
sig=5.6704e-5	
torad=4.8481368e-12

rad=data['R*']
teff=(4.*data['Fbol']/(sig* (2.*thet)**2))**(1./4.)
feh=np.zeros(len(teff))
logg=np.log10(gconst*data['M*']*m_sun/(data['R*']*r_sun)**2)
logg=np.zeros(len(teff))+4.5
av=data['Av']
kmag=data['Kmag']
fbol=data['Fbol']

#fn = os.path.join('/Users/daniel/science/research/codes/github/isoclassify/','bcgrid.h5')
bcmodel = h5py.File('bcgrid.h5','r', driver='core', backing_store=False)

teffgrid = bcmodel['teffgrid'][:]
logggrid = bcmodel['logggrid'][:]
fehgrid = bcmodel['fehgrid'][:]
avgrid = bcmodel['avgrid'][:]
bc_band = bcmodel['bc_k'][:]

points = (teffgrid,logggrid,fehgrid,avgrid)
values = bc_band
interp = RegularGridInterpolator(points, values)

fbols=np.zeros(len(fbol))
ids=['']*len(fbol)

f0=1.361e6
mcal=-26.82

f0=3.828e33
mbol=4.74

f0=1.361e6

mcal=5.*np.log10(4.84814e-6)-5+mbol
#mcal=-26.82

for i in range(0,len(fbol)):
	x = np.array([np.float(teff[i]),np.float(logg[i]),np.float(feh[i]),np.float(av[i])])
	bc = interp(x)[0]
	fbols[i] = f0*10.**(-0.4*(kmag[i]-mcal+bc))
	ids[i]='TYC'+data['Tycho'][i]
	#print(data['Tycho'][i],kmag[i],teff[i],logg[i],feh[i],av[i],fbol[i],fbols[i])

plt.ion()
plt.clf()
plt.plot(teff,fbol/fbols,'o')
plt.plot([4000,7000],[1,1],color='red')
plt.xlim([4000,7000])
plt.ylim([0.6,1.4])

print(np.median(fbol/fbols))
ascii.write([teff,rad,fbol,fbols],'mistbcomp.csv',names=['teff','rad','fbol_sed','fbol_bc'],delimiter=',')