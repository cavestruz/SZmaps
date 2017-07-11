'''Tools for observational comparison'''

def general_nfw_profile(radial_bins,**kw) :
    '''General NFW pressure profile.  Requires unpacked dictionary with
parameter kwargs'''

    import numpy as np
    return kw['p0']*(kw['c']*radial_bins)**(-kw['gamma'])* \
        (1+(kw['c']*radial_bins)**kw['alpha'])**(-(kw['beta']-kw['gamma'])/kw['alpha'])

McDonald14_params = {
    'z=0.4':{ 'p0': 4.33, 'c': 2.59, 'gamma': 0.26, 'alpha': 1.63, 'beta': 3.3 },
    'z=0.8':{ 'p0': 3.47, 'c': 2.59, 'gamma': 0.15, 'alpha': 2.27, 'beta': 3.48 },
}

def test_general_nfw_profile() :
    import numpy as np
    return general_nfw_profile(np.arange(0,1000.), **McDonald14_params['z=0.4'])

                            
