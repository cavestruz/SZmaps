import yt
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid

def plot_slices(yt_datastruct, fig_dir='.') : 
    ''' Quick check on units '''
    fig = plt.figure()

    grid = AxesGrid(fig, (0.075,0.075,0.85,0.85),
                    nrows_ncols = (2, 2),
                    axes_pad = 1.0,
                    label_mode = "1",
                    share_all = True,
                    cbar_location="right",
                    cbar_mode="each",
                    cbar_size="3%",
                    cbar_pad="0%")

    fields = ['density', 'temperature', 'szy']

    # Create the plot.  Since SlicePlot accepts a list of fields, we need only
    # do this once.
    p = yt.SlicePlot(yt_datastruct, 'z', fields)

    p.zoom(2)
    
    # For each plotted field, force the SlicePlot to redraw itself onto the AxesGrid
    # axes.
    for i, field in enumerate(fields):
        plot = p.plots[field]
        plot.figure = fig
        plot.axes = grid[i].axes
        plot.cax = grid.cbar_axes[i]
        
    # Finally, redraw the plot on the AxesGrid axes.
    p._setup_plots()

    plt.savefig('slice')
