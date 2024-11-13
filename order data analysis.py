
import kaggle






#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file





#read data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()
df.head(5)



df['profit']=df['sale_price']-df['cost_price']
df


df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")



df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)



import sqlalchemy as sal
engine = sal.create_engine('')
conn=engine.connect()




#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')

