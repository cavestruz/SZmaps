''' Collection of functions to calculate mass and redshift dependent assumed scalings. '''

from astropy.cosmology import WMAP9 as cosmo

def pressure_critical_scaling(aexp=None, mass=None) :
    '''Calculates P_deltac.  Part of profile_scaling_function_collections. 
    Returns P_deltac in erg/cm**3. M_deltac (mass) expected in Msun/h'''
    
    return 1.45*1e-11 * (mass / 1e15)**(2./3) * cosmo.efunc(1./float(aexp) - 1.)**(8./3)
            
def pressure_mean_scaling(aexp=None, mass=None) :
    '''Calculates P_deltam.  Part of profile_scaling_function_collections. 
    Returns P_deltam in erg/cm**3.  M_deltam (mass) expected in Msun/h'''

    return 1.45*1e-11 * (mass/1e15)**(2./3) * (1./aexp)**(8./3)
        
def temperature_critical_scaling(aexp=None, mass=None) :
    '''Calculates T_deltac.  Part of profile_scaling_function_collections. 
    Returns T_deltac in keV. M_deltac (mass) expected in Msun/h'''

    return 11.05 * (mass/1e15)**(2./3) * cosmo.efunc(1./float(aexp)-1.)**(2./3)


def temperature_mean_scaling(aexp=None, mass=None) :
    '''Calculates T_deltam.  Part of profile_scaling_function_collections. 
    Returns T_deltam in keV. M_deltam (mass) expected in Msun/h'''

    return 11.05 * (mass/1e15)**(2./3) * (1./float(aexp))**(2./3)


def entropy_critical_scaling(aexp=None, mass=None) :
    '''Calculates K_deltac.  Part of profile_scaling_function_collections. 
    Returns K_deltac in keV/cm**2. M_deltac (mass) expected in Msun/h'''

    return 1963 * (mass/1e15)**(2./3) * cosmo.efunc(1./float(aexp)-1.)**(-2./3)

def entropy_mean_scaling(aexp=None, mass=None) :
    '''Calculates K_deltam.  Part of profile_scaling_function_collections. 
    Returns K_deltam in keV/cm**2. M_deltam (mass) expected in Msun/h'''

    return 1963 * (mass/1e15)**(2./3) * (1./aexp)**(-2./3)
