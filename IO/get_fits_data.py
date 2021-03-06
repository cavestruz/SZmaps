'''Main method to generate a yt data structure from fits cubes'''
from _tools import ytname2artname, \
        collect_art_data_arrays, calculate_length_unit_box
import numpy as np

def create_yt_datastruc_from_cubes(fitsdir, aexp, halo_id, Lv,
                                   Lbox_fits=np.array([256.,256.,256.]),
                                   max_Lv_kpc=3.8/0.7) :

        redshift = max(1/float(aexp) - 1., 0.)
        art_data_arrays = collect_art_data_arrays(fitsdir, aexp, halo_id, Lv)
        
        # Create the input data kwarg for load_uniform_grid
        data = {}

        for yt_field, art in ytname2artname.iteritems() :
            art_data_array = art_data_arrays[art['name']]
            
            if 'conversion' in art.keys() : 
		    if art_data_array.max() > 1e-14 :
			    print "in units of omM"
			    art_data_array *= art['conversion'](redshift)
            
            data[yt_field] = (art_data_array, art['units'])
            
        length_unit = calculate_length_unit_box( Lbox_fits, max_Lv_kpc, Lv, aexp )
        import yt
        return yt.load_uniform_grid(data, Lbox_fits, length_unit=length_unit)
        


