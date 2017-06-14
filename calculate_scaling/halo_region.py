from SZmaps.utils import files
from SZmaps.utils.constants import kpc2cm, h
from SZmaps.utils.sim_props import Lvmax, kpchperpix

# pre-computed from compute_cell_?d_distance_from_center()
distance_3d = files.load_pkl('../samples/distance_3d.pkl')
distance_2d = files.load_pkl('../samples/distance_2d.pkl')

def calculate_rextent_in_cube_units(r_min, r_max) :
    pass



def collect_shell_min_max_indices(r_min, r_max, cube_dist=distance_3d, r_units='r500c',halo_id=1,Lv=6, kpchperpix=3.6, cells_per_cube=256) :
    '''Returns a np.where statement for the cube'''
    r_scale = float(halo_props[r_units][halo_props['id']==halo_id]) * kpc2cm / h
    Lv_width = kpchperpix * kpc2cm * 2**(Lvmax - Lv) / h
    # compute min/max in terms of cell width
    r_min *= r_scale / Lv_width
    r_max *= r_scale / Lv_width
    return np.where( (cube_dist >= r_min)  &  (cube_dist <= r_max) ) 
