---
title: Exercise 2
linktitle: 2. Air-sea fluxes
date: '2023-03-20T00:00:00+01:00'
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
---


## Exercise sheet 2

1. Theta $\theta$-Salinity diagrams

    Make a $\theta$-S diagram using data from the Atlantic (e.g., `A16S_2005_sta085_bottle.joa`).  Here, you will want to follow the instructions for Exercise 3B on JOA for DPO (https://joa.ucsd.edu/dpo/dpo_joa_examples/chapter_3/3b.html).  Make sure to use sensible axes limits.  

    What is the median density of the profile (approximately, to the nearest 0.5 kg/m$^3$) using potential density referenced to the surface?  Using density referenced to 2000~m?



2. Heating from solar radiation:

    The effect of solar radiation on the surface layer temperature can be calculated using the equation

    $$\rho c_p {\partial T \over \partial t} = {\partial I \over \partial z}$$

    where $I$ is the downward solar radiation. On a cloudless and windless summer day, a mean irradiance of 
    $$I_o = (1 - \alpha)Q_{SW}^{\downarrow} = 300 W m^{-2}$$ is available at the sea surface for 15 hours.

     The penetration of the short-wave radiation into the ocean follows the Lambert-Beer law

    $$I(z) = I_o \exp (k_w z)$$

    ($z$ positive upwards!) What is the temperature increase within this period in a cover layer of (a) 10 m and (b) 30 m thickness if the attenuation coefficient is $k_{w}$=0.1m$^{-1}$?  Use constant values for $\rho$ und $c_p$.

3. Surface fluxes

    The NCEP/NCAR Reanalysis Project uses a weather forecast model with data assimilation to estimate the distribution of atmospheric variables from 1948 to the present. Among other things, monthly mean values of fluxes at the land-ocean-ice-atmosphere interface are given here.

    The data are available from the NCEP Reanalysis WEB site, where they can be directly displayed in maps

    (https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html).
    
    1. [1 point] Identify the different components of the heat flux between the ocean and the atmosphere.
    2. [3 points] Plot these components for the North Atlantic and Nordic Seas area (100$^\circ$W - 40$^\circ$E, 20$^\circ$N - 85$^\circ$N): (i) for the annual mean, (ii) the winter season (Jan-March), and (iii) the summer season (Jul - Sep). Use meaningful plot output options.
    3. [3 points] Discuss the relative importance of the different components and their seasonal variability either for the convective eddies of the Labrador Sea and Greenland Sea, or along the propagation path of warm Atlantic water from the Florida Strait to Norway (free choice). 
