from imports import *

global month, longitudes, latitudes, latwind, coords, coord_wind

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

longitudes = np.arange(0,360,3.75)

latitudes = np.arange(90,-92.5,-2.5)
latwind = np.arange(88.75,-91.25,-2.5)

long_mesh, lat_mesh = np.meshgrid(longitudes, latitudes)
wlong_mesh, wlat_mesh = np.meshgrid(longitudes, latwind)

coords = np.column_stack((long_mesh.ravel(), lat_mesh.ravel()))
coords_wind = np.column_stack((wlong_mesh.ravel(), wlat_mesh.ravel()))


def conv(file):
    var = []
    climate = {}
    
    with open(file) as f:
        lines = f.readlines()

        for l in lines:
            if "7008" in l:
                pass
            elif "6912" in l:
                pass
            else:
                ts = l.split(' ')
                ts = [t for t in ts if t != '']
                for item in ts:
                    try:
                        var.append(float(item))
                    except: 
                        break          

    monthly_var = []

    for i in range(0, len(var), int(len(var)/len(month))):
        monthly_var.append(var[i : i + int(len(var)/len(month))])

    for i in range(0, 12):
        climate[month[i]] = monthly_var[i]

    df = pd.DataFrame(climate)

    if 'WIND' in file:
        mat = df.to_numpy().transpose().reshape(12,72,96)
        df['Longitude'] = coords_wind[:,0]
        df['Latitude'] = coords_wind[:,1] 
    else:
        mat = df.to_numpy().transpose().reshape(12,73,96)
        df['Longitude'] = coords[:,0]
        df['Latitude'] = coords[:,1]


    return mat, df, len(var)  