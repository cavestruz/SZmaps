def collect_art_data_arrays (fitsdir, aexp, halo_id, Lv) :
    from glob import glob
    fitsfiles = glob( fitsdir+'/*'+str(aexp)+'*CL'+str(halo_id)+\
                      '*_Lv'+str(Lv)+'.fits' )

    # Read in as numpy arrays into a dictionary labeled with field names
    from astropy.io.fits import getdata
    return { fitsfile.split(fitsdir)[1].split('_')[0] :
             getdata(fitsfile)
             for fitsfile in fitsfiles }

def calculate_length_unit_box( Lbox_fits, max_Lv_kpc, Lv ) :
        # Define the Lbox in cm, which is the length unit of the whole box
        from yt.units import kpc
        Lbox = Lbox_fits * max_Lv_kpc * 2**(8-Lv) * kpc
        Lbox = Lbox.in_units('cm')
        return Lbox.value[0]

def _mean_matter_density(redshift) :
    from yt.utilities.cosmology import Cosmology
    cosmo = Cosmology()
    return cosmo.critical_density(0.).in_units('g/cm**3') * cosmo.omega_matter

# Map the art field name to yt field name and units
ytname2artname = {
        'density':{'name':'rhogas','conversion':_mean_matter_density,'units':'g/cm**3'},
        'temperature':{'name':'temperature','units':'K'},
        'velocity_x':{'name':'vx','units':'km/s'},
        'velocity_y':{'name':'vy','units':'km/s'},
        'velocity_z':{'name':'vz','units':'km/s'}
        }



        
            
