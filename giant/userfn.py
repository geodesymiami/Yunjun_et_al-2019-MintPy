######This needs to be custom written for your stacks if needed
def makefnames(dates1,dates2,sensor):
    ####Sensor input is ignored in this case
    dirname = '/Users/yunjunz/insarlab/Galapagos/GalapagosSenDT128/ISCE/merged/interferograms'     #Relative path provided. Change to absolute path if needed.
    iname = '%s/%s_%s/filt_fine.unw'%(dirname,dates1,dates2)
    cname = '%s/%s_%s/filt_fine.cor'%(dirname,dates1,dates2)

    return iname,cname

#####To use for NSBAS
def NSBASdict():
    '''Returns a string representation of the temporal dictionary to be used with NSBAS.'''
    rep = [['POLY',[1],[tims[Ref]]],
           ['LOG'],[-2.0],[3.0]]
    return rep

#####To use for timefn invert / MInTS.
def timedict():
    '''Returns a string representation of the temporal dictionary to be used with inversions.'''
    rep = [['ISPLINES',[3],[48]]]
    return rep

############################################################
# Program is part of GIAnT v1.0                            #
# Copyright 2012, by the California Institute of Technology#
# Contact: earthdef@gps.caltech.edu                        #
############################################################

