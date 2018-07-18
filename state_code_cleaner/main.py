import pandas as pd
import sys

def get_state_code_index(df):
     col_list = list(df.columns).index('state_code')
     return col_list

def state_code_to_int(x):
     x[i] = int(x[i])
     return x

# rst ne
def state_code_cleaner(df):
     df['len'] = df['state_code'].apply(lambda x: len(x))
     tmp1 = df[(df['len'] == 9) & (~df['state_code'].str.contains('-'))]
     tmp2 = tmp1.drop(['len'],axis=1)
     df_fn = tmp2.apply(state_code_to_int,axis=1)
     # print(tmp2.head())
     return df_fn

# print(rst_fn['state_code'])
# print(rst_fn.info())
# print(rst.info())

if __name__ == '__main__':

     fileIn = sys.argv[1]
     fileOut = fileIn[:-4] + '_cleaned.csv'

     df = pd.read_csv(fileIn)
     global i
     i = get_state_code_index(df)

     res = state_code_cleaner(df)
     # print(res.columns)
     # res = res.drop(['Unnamed: 0'],axis=1)
     # print(res.info())
     res.to_csv(fileOut,index=False)

     # print(state_code_cleaner(jb))
     # print(stae_code_cleaner(jb))
     # print(list(rst.columns).index('len'))
     # rst_fn.to_csv('data/restaurant_clean.csv')