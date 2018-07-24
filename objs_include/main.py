import pandas as pd
import cordinate_to_km
from math import pow, sqrt
import numpy as np
from datetime import datetime
# import sys

def calculation_dist(obj_xy_list,state_center):
    count = 0
    ranger = 0
    ranger_list = []
    for objs_xy in objs_xy_list:
        x_dist = objs_xy[0] - state_center[0]
        y_dist = objs_xy[1] - state_center[1]
        range = round(sqrt(pow(x_dist,2)+pow(y_dist,2)),3)

        # IF RANGE IN 1.5 KM
        if range < 1.5:
            # ranger += range
            count += 1
            ranger_list.append(range)
    if count == 0:
        return 0
    # IF THERE HAS ANY ONJS, GET ITS STANDARD DEVIATION
    else:
        # res = round(ranger / count,2)
        ranger_np = np.array(ranger_list)
        return np.std(ranger_np,axis=0)

if __name__ == '__main__':
    # CALCULATE KM IN BIG TABLE
    bigTable = pd.read_csv('partOfBigTable-2018-07-24.csv')
    print(bigTable.info())

    bigTable['km_x'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lat'], axis=1)
    bigTable['km_y'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lon'], axis=1)

    # print(bigTable.info())

    # OBJECTS
    ## SINGLE ONE TEST
    path = '../projectData/{}_clr.csv'
    category = ['mrt', 'hsp_and_clc', 'illegal','night_club','ubike','edu_all_statecode','106_traffic_done']
    # num = int(sys.argv[1])
    for num in range(len(category)):
        obj_df = pd.read_csv(path.format(category[num]))
        obj_df['km_x'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lat'], axis=1)
        obj_df['km_y'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lon'], axis=1)
        print(obj_df.info())
        objs_xy_list = list(zip(obj_df['km_x'].tolist(),obj_df['km_y'].tolist()))

        for i in range(bigTable.count()['state_code']):
            state_center_km = bigTable.loc[i,'km_x'],bigTable.loc[i,'km_y']
            # print(state_center_km)
            # print(objs_x_list)
            # print(objs_y_list)
            bigTable.loc[i,category[num]] = calculation_dist(objs_xy_list,state_center_km)

        res = bigTable[bigTable[category[num]] > 1].sort_values(category[num],ascending=False)
        print(res)
        print('==== =Top 10 {} ====='.format(category[num]))
        print(res[0:9].to_string())
        print(res[0:49].groupby('dist').size())
        # print(bigTable[bigTable['state_code'] == 553526927]['center'])
    print(bigTable.info())
    bigTable.to_csv('objs_in_range_{}.csv'.format(datetime.now().date()),index=False)
    print(bigTable.to_string())