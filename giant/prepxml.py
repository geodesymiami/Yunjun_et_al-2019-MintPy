#! /usr/bin/env python2

import tsinsar as ts
import argparse
import numpy as np

def parse():
    parser= argparse.ArgumentParser(description='Preparation of XML files for setting up the processing chain. Check tsinsar/tsxml.py for details on the parameters.')
    parser.parse_args()

geomDir = '/Users/yunjunz/insarlab/Galapagos/GalapagosSenDT128/ISCE/merged/geom_master'
parse()
g = ts.TSXML('data')
g.prepare_data_xml('filt_fine.unw', proc='RPAC',
                   xlim=[0,1700], ylim=[400,2400],
                   rxlim=[839,841], rylim=[771,773],
                   latfile=geomDir+'/lat.rdr',
                   lonfile=geomDir+'/lon.rdr',
                   hgtfile=geomDir+'/hgt.rdr',
                   inc=33.5,
                   atmosdir='/Users/yunjunz/insarlab/WEATHER/ECMWF',
                   cohth=0.25,
                   mask='/Users/yunjunz/insarlab/Galapagos/GalapagosSenDT128/ISCE/merged/geom_master/waterMask.h5',
                   chgendian='False',
                   masktype='HDF5',
                   unwfmt='RMG',
                   corfmt='FLT',
                   demfmt='float64')
g.writexml('data.xml')


g = ts.TSXML('params')
g.prepare_sbas_xml(nvalid=300,
                   netramp=True,
                   atmos='ECMWF',
                   demerr=True,
                   uwcheck=False,
                   regu=True,
                   masterdate='20141225',
                   filt=0.01)
g.writexml('sbas.xml')


g = ts.TSXML('params')
g.prepare_mints_xml(netramp=True,
                    atmos='ECMWF',
                    demerr=True,
                    uwcheck=False,
                    regu=True,
                    masterdate='20141225')
g.writexml('mints.xml')

