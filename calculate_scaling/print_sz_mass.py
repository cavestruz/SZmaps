''' Prints out the sz scaling '''

import L500analysis.caps.io.reader as db
from yt.units import kpc, Msun, Mpc
from SZmaps.IO import get_fits_data as gf

database_dir = '/data/avestruz/L500/databases/'
# /home/babyostrich/data/databases/
database_sim_name = 'L500_NR_0'

fits_dir = '/data/avestruz/L500/fits_cubes/'
aexps = ['1.0005']#, '0.5014']
Lv=6

# Load the database and get properties of interest
sim = db.Simulation(database_sim_name,
                       db_dir=database_dir
                                         )

#halo_ids = [1]
props =['r200m','r500c','r200c','M_total_200m','M_total_500c','M_total_200c']


def integrate_in_yt_volume(yt_volume_type, field_name, *volume_type_params) :
    yt_volume = yt_volume_type(*volume_type_params)
    num_points = yt_volume[field_name].size
    integrated_szy = yt_volume[field_name].sum()
    volume = yt_volume.volume().in_units('Mpc**3') / float(num_points)
    return integrated_szy * volume


from collections import defaultdict

for aexp in aexps  :

    szy_scaling = defaultdict(list)
    halo_ids = sim.get_halo_ids(aexp=aexp)
    halo_props = sim.get_halo_properties(halo_ids, props, aexp)

    for halo_id in halo_ids :
        print "reading in halo ", halo_id
        szy_scaling['halo_ids'].append( halo_id )

        # Create yt datastructure
        yt_datastruct = gf.create_yt_datastruc_from_cubes(fits_dir, aexp, halo_id, Lv)
        dd = yt_datastruct.all_data()

        # from SZmaps.plotting.slices import plot_slices
        # plot_slices(yt_datastruct)

        # Get the halo properties from the database
        halo_prop = halo_props.loc[halo_props['id'] == halo_id]   



        r200m = float(halo_prop['r200m'])/.7 #* kpc 
        r200c = float(halo_prop['r200c'])/.7 #* kpc
        r500c = float(halo_prop['r500c'])/.7 #* kpc
        
        M200m = float(halo_prop['M_total_200m']) #* Msun/h
        M200c = float(halo_prop['M_total_200c']) #* Msun/h
        M500c = float(halo_prop['M_total_500c']) #* Msun/h
        
        #szy_scaling['r200m'].append(r200m)
        szy_scaling['r200c'].append(r200c)
        szy_scaling['r500c'].append(r500c)
        szy_scaling['M200m'].append(M200m)
        szy_scaling['M200c'].append(M200c)
        szy_scaling['M500c'].append(M500c)
            
        center = [0.5, 0.5, 0.5]

        for rname, rval in [ #('r200m',r200m),
                             # ('r200c',r200c),
                ('r500c',r500c)]:#, ('1.5r500c',1.5*r500c),] :
            # Integrate in a sphere
            Yszsph = integrate_in_yt_volume( yt_datastruct.sphere, 'szy',
                                             center, (rval,'kpc') ).in_units('Mpc**2') 
            try :
                assert( Yszsph.value > 1e-9 )
            except AssertionError:
                print 'Ysz too small! ', Yszsph.value

            szy_scaling['Ysz'+rname].append(Yszsph.value)

        
        
            # Integrate in a cylinder
            radius = ( rval, 'kpc' )
            depth = ( 3*rval, 'kpc' )
            normal_vectors = {'x': [1,0,0],
                              'y': [0,1,0],
                              'z': [0,0,1]
                              }

    
            for los, normal_vector in normal_vectors.iteritems() :
                Yszcylinder = integrate_in_yt_volume( yt_datastruct.disk, 'szy',
                                                      center, normal_vector,
                                                      radius, depth ).in_units('Mpc**2')
                assert(Yszcylinder.value > 1e-7)
                szy_scaling['Yszcyl_'+los+'_'+rname].append( Yszcylinder.value )

        
    import pandas as pd
        
    df = pd.DataFrame(szy_scaling)
    df.to_csv( path_or_buf='szyscaling_a'+aexp+'_Lv'+str(Lv)+'.csv', sep=' ', index=False )

