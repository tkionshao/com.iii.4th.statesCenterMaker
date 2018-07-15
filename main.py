
import pandas as pd
from math import cos

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
    rst = pd.read_csv("data/restaurant_clean.csv")
    rst.count()
    rst_sc_ay = rst['state_code'].unique()
    rst_sc_list = rst_sc_ay.tolist()
    rst_sc_df = pd.DataFrame(rst_sc_list)
    rst_sc_df.columns = ['state_code']

    rst_sc_df['center'] = rst_sc_df['state_code'].apply(str).apply(centerProducer)
    rst_sc_df['center_lat'] = rst_sc_df['center'].apply(lambda x:x[0])
    rst_sc_df['center_lon'] = rst_sc_df['center'].apply(lambda x:x[1])
    rst_sc_df = rst_sc_df.drop(['center'],axis=1)
    print(rst_sc_df.info())

    rst_sc_df.to_csv('data/map_states_in_taipei.csv',index=False)