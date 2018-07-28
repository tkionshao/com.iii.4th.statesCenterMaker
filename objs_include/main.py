import pandas as pd
# import cordinate_to_km
import math
import numpy as np
from datetime import datetime
# import sys

def calculation_dist(destination,origin):
    count = 0
    ranger = 0
    ranger_list = []
    for single_objs in destination:
        lat1, lon1 = origin
        lat2, lon2 = single_objs
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        range = radius * c

        # IF RANGE IN 1.5 KM
        if range < 1.5:
            # ranger += range
            count += 1
            ranger_list.append(range)
    if count == 0:
        return 0
    # IF THERE HAS ANY ONJS INCLUDED, GET ITS STANDARD DEVIATION
    else:
        # res = round(ranger / count,2)
        ranger_np = np.array(ranger_list)
        return np.std(ranger_np,axis=0)

if __name__ == '__main__':
    # CALCULATE KM IN BIG TABLE
    bigTable = pd.read_csv('partOfBigTable-2018-07-24.csv')
    print(bigTable.info())

    # bigTable['km_x'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lat'], axis=1)
    # bigTable['km_y'] = bigTable.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['center_lat'],x['center_lon'])['lon'], axis=1)

    # print(bigTable.info())

    # OBJECTS
    ## SINGLE ONE TEST
    path = '../projectData/{}_clr.csv'
    category = ['mrt', 'hsp_and_clc', 'illegal','night_club','ubike','edu_all_statecode','106_traffic_done']
    # num = int(sys.argv[1])
    for num in range(len(category)):
        obj_df = pd.read_csv(path.format(category[num]))
        # obj_df['km_x'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lat'], axis=1)
        # obj_df['km_y'] = obj_df.apply(lambda x: cordinate_to_km.lat_lon_to_km(x['lat'],x['lon'])['lon'], axis=1)
        print(obj_df.info())
        objs_loc = list(zip(obj_df['lat'].tolist(),obj_df['lon'].tolist()))

        for i in range(bigTable.count()['state_code']):
            state_center = bigTable.loc[i,'center_lat'],bigTable.loc[i,'center_lon']
            bigTable.loc[i,category[num]] = calculation_dist(objs_loc,state_center)

        res = bigTable[bigTable[category[num]] > 1].sort_values(category[num],ascending=False)
        print(res)
        print('==== =Top 10 {} ====='.format(category[num]))
        print(res[0:9].to_string())
        print(res[0:49].groupby('dist').size())
        # print(bigTable[bigTable['state_code'] == 553526927]['center'])
    print(bigTable.info())
    bigTable.to_csv('objs_in_range_{}.csv'.format(datetime.now().date()),index=False)
    print(bigTable.to_string())