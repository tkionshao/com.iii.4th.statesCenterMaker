import pandas as pd
import cordinate_to_km
from math import pow, sqrt

def calculation_dist(obj_xy_list,state_center):
    count = 0
    for objs_xy in objs_xy_list:
        x_dist = objs_xy[0] - state_center[0]
        y_dist = objs_xy[1] - state_center[1]
        range = round(sqrt(pow(x_dist,2)+pow(y_dist,2)),3)
        if range < 1.5:
            print(range)
            count += 1
    return count

if __name__ == '__main__':
    # CALCULATE KM IN BIG TABLE
    bigTable = pd.read_csv('../projectData/bigTable_much_ranger.csv')
    print(bigTable.info())

    bigTable['km_x'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lat'], axis=1)
    bigTable['km_y'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lon'], axis=1)

    print(bigTable.info())

    # OBJECTS
    ## SINGLE ONE TEST
    path = '../projectData/{}_clr.csv'
    category = ['mrt', 'hsp_and_clc', 'illegal']

    obj_df = pd.read_csv(path.format(category[0]))
    obj_df['km_x'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lat'], axis=1)
    obj_df['km_y'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lon'], axis=1)
    print(obj_df.info())
    objs_xy_list = list(zip(obj_df['km_x'].tolist(),obj_df['km_y'].tolist()))

    for i in range(bigTable.count()['state_code']):
        state_center_km = bigTable.loc[i,'km_x'],bigTable.loc[i,'km_y']
        print(state_center_km)
        # print(objs_x_list)
        # print(objs_y_list)
        bigTable.loc[i,category[0]] = calculation_dist(objs_xy_list,state_center_km)

    print(bigTable[bigTable[category[0]] > 1].sort_values(category[0]))
    print(bigTable[bigTable['state_code'] == 553526927]['center'])