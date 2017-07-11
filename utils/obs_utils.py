'''Tools for observational comparison'''

def general_nfw_profile(radial_bins,**kw) :
    '''General NFW pressure profile.  Requires unpacked dictionary with
parameter kwargs'''
    # p0 = kwargs.pop('p0')
    # c  = kwargs.pop('c')
    # gamma = kwargs.pop('gamma')
    # alpha = kwargs.pop('alpha')
    # beta  = kwargs.pop('beta')

    return kw['p0']*(kw['c']*radial_bins)**(-kw['gamma'])* \
        (1+(kw['c']*radial_bins)**kw['alpha'])**(-(kw['beta']-kw['gamma'])/kw['alpha'])

McDonald14_params = {
    'z=0.4':{ 'p0': 4.33, 'c': 2.59, 'gamma': 0.26, 'alpha': 1.63, 'beta': 3.3 },
    'z=0.8':{ 'p0': 3.47, 'c': 2.59, 'gamma': 0.15, 'alpha': 2.27, 'beta': 3.48 },
}

def test_general_nfw_profile() :
    import numpy as np
    return general_nfw_profile(np.arange(0,1000.), **McDonald14_params['z=0.4'])

# McDonald et al14 high and low z fitted parameters:
# param["M14lz"]  = [4.33,2.59, 0.26, 1.63,3.3]
# param["M14hz"] = [3.47,2.59, 0.15, 2.27 ,3.48]
                            
