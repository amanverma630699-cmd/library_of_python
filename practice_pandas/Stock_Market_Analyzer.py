

# - Volatility calculation
# - Trend detection

# ### NumPy Concepts

# ```
# mean()
# std()
# var()
# diff()
# cumsum()
# argmax()
# argmin()
# ```

# ### Pandas Concepts

# ```
# rolling()
# corr()
# to_datetime()
# sort_values()


import numpy as np
import pandas as pd

def add_data():
    data=[]
    while True:
          st_p_day=input("enter the price of stock( TO STOP TYPE exit ) : ")
          if st_p_day.strip().lower()=='exit':
               break
          data_stock=list(map(int,st_p_day.split()))
          data.append(data_stock)
    return np.array(data)
data=add_data()
s=data.shape
df=pd.DataFrame(data,columns=[f'stock:{i+1}'for i in range(s[-1])],index=[f'day:{i+1}'for i in range(s[-2])])

def analyze():
     df["total.price.day"]=np.sum(data,axis=1)
     df["High"]=np.max(data,axis=1) 
     df["low"]=np.min(data,axis=1)
     df["Average price"]=np.mean(data,axis=1)
     df["close"]=data[:,-1:]
     df["Daily return"]=df["close"].pct_change()
     ins=df["close"].iloc[0]
     df["Growth percentage"]=(df["close"]-ins)/ins*100
     df["volatility"]=df["Daily return"].std()*np.sqrt(252) #252 trading day in a year
     df["SMa_2"]=df["close"].rolling(window=2).mean()
     df["SMa_4"]=df["close"].rolling(window=4).mean()
     df["Trend"]=np.where(df["SMa_2"]>df["SMa_4"],"uptrend",'downtrend')
     print("best day is : ",df['total.price.day'].idxmax())
     
     

     return df
an=analyze()
print(an)