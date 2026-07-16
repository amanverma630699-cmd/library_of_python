import numpy as np 
def Data_Structure():
    nd=int(input("enter the number no. of day : "))
    sd=list(map(str,input("enter the item name : ").split()))
    il=len(sd)
    data=[]
    for i in range(nd):
        while True:
            ad=list(map(int,input(f"enter price of item  of day {i+1} : ").split()))
            if len(ad)==il:
                data.append(ad)
                break
            else:
                print(f"error: you enter{len(ad)},price but you have {il} item ,Try again.")
    return np.array(data),sd
data,sd=Data_Structure()
print(data)


def Total_expense():
    u=np.array(data)
    sadd=np.sum(u,axis=1,keepdims=True)
    t=np.hstack([u,sadd])
    return t

t=Total_expense()
print(t)













# - Monthly total
# - Category total
# - Highest expense category
# - Lowest expense category
# - Expenses above a threshold
# - Average spending 



