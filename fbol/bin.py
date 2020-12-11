import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from astropy.stats import mad_std
import pdb
from scipy import stats

def bin(xdata,ydata,sigmas,nbins):

    steps=(np.max(xdata)-np.min(xdata))/nbins
    start=np.min(xdata)
    stop=start+steps
    
    resx=np.zeros(nbins)
    resy=np.zeros(nbins)
    erry=np.zeros(nbins)
        
    
    for i in range(0,nbins):
        um=np.where( (xdata >= start) & (xdata < stop))[0]
        #print start,stop,len(um)
        if (len(um) < 5):
            start = start+steps
            stop = stop+steps
            continue
        resx[i]=start+steps/2. #np.median(xdata[um])
        resy[i]=np.median(ydata[um])
        
        #resy[i]=np.average(ydata[um],weights=sigmas[um])
        
        #print start,stop,resx[i],resy[i],len(um)
        #print xdata[um]
        #break
        #plt.clf()
        #plt.errorbar(xdata[um],ydata[um],1./sigmas[um])
        #raw_input(':')
        
        
        #pdb.set_trace()
        erry[i]=np.std(ydata[um])/np.sqrt(len(um))
        start = start+steps
        stop = stop+steps
        
    '''    
    plt.clf()
    plt.plot(xdata,ydata,'.')
    plt.errorbar(resx,resy,yerr=erry,fmt='o')
    pdb.set_trace()
    '''

    um=np.where(resy > 0.)[0]
    
    return resx[um],resy[um],erry[um]
  
def bin_time(xdata,ydata,steps):

    start=np.min(xdata)
    stop=start+steps
    
    nbins=int((np.max(xdata)-np.min(xdata))/steps)
    
    resx=np.zeros(nbins)
    resy=np.zeros(nbins)
    erry=np.zeros(nbins)
        
    
    for i in range(0,nbins):
        um=np.where( (xdata >= start) & (xdata < stop))[0]
        #pdb.set_trace()
        #print start,stop,len(um)
        if (len(um) < 5):
            start = start+steps
            stop = stop+steps
            continue
        resx[i]=start+steps/2. #np.median(xdata[um])
        resy[i]=np.median(ydata[um])
        
        #resy[i]=np.average(ydata[um],weights=sigmas[um])
        
        #print start,stop,resx[i],resy[i],len(um)
        #print xdata[um]
        #break
        #plt.clf()
        #plt.errorbar(xdata[um],ydata[um],1./sigmas[um])
        #raw_input(':')
        
        
        #pdb.set_trace()
        erry[i]=np.std(ydata[um])/np.sqrt(len(um))
        start = start+steps
        stop = stop+steps
        
    '''    
    plt.clf()
    plt.plot(xdata,ydata,'.')
    plt.errorbar(resx,resy,yerr=erry,fmt='o')
    pdb.set_trace()
    '''

    um=np.where(resy != 0.)[0]
    
    return resx[um],resy[um],erry[um]  
    
def bin_set(xdata,ydata,bins):

    nbins=len(bins)-1
    
    resx=np.zeros(nbins)
    resy=np.zeros(nbins)
    erry=np.zeros(nbins)
    
    for i in range(0,len(bins)-1):
        um=np.where( (xdata >= bins[i]) & (xdata < bins[i+1]))[0]
        
        resx[i]=(bins[i]+bins[i+1])/2.
        resy[i]=np.median(ydata[um])
        erry[i]=np.std(ydata[um])/np.sqrt(len(um))
        #print bins[i],bins[i+1],resx[i],resy[i],len(um)
        #print xdata[um]
        #break
        
    '''    
    plt.clf()
    plt.plot(xdata,ydata,'.')
    plt.errorbar(resx,resy,yerr=erry,fmt='o')
    pdb.set_trace()
    '''
    
    return resx,resy,erry
    
        
def bin_set_mean(xdata,ydata,bins):

    nbins=len(bins)-1
    
    resx=np.zeros(nbins)
    resy=np.zeros(nbins)
    erry=np.zeros(nbins)
    
    for i in range(0,len(bins)-1):
        um=np.where( (xdata >= bins[i]) & (xdata < bins[i+1]))[0]
        print(bins[i],bins[i+1])
        resx[i]=(bins[i]+bins[i+1])/2.
        resy[i]=np.mean(ydata[um])
        #resy[i]=stats.mode(ydata[um])[0]
        erry[i]=np.std(ydata[um])/np.sqrt(len(um))
        
    '''    
    plt.clf()
    plt.plot(xdata,ydata,'.')
    plt.errorbar(resx,resy,yerr=erry,fmt='o')
    pdb.set_trace()
    '''
   
def bin_cadence(x,y,ncad):
    
	resx=np.zeros(len(x))
	resy=np.zeros(len(x))
	erry=np.zeros(len(x))
	start=0
	end=ncad

	for i in range(0,len(x)-1):
		resx[i]=np.mean(x[start:end])
		resy[i]=np.mean(y[start:end])
		erry[i]=np.std(y[start:end])
		start=start+ncad
		end=end+ncad
		if (end > len(x)):
			break
			
	um=np.where(resx > 0.)[0]
			
	return resx[um],resy[um],erry[um]


