from funcs import *

weather = "weather-data\A2a\HADCM3_A2a_TEMP_2020.dif"

global temps_mat, fig

temps_mat = conv(weather)[0]
temps_df = conv(weather)[1]

fig = plt.figure(figsize=(10,12))

def plotter(month):
    global cs 
    fig.canvas.draw() 
    fig.canvas.flush_events()

    ax=plt.axes(projection=ccrs.PlateCarree())

    data, lons = add_cyclic_point(temps_mat[month], coord = longitudes)

    cs = ax.contourf(lons, latitudes, data,
        transform = ccrs.PlateCarree(),cmap='Reds',extend='both')
    
    ax.coastlines()

    cb = fig.colorbar(cs, shrink = 0.35)
    
    ax.set_xticks(np.arange(-180,181,15), crs=ccrs.PlateCarree())
    lon_formatter = cticker.LongitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)

    
    ax.set_yticks(np.arange(-90,91,15), crs=ccrs.PlateCarree())
    lat_formatter = cticker.LatitudeFormatter()
    ax.yaxis.set_major_formatter(lat_formatter)

    ax.grid()

    return 


axmonth = fig.add_axes([0.15, 0.08, 0.55, 0.03])

month_slider = Slider(ax=axmonth, label='Month',
                      valmin=0, valmax=11, valinit=5, valstep=1)

plotter(0)


def update(val):
    plotter(month_slider.val)
    
    fig.canvas.draw() 
    fig.canvas.flush_events()


month_slider.on_changed(update)


plt.show()