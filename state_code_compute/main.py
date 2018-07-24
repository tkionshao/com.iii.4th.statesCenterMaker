import pandas as pd
from math import cos


def state_code_compute(x):
    scale_km = 0.5
    global lat_index, lon_index
    lat = x[lat_index]
    lon = x[lon_index]
    lat_to_km = lat*110.574
    lon_to_km = lon*(111.320*cos(lat))

    state_code_x = int(lat_to_km//scale_km)
    state_code_y = int(lon_to_km//scale_km)
    state_code = str(state_code_x)+str(state_code_y)
    return state_code

if __name__ == '__main__':
    objs = pd.read_csv('106_traffic_done.csv')
    lat_index = objs.columns.tolist().index('lat')
    lon_index = objs.columns.tolist().index('lon')
    print(lat_index,lon_index)
    objs['state_code'] = objs.apply(state_code_compute,axis=1)
    print(objs)
    objs.to_csv('../projectData/106_traffic_done.csv')
    # objs['lat']
    # objs['lon']