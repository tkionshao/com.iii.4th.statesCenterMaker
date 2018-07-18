import googlemaps
import re
from pprint import pprint

# ERROR

# GET INFORMATION
key = 'AIzaSyAgMGyDKheHh4IfHWbzaw6-hvdgoab8nPI'
geoFunction = googleUClientCreater(key).getInformation
centers = rst_sc_df['center'].tolist()

# CHECK INTO WRONG INDEX
i = 0
for ctr in centers:
    res = geoFunction(ctr)
    print(res ,i)
    i += 1

# TRY ONE CENTER
num = 872
list_num = [1 ,2 ,3 ,4 ,5]
rst_sc_df.iloc[num  ]  # ['center']
rst[rst['state_code'] == 534915749]['Address']
geoFunction(rst_sc_df.iloc[num]['center'])

# FROM ADDERESS TO GET STATECODE

# Addr
addr = '台北市北投區大同街337號'
pprint(gmaps.geocode(addr, language='zh-tw'))

# STATE CODE
def stat_code_compute(x):
    scale_km = 0.5
    lat = x[0]
    lon = x[1]
    lat_to_km = lat * 110.574
    lon_to_km = lon * (111.320 * cos(lat))

    state_code_x = int(lat_to_km // scale_km)
    state_code_y = int(lon_to_km // scale_km)
    state_code = str(state_code_x) + str(state_code_y)
    return state_code

missing_data_latlon = [25.140829 ,121.499329]
stat_code_compute(missing_data_latlon)
