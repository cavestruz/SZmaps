''' Prints out the sz scaling '''

import L500analysis.caps.io.reader as db
from yt.units import kpc, Msun, Mpc
from SZmaps.IO import get_fits_data as gf

database_dir = '/data/avestruz/L500/databases/'
# /home/babyostrich/data/databases/
database_sim_name = 'L500_NR_0'

fits_dir = '/data/avestruz/L500/fits_cubes/'
aexp = '1.0005'

# Load the database and get properties of interest
sim = db.Simulation(database_sim_name,
                       db_dir=database_dir
                                         )
halo_ids = sim.get_halo_ids()
#halo_ids = [1]
props =['r200m','r500c','M_total_200m','M_total_500c']

halo_props = sim.get_halo_properties(halo_ids, props, aexp)

def integrate_in_yt_volume(yt_volume_type, field_name, *volume_type_params) :
    yt_volume = yt_volume_type(*volume_type_params)
    num_points = yt_volume[field_name].size
    integrated_szy = yt_volume[field_name].sum().in_units('1/Mpc')
    volume = yt_volume.volume().in_units('Mpc**3') / num_points
    
    return integrated_szy * volume


from collections import defaultdict

szy_scaling = defaultdict(list)

for halo_id in halo_ids :
    print halo_id
    szy_scaling['halo_ids'].append( halo_id )

    # Create yt datastructure
    yt_datastruct = gf.create_yt_datastruc_from_cubes(fits_dir,aexp,halo_id, 6)
    dd = yt_datastruct.all_data()

    # Get the halo properties from the database
    halo_prop = halo_props.loc[halo_props['id'] == halo_id]
    #print halo_prop
    r200m = float(halo_prop['r200m'])/.7 #* kpc 
    r500c = float(halo_prop['r500c'])/.7 #* kpc

    M200m = float(halo_prop['M_total_200m']) #* Msun
    M500c = float(halo_prop['M_total_500c']) #* Msun

    szy_scaling['r200m'].append(r200m)
    szy_scaling['r500c'].append(r500c)
    szy_scaling['M500c'].append(M500c)
    szy_scaling['M200m'].append(M200m)
    
    # Get the angular diameter distance with minimum observable redshift to 0.02
    # from yt.utilities.cosmology import Cosmology
    # cosmo = Cosmology()
    # (zi, zf) = ( 0,  max(0.02,1./float(aexp)-1.) )
    # dA = cosmo.angular_diameter_distance(zi,zf).in_units('Mpc')
    
    # Integrate in a sphere
    center = [0.5, 0.5, 0.5]
    Ysz500c = integrate_in_yt_volume( yt_datastruct.sphere, 'szy',
                                 center,(r500c,'kpc') ) 

    szy_scaling['Ysz500c'].append(Ysz500c.value)

    # Integrate in a cylinder
    radius = ( r500c, 'kpc' )
    depth = ( 3*r500c, 'kpc' )
    normal_vectors = {'x': [1,0,0],
                      'y': [0,1,0],
                      'z': [0,0,1]
    }

    
    for los, normal_vector in normal_vectors.iteritems() :
        Yszcylinder = integrate_in_yt_volume( yt_datastruct.disk, 'szy',
                                              center, normal_vector,
                                              radius, depth ) 
        szy_scaling['Yszcyl_'+los].append( Yszcylinder.value )

        
import pandas as pd

df = pd.DataFrame(szy_scaling)
df.to_csv( path_or_buf='szyscaling.csv', sep=' ', index=False )




    
        
