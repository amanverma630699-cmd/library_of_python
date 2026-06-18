import numpy as np 
def Data_Structure():
    nd=int(input("enter the number no. of day : "))
    data=[]
    for i in range(nd):
        ad=list(map(int,input(f"enter price of item  of day {i+1}:").split()))
        data.append(ad)
    return np.array(data)
data=Data_Structure()
print(data)