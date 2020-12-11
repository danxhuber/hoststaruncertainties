import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
from astroquery.simbad import Simbad
from astropy.stats import mad_std
import pdb

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

#data=ascii.read('diameters.csv')
#data=ascii.read('diameters-Dec2019-ed.csv')
data=ascii.read('diameters-Dec2020.csv')

ras=np.zeros(len(data))
decs=np.zeros(len(data))

Simbad.add_votable_fields('ra(d)', 'dec(d)')
Simbad.add_votable_fields('typed_id')
Simbad.ROW_LIMIT = 1

sim=Simbad.query_objects(data['Star'].tolist())
x=np.zeros(1)
xe=np.zeros(1)
y=np.zeros(1)
ye=np.zeros(1)
istr=['']*len(x)
refs=['']*len(x)

done=np.zeros(len(sim))

for i in range(0,len(sim)):
    if (done[i] == 1):
        continue
    um=np.where((sim['RA_d'] == sim['RA_d'][i]) & (sim['DEC_d'] == sim['DEC_d'][i]))[0]
    if (len(um) == 1):
        continue
    else:
        s=np.argsort(data['Instrument'][um])
        um=um[s]
        if (len(um) == 2):
            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[1]])
            ye=np.append(ye,data['Err'][um[1]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[1]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[1]])

        if (len(um) == 3):
            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[1]])
            ye=np.append(ye,data['Err'][um[1]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[1]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[1]])
            
            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[2]])
            ye=np.append(ye,data['Err'][um[2]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[2]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[2]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[2]])
 
            x=np.append(x,data['Diam'][um[1]])
            xe=np.append(xe,data['Err'][um[1]])
            y=np.append(y,data['Diam'][um[2]])
            ye=np.append(ye,data['Err'][um[2]])       
            istr=np.append(istr,data['Instrument'][um[1]]+'/'+data['Instrument'][um[2]])
            refs=np.append(refs,data['Reference'][um[1]]+' & '+data['Reference'][um[2]])
            allrefs=np.append(refs,data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[2]])


        if (len(um) == 4):
            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[1]])
            ye=np.append(ye,data['Err'][um[1]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[1]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[1]])
            
            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[2]])
            ye=np.append(ye,data['Err'][um[2]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[2]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[2]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[2]])

            x=np.append(x,data['Diam'][um[0]])
            xe=np.append(xe,data['Err'][um[0]])
            y=np.append(y,data['Diam'][um[3]])
            ye=np.append(ye,data['Err'][um[3]])
            istr=np.append(istr,data['Instrument'][um[0]]+'/'+data['Instrument'][um[3]])
            refs=np.append(refs,data['Reference'][um[0]]+' & '+data['Reference'][um[3]])
            allrefs=np.append(refs,data['Reference'][um[0]])
            allrefs=np.append(refs,data['Reference'][um[3]])
 
            x=np.append(x,data['Diam'][um[1]])
            xe=np.append(xe,data['Err'][um[1]])
            y=np.append(y,data['Diam'][um[2]])
            ye=np.append(ye,data['Err'][um[2]])  
            istr=np.append(istr,data['Instrument'][um[1]]+'/'+data['Instrument'][um[2]])    
            refs=np.append(refs,data['Reference'][um[1]]+' & '+data['Reference'][um[2]])
            allrefs=np.append(refs,data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[2]])

            x=np.append(x,data['Diam'][um[1]])
            xe=np.append(xe,data['Err'][um[1]])
            y=np.append(y,data['Diam'][um[3]])
            ye=np.append(ye,data['Err'][um[3]])       
            istr=np.append(istr,data['Instrument'][um[1]]+'/'+data['Instrument'][um[3]])
            refs=np.append(refs,data['Reference'][um[1]]+' & '+data['Reference'][um[3]])
            allrefs=np.append(refs,data['Reference'][um[1]])
            allrefs=np.append(refs,data['Reference'][um[3]])
        
            x=np.append(x,data['Diam'][um[2]])
            xe=np.append(xe,data['Err'][um[2]])
            y=np.append(y,data['Diam'][um[3]])
            ye=np.append(ye,data['Err'][um[3]])
            istr=np.append(istr,data['Instrument'][um[2]]+'/'+data['Instrument'][um[3]])
            refs=np.append(refs,data['Reference'][um[2]]+' & '+data['Reference'][um[3]])
            allrefs=np.append(refs,data['Reference'][um[2]])
            allrefs=np.append(refs,data['Reference'][um[3]])
            
        done[um]=1       
        
        #for j in range(0,len(um)):
            
x=x[1::]
y=y[1::]
xe=xe[1::]
ye=ye[1::]
istr=istr[1::]
refs=refs[1::]

#pdb.set_trace()

rat=x/y
rate=np.sqrt( (xe/x)**2 + (ye/y)**2 )*rat

x2=np.zeros(1)
x2e=np.zeros(1)
y2=np.zeros(1)
y2e=np.zeros(1)
ids=np.zeros(1,dtype='S20')

sim=ascii.read('jmmc.csv',delimiter=';')

done=np.zeros(len(sim))

