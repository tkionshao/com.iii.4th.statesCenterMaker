import googlemaps
import re
from pprint import pprint
# from time import sleep

# GOOGLE API
class googleUClientCreater:
    def __init__(self,key):
        self.gmaps = googlemaps.Client(key=key)

    def getInformation(self,center):
        res = self.gmaps.reverse_geocode(center,language='zh-TW')
        # sleep(1)
        try:
            print('type 1')
            political_1 = res[0]['address_components'][3]['long_name']
            political_2 = res[0]['address_components'][2]['long_name']
            if ('區' not in political_1) and ('里' not in political_2):False

        except:
            print("type 2")
            political_1 = res[2]['address_components'][1]['long_name']
            political_2 = res[2]['address_components'][0]['long_name']
            # if '區' not in political_1 and '里' not in political_2:False

        finally:
            # if '區' not in political_1 or '里' not in political_2:
            #     political_1 = res[1]['address_components'][1]['long_name']
            #     political_2 = res[1]['address_components'][1]['long_name']
            return {'區': political_1, '里': political_2}

def stat_code_compute(x):
    scale_km = 0.5
    lat = x[6]
    lon = x[7]
    lat_to_km = lat*110.574
    lon_to_km = lon*(111.320*cos(lat))

    state_code_x = int(lat_to_km//scale_km)
    state_code_y = int(lon_to_km//scale_km)
    state_code = str(state_code_x)+str(state_code_y)
    return state_code

if __name__ == '__main__':

    key = 'AIzaSyAgMGyDKheHh4IfHWbzaw6-hvdgoab8nPI'
    gmaps = googlemaps.Client(key=key)
    # REGULAR
    center = (25.0329694, 121.5654177) # 25.057621	 121.523086
    print(googleUClientCreater(key).getInformation(center))
    # print(res['區'])
    # print(res['里'])

    # ERROR
    error_center  = (24.99457376960226, 121.52962267265384)
    print(googleUClientCreater(key).getInformation(error_center))

    # ERROR II
    error_center = (25.039792356250114, 121.61506875374727)
    print(googleUClientCreater(key).getInformation(error_center))

    error_center_shanghai = (31.24104300988,121.41872241448998)
    print(googleUClientCreater(key).getInformation(error_center_shanghai))

    # EERROR III
    error_center = (24.999095628267042, 121.01489550495403)
    print(googleUClientCreater(key).getInformation(error_center))
    er_cr_ls = gmaps.reverse_geocode(error_center_shanghai,language='zh-TW')
    pprint(er_cr_ls)



    # ORIGIN RESPONSE
    er_cr_ls = gmaps.reverse_geocode(error_center_shanghai,language='zh-TW')
    pprint(er_cr_ls)


    political_1 = er_cr_ls[1]['address_components'][1]['long_name']
    political_2 = er_cr_ls[1]['address_components'][1]['long_name']
    print(political_1,political_2)
    def test(political_1,political_2):
        if '區' not in political_1 and '理' not in political_2:
            return False
        else:
            return True

    test(political_1,political_2)



    # REGEX PARSER
    # er_cr_ls = gmaps.reverse_geocode(error_center,language='zh-TW')
    # print(type(er_cr_ls))
    # er_cr_ls_str = str(er_cr_ls)
    # print(type(er_cr_ls_str))
    # re.findall('''long_name': '(.+)里', 'short_name': ''',er_cr_ls_str)
