import obs_utils as ou
def test_general_nfw_profile() :
    import numpy as np
    return ou.general_nfw_profile(np.arange(0,1000.)+np.spacing(np.float32(1e-12)), **ou.McDonald14_params['z=0.4'])

