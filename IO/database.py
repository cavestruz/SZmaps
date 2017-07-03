# Get Database Contents for halo properties (200m and 500c)
import L500analysis.caps.io.reader as db

sim = db.Simulation('L500_NR_0',db_dir='/home/babyostrich/data/databases/'
                  )
halo_ids = sim.get_halo_ids()

def collect_halo_props(halo_ids=halo_ids, props=['r200m','r500c','r200c', 'M_total_200m','M_total_500c', 'M_total_200c'], aexp='1.0005') :
    
    return sim.get_halo_properties(halo_ids, props, aexp)