for i in range(0,len(sim)):
    if (done[i] == 1):
        continue
    um=np.where((sim['RA_d'] == sim['RA_d'][i]) & (sim['DEC_d'] == sim['DEC_d'][i]))[0]
    if (len(um) == 1):
        continue
    else:
        if (len(um) == 2):
            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[1]])
            y2e=np.append(y2e,sim['Err'][um[1]])
            ids=np.append(ids,sim['ID1'][um[0]])

        if (len(um) == 3):
            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[1]])
            y2e=np.append(y2e,sim['Err'][um[1]])
            ids=np.append(ids,sim['ID1'][um[0]])
            
            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[2]])
            y2e=np.append(y2e,sim['Err'][um[2]])
            ids=np.append(ids,sim['ID1'][um[0]])
            
            x2=np.append(x2,sim['Diam'][um[1]])
            x2e=np.append(x2e,sim['Err'][um[1]])
            y2=np.append(y2,sim['Diam'][um[2]])
            y2e=np.append(y2e,sim['Err'][um[2]])       
            ids=np.append(ids,sim['ID1'][um[0]])
            
    
        if (len(um) == 4):
            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[1]])
            y2e=np.append(y2e,sim['Err'][um[1]])
            ids=np.append(ids,sim['ID1'][um[0]])
            
            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[2]])
            y2e=np.append(y2e,sim['Err'][um[2]])
            ids=np.append(ids,sim['ID1'][um[0]])

            x2=np.append(x2,sim['Diam'][um[0]])
            x2e=np.append(x2e,sim['Err'][um[0]])
            y2=np.append(y2,sim['Diam'][um[3]])
            y2e=np.append(y2e,sim['Err'][um[3]])
            ids=np.append(ids,sim['ID1'][um[0]])
 
            x2=np.append(x2,sim['Diam'][um[1]])
            x2e=np.append(x2e,sim['Err'][um[1]])
            y2=np.append(y2,sim['Diam'][um[2]])
            y2e=np.append(y2e,sim['Err'][um[2]])      
            ids=np.append(ids,sim['ID1'][um[0]])

            x2=np.append(x2,sim['Diam'][um[1]])
            x2e=np.append(x2e,sim['Err'][um[1]])
            y2=np.append(y2,sim['Diam'][um[3]])
            y2e=np.append(y2e,sim['Err'][um[3]])       
            ids=np.append(ids,sim['ID1'][um[0]])
        
            x2=np.append(x2,sim['Diam'][um[2]])
            x2e=np.append(x2e,sim['Err'][um[2]])
            y2=np.append(y2,sim['Diam'][um[3]])
            y2e=np.append(y2e,sim['Err'][um[3]])       
            ids=np.append(ids,sim['ID1'][um[0]])
                  
        done[um]=1
        
x2=x2[1::]
y2=y2[1::]
x2e=x2e[1::]
y2e=y2e[1::]
ids=ids[1::]

rat2=x2/y2
rat2e=np.sqrt( (x2e/x2)**2 + (y2e/y2)**2 )*rat2


upl=1.35
lol=0.65


plt.ion()
plt.clf()

un=np.unique(istr)
un=un[0:-1]

um=np.where((x > 1.) & (istr == 'CLASSIC/VEGA'))[0]

plt.subplot(2,1,1)

ss=['o','D','s','^','>','<','D','^','s']


allrefs=['']

vals=np.zeros(1)

for i in range(0,len(un)):
    um=np.where((istr == un[i]) & (rate < 0.05))[0]
    if (len(um) > 1):
	    plt.errorbar(x[um],rat[um],yerr=rate[um],fmt=ss[i],color='grey',zorder=-32)
	    plt.plot(x[um],rat[um],ss[i],label=un[i])
	
	    for j in range(0,len(um)):
		    xt=refs[um[j]].split('&')
		    allrefs=np.append(allrefs,xt[0])
		    allrefs=np.append(allrefs,xt[1])
	
	    print(un[i],np.median(rat[um]))
	    vals=np.append(vals,1.-np.median(rat[um]))
    
print('median absolute difference over all beam combiners:',np.median(np.abs(vals[1::])))

plt.xlim([0.25,2.2])
plt.ylim([lol,upl])
#plt.plot([0.05,30],[1,1],ls='dashed',color='grey')

xarr=np.arange(0.1,5.5,0.1)
yarr1=np.zeros(len(xarr))+1.02
yarr2=np.zeros(len(xarr))+0.98
plt.fill_between(xarr,yarr1,yarr2,color='grey',alpha=0.9,label='')

xarr=np.arange(0.1,5.5,0.1)
yarr1=np.zeros(len(xarr))+1.04
yarr2=np.zeros(len(xarr))+0.96
plt.fill_between(xarr,yarr1,yarr2,color='grey',alpha=0.4,label='')


plt.legend(fontsize=13)
plt.ylabel('Diameter Ratio')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    labelbottom=False) # labels along the bottom edge are off

plt.text(0.3,1.25,'(a)',fontsize=24)

plt.subplot(2,1,2)
um=np.where((rat2e < 0.05))[0]
plt.errorbar(x2[um],rat2[um],yerr=rat2e[um],fmt='o',color='grey',zorder=-32,label='')
plt.plot(x2[um],rat2[um],'o',label='')

plt.xlim([0.25,2.2])
plt.ylim([lol,upl])
#plt.plot([0.05,30],[1,1],ls='dashed',color='grey')

xarr=np.arange(0.1,5.5,0.1)
yarr1=np.zeros(len(xarr))+1.02
yarr2=np.zeros(len(xarr))+0.98
plt.fill_between(xarr,yarr1,yarr2,color='grey',alpha=0.9,label='$\sigma_{T_{eff}}$/T$_{eff}$=1%')

xarr=np.arange(0.1,5.5,0.1)
yarr1=np.zeros(len(xarr))+1.04
yarr2=np.zeros(len(xarr))+0.96
plt.fill_between(xarr,yarr1,yarr2,color='grey',alpha=0.4,label='$\sigma_{T_{eff}}$/T$_{eff}$=2%')

plt.legend(fontsize=16,loc='upper right')
plt.xlabel('Angular Diameter (mas)')
plt.ylabel('Diameter Ratio')

plt.text(0.3,1.25,'(b)',fontsize=24)

#plt.savefig('diametercomp.pdf',dpi=200)

