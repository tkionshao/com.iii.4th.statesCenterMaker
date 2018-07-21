import pandas as pd
from glob import glob
from math import pow, sqrt, cos
from datetime import datetime
import concurrent.futures
districts = ['北投區','士林區','中山區','內湖區','大同區','松山區','萬華區','中正區','大安區','信義區','南港區','文山區']

clr_data_pathes = glob('../projectData/output/*_ranger.csv')
print(clr_data_pathes)
bigTable = pd.read_csv(clr_data_pathes[0])
for i in range(1,len(clr_data_pathes)):
    data = pd.read_csv(clr_data_pathes[i])
    bigTable = bigTable.append(data)
bigTable = bigTable.drop_duplicates('state_code',keep='first').sort_values('state_code')
bigTable = bigTable[bigTable['dist'].isin(districts)].reset_index().drop(['index'],axis=1)

print(bigTable.count())
print(bigTable.groupby(['dist']).size())
print(bigTable.groupby(['dist']).size().count())
print(bigTable)
# 
# # RANGER TYPE
# def whoInRange(obj,state):
#     def coordinate_to_km(lat,lon):
#         lat_to_km = lat * 110.574
#         lon_to_km = abs(lon * (111.320 * cos(lat)))
#         return lat_to_km,lon_to_km
#
#     obj_lat = obj['lat'].tolist()
#     obj_lon = obj['lon'].tolist()
#     obj_cor = coordinate_to_km(obj_lat,obj_lon)
#     obj_x = obj_cor[0]
#     obj_y = obj_cor[1]
#     # print(type(obj_x))
#
#     state_lat = state['center_lat'].tolist()
#     state_lon = state['center_lon'].tolist()
#     state_cor = coordinate_to_km(state_lat,state_lon)
#     state_x = state_cor[0]
#     state_y = state_cor[1]
#
#     x_diff_square = pow(obj_x - state_x,2)
#     y_diff_square = pow(obj_y - state_y,2)
#     # print(x_diff_square,y_diff_square)
#     # print(sqrt((x_diff_square + y_diff_square))*1000)
#     return sqrt((x_diff_square + y_diff_square))*1000
#
# ## BigTable readiness
# bigTable_count = bigTable.count()['state_code']
# sum = bigTable_count
#
# ## Illeagal readiness
# ilg_list = glob('../projectData/hsp*')
# ilgs = pd.read_csv(ilg_list[0])
# ilg_count = ilgs.count()['state_code']
#
# # # COUNTING FUNCTION
# # def countObjs(index):
# #     objs_sum = 0
# #     global bigTable
# #     state = bigTable.loc[index,:]
# #     for j in range(ilg_count):
# #         ilg = ilgs.loc[j,:]
# #         ranger = whoInRange(ilg, state)
# #
# #         if ranger <= 1000:
# #             objs_sum += 1
# #     print(state)
# #     print(objs_sum)
# #     return objs_sum
# #     # bigTable.loc[index,'illegal_sum'] = int(objs_sum)
# #     # print(bigTable.loc[index,'illegal_sum'])
# #
# # fus = []
# # with concurrent.futures.ProcessPoolExecutor() as executor:
# #     for i in range(sum):
# #         print(i)
# #         fus.append(executor.submit(countObjs,i))
# #
# #     # for future in concurrent.futures.as_completed(fus):
# #     #     future.result()
#
#
# # print(bigTable.loc[:,'illegal_sum'])
#
# # Calculation Loop
# for i in range(sum):
#     objs_sum = 0
#     state = bigTable.loc[i, :]
#     for j in range(ilg_count):
#         ilg = ilgs.loc[j,:]
#         ranger = whoInRange(ilg, state)
#         # print(ilg_count)
#         if ranger < 3000:
#             # print(ranger)
#             objs_sum += 1
#     print(i, 'Illegal Sum:',objs_sum)
#     bigTable.loc[i,'hso_cli_sum'] = int(objs_sum)
#
# ## Hospital and Clinic
#
# ## KTV
bigTable.to_csv('partOfBigTable-{}.csv'.format(datetime.now().date()),index=False)