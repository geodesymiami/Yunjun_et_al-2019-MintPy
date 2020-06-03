## Jupyter Notebooks for: ##

Yunjun, Z., H. Fattahi, F. Amelung (2019), Small baseline InSAR time series analysis: Unwrapping error correction and noise reduction, _Computers & Geosciences_, _133_, 104331, doi:[10.1016/j.cageo.2019.104331](https://doi.org/10.1016/j.cageo.2019.104331), [arXiv](https://eartharxiv.org/9sz6m/), [code](https://github.com/insarlab/MintPy).

### Data ([zenodo](https://zenodo.org/record/3464191)) ###

The Sentinel-1 and ALOS-1 InSAR time-series for Galápagos volcanoes are available at https://zenodo.org/record/3464191.

#### Dataset 1: ALOS-1 ascending track 133 frame 7160-7180 ####

+ Date: 15 Jan 2007 - 13 Mar 2011 (22 acquisitions)
+ Processor: ROI_PAC + [MintPy](https://github.com/insarlab/MintPy)
+ Configuration: [GalapagosAlosAT133.template](./configs/GalapagosAlosAT133.template)
+ Interferogram stack: [GalapagosAlosAT133.tar.xz](https://zenodo.org/record/3464191/files/GalapagosAlosAT133.tar.xz) (5.8 GB)
+ Displacement time-series (HDF-EOS5): [ALOS_SM_131_7160_7180_20070115_20110313.he5](https://zenodo.org/record/3464191/files/ALOS_SM_131_7160_7180_20070115_20110313.he5) (140 MB)
+ Displacement time-series (KMZ): [ALOS_SM_131_7160_7180_20070115_20110313.kmz](https://zenodo.org/record/3464191/files/ALOS_SM_131_7160_7180_20070115_20110313.kmz) (28 MB)
+ Volcanic events:
   - Alcedo: 2010 non-eruptive unrest
   - Fernandina: April 2009 eruption
   - Cerro Azul: 2008 eruption

#### Dataset 2: Sentinel-1 descending track 128 frame 593-597 ####

+ Date: 13 Dec 2014 - 19 Jun 2018 (98 acquisitions)
+ Processor: [ISCE](https://github.com/isce-framework/isce2)/[topsStack](https://github.com/isce-framework/isce2/blob/master/contrib/stack/topsStack/README.md) + [MintPy](https://github.com/insarlab/MintPy)
+ Configuration: [GalapagosSenDT128.template](./configs/GalapagosSenDT128.template)
+ Interferogram stack: [GalapagosSenDT128.tar.xz](https://zenodo.org/record/3464191/files/GalapagosSenDT128.tar.xz) (21.5 GB)
+ Displacement time-series (HDF-EOS5): [S1_IW12_128_0593_0597_20141213_20180619.he5](https://zenodo.org/record/3464191/files/S1_IW12_128_0593_0597_20141213_20180619.he5) (1.3 GB)
+ Displacement time-series (KMZ): [S1_IW12_128_0593_0597_20141213_20180619.kmz](https://zenodo.org/record/3464191/files/S1_IW12_128_0593_0597_20141213_20180619.kmz) (73 MB)
+ Volcanic events:
   - Wolf: May 2015 eruption
   - Fernandina: September 2017 eruption (GVP, 2018) and June 2018 eruption (GVP, 2018)
   - Sierra Negra: inflation prior to the 26 June 2018 eruption (GVP, 2018)
   - Cerro Azul: March 2017 dike intrusion

HDF-EOS5 file structure is described in https://mintpy.readthedocs.io/en/latest/hdfeos5.

### Figures ([nbviewer](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/tree/master/))  

NOTE: This notebook is based on the released version of [MintPy-1.2](https://github.com/insarlab/MintPy/releases/tag/v1.2.0) and NOT maintained for future development. All figures are plotted using [matplotlib](https://matplotlib.org/).

+ [Fig. 1](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_01_S02_S12_S13_sim_weightFunc.ipynb) - Performance of four weight functions.
+ [Fig. 2](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_02_S03_sim_bridging.ipynb) - Phase-unwrapping error correction with bridging.
+ [Fig. 3](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_03_closurePhase_stat.ipynb) - Characteristics of phase-unwrapping error in the closure phase.
+ [Fig. 4](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_04_sim_phaseClosure.ipynb) - Phase-unwrapping error correction with phase closure.
+ [Fig. 5](https://nbviewer.jupyter.org/github/insarlab/MintPy-tutorial/blob/master/docs/smallbaselineApp_workflow.png) - Routine workflow.
+ [Fig. 6](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_06_velocity_GalapagosSenDT128.ipynb) - Velocity at Isabela, Fernandina and Santiago islands.
+ [Fig. 7](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_07_timeseries_FernandinaSenDT128.ipynb) - Displacement time-series at Fernandina island.
+ [Fig. 8](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_08_S06_InSAR_vs_GPS.ipynb) - Comparing InSAR with GPS.
+ [Fig. 9](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_09_unwrapError_GalapagosSenDT128.ipynb) - Assessment of phase-unwrapping error correction using temporal coherence.
+ [Fig. 10](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_10_cohNetModify_tempCoh.ipynb) - Impact of network modification using temporal coherence.
+ [Fig. 11](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_11_netInv_decorNoiseFilter.ipynb) - Spatial inspection of the inverted raw phase.
+ [Fig. 12](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_12_S07_noisyAcquisition_residualPhase.ipynb) - Impact of noisy acquisitions on velocity estimation.
+ [Fig. 13](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_13_phaseCorrection_timeseries.ipynb) - Phase corrections in the time-series domain.
+ [Fig. 14](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_14_S08_network_redundancy.ipynb) - Impact of network redundancy.
+ [Fig. 15](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_15_tempCoh_limits.ipynb) - Advantage and limitation of temporal coherence as reliability measure.
+ [Fig. 16](https://nbviewer.jupyter.org/github/geodesymiami/Yunjun_et_al-2019-MintPy/blob/master/Fig_16_S09_MintPy_vs_GIAnT.ipynb) - Comparing MintPy with GIAnT.
