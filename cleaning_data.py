import pandas as pd
import googlemaps
from pprint import pprint
from glmTf import googleUClientCreater


dt_bs = pd.read_csv('data/map_states_in_taipei_copy_NaN.csv')
dt_bs
# dt_bs.to_csv('data/incorrect.csv')
dt_bs[~dt_bs['dist'].isnull()].to_csv("data/map_states_in_taipei_clean_complete.csv")


key = 'AIzaSyDmjTq17LmNHYeoWhf5R57QsxqM92bvaaE'
gms = googlemaps.Client(key=key)

number = 843
dt_bs.iloc[number]['center']

point = (24.985530052272686, 121.61951637420566)
test_res = gms.reverse_geocode(point,language='zh-TW')
pprint(test_res)
political_1 = test_res[0]['address_components'][3]['long_name']
political_2 = test_res[0]['address_components'][2]['long_name']
print(political_1,political_2)

dt_bs.loc[number,'dist'] = '深坑區'
dt_bs.loc[number,'vil'] = '阿柔里'
dt_bs.iloc[number]

# DROP
dt_bs = dt_bs.drop([356],axis=0)

# OUTPUT FILE
dt_bs.to_csv('data/map_states_in_taipei_clean.csv')

# if political_1.find('區') == -1:
#     print('ok')


# GET INFORMATION FROM GOOGLEMAPS API
key = 'AIzaSyDmjTq17LmNHYeoWhf5R57QsxqM92bvaaE'
geoFunction = googleUClientCreater(key).getInformation
print(geoFunction(point))

# rst_sc_df['dist'] = rst_sc_df['center'].apply(lambda x: geoFunction(x)['區'])
# rst_sc_df['vil'] = rst_sc_df['center'].apply(lambda x: geoFunction(x)['里'])