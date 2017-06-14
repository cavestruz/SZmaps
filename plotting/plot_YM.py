'''Plot Y vs. M at different radii'''


halo_ids = [1, 104]

aexps = ['1.0005','0.5014']
tfile = '../data/temperature_a'+aexps[0]+'_CL'+halo_ids[1]+'_N256_Lv6.fits'
rhofile = '../data/rhogas_a'+aexps[0]+'_CL'+halo_ids[1]+'_N256_Lv6.fits'

# Collect relevant halo properties
from SZmaps.IO.database import collect_halo_props
# Default has 'r200m','r500c','M_total_200m','M_total_500c'
halo_props = collect_halo_props(halo_ids, aexp=aexps[0])

# Read in fits
from SZmaps.IO.get_fits_data import get_temperature, get_rho
T = get_temperature(tfile, aexp=float(aexp))
rho = get_rho(rhofile, aexp=float(aexp))

# Derive the integrated YSZ
from SZmaps.derived_fields.calc import calculate_ysz, YSZ
YSZ_cube = YSZ(calculate_ysz(rho, T), aexp=aexps[0], Lv=6.)

# Collect value in radial region we care about - need to think about
# how to do this more generally!
####from SZmaps.calculate_scaling.scaled_halo_quantities import 
SZ_in_reg = ?????
