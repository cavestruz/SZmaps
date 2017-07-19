import numpy as np

rbins = np.arange(.1,5.,0.01)

def plot_McDonald(rbins) :
    '''Call this to overplot McDonald best fit pressure profiles'''
    from matplotlib import pyplot as plt
    from L500analysis.plotting.tools.figure_formatting import MyLogFormatter
    from SZmaps.utils.obs_utils import general_nfw_profile, McDonald14_params

    plt.plot(rbins, general_nfw_profile(rbins,**McDonald14_params['z=0.4']),ls=':',label='M14: z=0.4')
    plt.plot(rbins, general_nfw_profile(rbins,**McDonald14_params['z=0.8']),ls=':',label='M14: z=0.8')
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('$\\tilde{P}$',fontsize='xx-large')
    plt.xlabel('r/R$_{500c}$',fontsize='xx-large')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(MyLogFormatter())
    plt.gca().yaxis.set_major_formatter(MyLogFormatter())


