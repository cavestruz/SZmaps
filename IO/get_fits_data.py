from astropy.io.fits import getdata
from SZmaps.utils.constants import Om0

def get_temperature(Tfits, aexp=1.0) :
    '''Return temperature as a numpy array in K units'''
    return getdata(Tfits)


def get_rho(rhofile, aexp=1.0) :
    '''Return rho in natural units'''
    return getdata(rhofile)*(Om0/aexp)


