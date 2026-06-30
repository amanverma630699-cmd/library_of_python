# Stock Market Analyzer


# - Daily change
# - Highest price
# - Lowest price
# - Average price
# - Growth %
# - Best day
# - Worst day
# - Moving average
import numpy as np

def data_strorage():
    data=[]
    number_of_days=int(input("Enter number of days to analyzer: "))
    for i in range(number_of_days):
        price=list(map(float or int,input(f"Enter price for day {i+1}: ").split()))
        data.append(price)
    return np.array(data)
data=data_strorage()

def data_summary():
    print("Data Summary:")
    print("1 for Highest Price")
    print("2 for Lowest Price")
    print("3 for Average Price")
    print("4 for Growth Percentage")
    print("5 for Best Day")
    print("6 for Worst Day")
    what=input("Enter the number of the summary you want to see: ")
    if what=="1":
        return np.max(data,axis=0,keepdims=True)
    elif what=="2":
        return np.min(data,axis=0,keepdims=True)
    elif what=="3":
        return np.mean(data,axis=0,keepdims=True)
    elif what=="4":
        return {np.diff(data,axis=0)/data[:-1]*100, np.diff(data,axis=1)/data[:-1]*100}
    elif what=="5":
        return np.argmax(data,axis=0,keepdims=True)
    elif what=="6":
        return np.argmin(data,axis=0,keepdims=True)

summary=data_summary()
print(summary)