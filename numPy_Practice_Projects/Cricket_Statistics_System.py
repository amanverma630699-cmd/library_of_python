import numpy as np

def add_data():
    row1=int(input("enter number of player: "))
    columns1=int(input("enter the no. of matches: "))
    data=[]
    for i in range (row1):
       while True: 
        ir=list(map(int,input("enter the run of player in matches: ").split()))
        if len(ir)==columns1:
            data.append(ir)
            break
        else:
            print(f"you enter no of matches {columns1} but you enter {len(ir) } run of matchs in one player .try agin ")
    return np.array(data),columns1

data,column1=add_data()
print(data)
def total_runs():
   r=data.copy()
   total=np.sum(r,axis=1,keepdims=True)
   return np.hstack([r,total])
total=total_runs()
print(total)

def Batting_average():
   r=data.copy()
   avg=np.average(r,axis=1,keepdims=True)
   return np.hstack([r,avg])
avg=Batting_average()
print(avg)

def highest_scorer():
   r=data.copy()
   m=np.max(r,axis=1,keepdims=True)
   return f"the highest scorer is {np.argmax(m)} and the run is {np.max(m)}"

def Best_match_performance():
    r=data.copy()
    m=np.max(r,axis=0,keepdims=True)
    return f" the best run achive in matches is {m} "
def Century_and_fifty_finder():
    da=data.copy()
    s=np.shape(da)
    ro=s[0]
    co=s[-1]
    for i in range (ro):
        for j in range(co):
         if da[i][j]>=100:
           print(f"the player {i} in matches {j} make Centur of 100 run")
         elif da[i][j]>=50 & da[i][j]<=99:
            print(f"the player {i} in matches {j} make fifty of 50 run ")
         else:
           print("no one make century and fifty ")
    
    return 
ce=Century_and_fifty_finder()
print(ce)


def  Top_batsman ():
   da=data.copy()
   ma=np.max(da,axis=0 ,keepdims=True)
   v=np.where(ma==np.max(ma))
   s=np.shape(da)
   ro=s[0]
   co=s[-1]
   for i in range(co):
      print(f"the Top batsman  in match {i+1} is {ma[0][i]}")
   print(f"the Top batsman in all the match are player {v[0]} and made run of {np.max(ma)}  ")
   return
to=Top_batsman()
print(to)

      
