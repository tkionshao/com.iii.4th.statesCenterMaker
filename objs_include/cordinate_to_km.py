import pandas as pd
from math import cos

def lat_lon_to_km(lat,lon):
    lat_to_km = lat * 110.574
    lon_to_km = abs(lon * (111.320 * cos(lat)))
    return {'lat':lat_to_km,'lon':lon_to_km}

if __name__ == '__main__':

    path = '../projectData/{}_clr.csv'
    category = ['mrt','hsp_and_clc','illegal']

    obj_df = pd.read_csv(path.format(category[0]))

    print(obj_df['lat'])




    bigTable = pd.read_csv('../projectData/bigTable_much_ranger.csv')
    print(bigTable.info())

    tmp1 = bigTable.apply(lambda x: x['center'], axis=1)


    #
    # tmp1 = bigTable.apply(lambda x:x['center'],axis=1)
    # print(tmp1)