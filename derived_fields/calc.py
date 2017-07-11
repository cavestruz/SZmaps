import numpy as np
from SZmaps.utils.constants import G, kb, sigT, me, c, h, Tcmb
from SZmaps.utils.sim_props import kpcperpix, kpc2cm, Lvmax
from astropy.cosmology import Planck13


def calculate_T500(M500c, R500c) :
    return G*M500c/(2*R500c)

def calculate_ysz(ne, Te) :
    return ne * kb * Te * sigT / (me * c**2)

def YSZ( ysz, aexp=1.0, Lv=6.) :
    
    # YSZ from each cube
    dA = Planck13.angular_diameter_distance(1./aexp - 1.)
    # level and redshift dependent volume element
    Lv_width = kpchperpix * kpc2cm * 2**(Lvmax - Lv) / h
    dV = Lv_width * Lv_width * Lv_width
    return (1/dA**2) * ysz * dV

def calculate_Tsz_freq_dependence(nu) :
    x = h*nu / (kb * Tcmb)
    return x * (np.exp(x)+1.)/(np.exp(x)-1.) - 4.
