from imports import *

global month, longitudes, latitudes, coords

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

longitudes = np.arange(0,360,3.75)
latitudes = np.arange(90,-92.5,-2.5)
#latitudes = np.arange(0,182.5,2.5)

long_mesh, lat_mesh = np.meshgrid(longitudes, latitudes)
coords = np.column_stack((long_mesh.ravel(), lat_mesh.ravel()))

def conv(file):
    global month 
    var_line = []
    var = []
    weather = {}

    
    with open(file) as f:
        lines = f.readlines()

        for l in lines:
            if "7008" in l:
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
        weather[month[i]] = monthly_var[i]

    df = pd.DataFrame(weather)

    mat = df.to_numpy().transpose().reshape(12,73,96)
    #mat = np.roll(mat, 48, axis=2)

    df['Longitude'] = coords[:,0]
    df['Latitude'] = coords[:,1]

    return mat, df  