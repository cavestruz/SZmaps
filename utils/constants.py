from astropy.cosmology import Planck13
import astropy.constants as const

# Constants
kb = const.k_B.cgs.value # erg/K
m2cm = 100 # cm/m
Msun2g = const.M_sun.cgs.value # g/Msun
kpc2cm = const.kpc.cgs.value # cm/kpc
Mpc2cm = kpc2cm * 1/1000 
sigT = 6.65245873*10**(-29) * m2cm * m2cm # cm^2
me = const.m_e.cgs.value # g
c = const.c.cgs.value # cm/s
h = Planck13.h
rhocrit = Planck13.critical_density0.value # g/cm^3
Tcmb = Planck13.Tcmb0.value # K
Om0 = Planck13.Om0 * rhocrit # g/cm^3 
G = const.G.cgs.value 
#dA = { z: Planck13.angular_diameter_distance(z).value * Mpc2cm for z in [0, 1] }
