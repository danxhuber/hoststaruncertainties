Data and code to reproduce Section 2 in Tayar et al. (2020), which describes typical uncertainties on classical observables (bolometric fluxes and angular diameters) for the characterization of exoplanet host stars.

fbol/calcfbol.py requires a bolometric correction grid available here:
```
wget --no-check-certificate -r 'https://docs.google.com/uc?export=download&id=1u2CQ65UBHDDn_J4ipg2Bayv7i88R5wua' -O bcgrid.h5
```
Please cite [Choi et al. 2016](https://ui.adsabs.harvard.edu/abs/2016ApJ...823..102C/abstract) and [Huber et al. 2017](http://adsabs.harvard.edu/abs/2017ApJ...844..102H) when using the grid for your research.
