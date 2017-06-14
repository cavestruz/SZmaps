# Get Database Contents for halo properties (200m and 500c)
import L500analysis.caps.io.reader as db

sim = db.Simulation('L500_NR_0',db_dir='/home/babyostrich/Documents/Repos/L500analysis/simulation_databases/'
                  )

def collect_halo_props(halo_ids, props=['r200m','r500c','M_total_200m','M_total_500c'], aexp='1.0005') :
    
    return halo_props = sim.get_halo_properties(halo_ids, props, aexp)
