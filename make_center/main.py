import pandas as pd
from math import cos
from glmTf import googleUClientCreater
import sys

def centerProducer(state_code):
    scale_km = 0.5
    x_code = int(state_code[:4]) + 0.5
    y_code = int(state_code[4:]) + 0.5

    x_code_m_scale = x_code * scale_km
    y_code_m_scale = y_code * scale_km

    x_code_to_lat = float(x_code_m_scale) / 110.574
    cosine_ = abs(cos(x_code_to_lat))
    y_code_to_lat = float(y_code_m_scale) / (111.320 * cosine_)

    return x_code_to_lat, y_code_to_lat

def centerSept(x):pass

if __name__ == '__main__':

    # IO
    fileIn = sys.argv[1]
    fileOut = fileIn[:-4]+'_stcode_range.csv'

    # READ DATA
    df = pd.read_csv(fileIn)
    # rst = pd.read_csv("../data/og/restaurant_clean.csv")
    # rst = rst[rst['status'] != '已歇業']
    # rst.count()
    df_sc_ay = df['state_code'].unique()
    df_sc_list = df_sc_ay.tolist()
    df_sc_df = pd.DataFrame(df_sc_list)
    df_sc_df.columns = ['state_code']

    # PRODUCE COLUMNS WHICH ARE LAT AND LON OF CENTER
    df_sc_df['center'] = df_sc_df['state_code'].apply(str).apply(centerProducer)
    df_sc_df['center_lat'] = df_sc_df['center'].apply(lambda x:x[0])
    df_sc_df['center_lon'] = df_sc_df['center'].apply(lambda x:x[1])
    # rst_sc_df = rst_sc_df.drop(['center'],axis=1)

    print(df_sc_df['center'].head(1))

    # GET INFORMATION FROM GOOGLEMAPS API
    key = 'AIzaSyDmjTq17LmNHYeoWhf5R57QsxqM92bvaaE'
    geoFunction = googleUClientCreater(key).getInformation
    df_sc_df['dist'] = df_sc_df['center'].apply(lambda x: geoFunction(x)['區'])
    df_sc_df['vil'] = df_sc_df['center'].apply(lambda x: geoFunction(x)['里'])

    # DROP NULL AND OUTPUT FILE
    df_sc_df[~df_sc_df['dist'].isnull()].to_csv(fileOut, index=False)
    # df_sc_df[~df_sc_df['dist'].isnull()].to_csv('../data/map_states_tpe_csv',index=False)

    # print(rst_sc_df.info())
    # rst_sc_df.to_csv('data/map_states_in_taipei_copy_clean_complete.csv',index=False)
