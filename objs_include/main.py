import pandas as pd
from glob import glob
from datetime import datetime
districts = ['北投區','士林區','中山區','內湖區','大同區','松山區','萬華區','中正區','大安區','信義區','南港區','文山區']

clr_data_pathes = glob('../projectData/output/*_ranger.csv')
print(clr_data_pathes)
df = pd.read_csv(clr_data_pathes[0])
for i in range(1,len(clr_data_pathes)):
    data = pd.read_csv(clr_data_pathes[i])
    df = df.append(data)
df = df.drop_duplicates('state_code',keep='first').sort_values('state_code')
df = df[df['dist'].isin(districts)]
print(df.count())
print(df.groupby(['dist']).size())
print(df.groupby(['dist']).size().count())

df.to_csv('partOfBigTable-{}.csv'.format(datetime.now().date()),index=False)
