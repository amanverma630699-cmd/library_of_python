import numpy as np
import pandas as pd

def Data_Structure():
    nd = int(input("Enter number of days: "))

    sd = input("Enter item names: ").split()
    il = len(sd)

    data = []

    for i in range(nd):
        while True:
            ad = list(map(int, input(f"Enter prices for Day {i+1}: ").split()))

            if len(ad) == il:
                data.append(ad)
                break
            else:
                print(
                    f"Error: You entered {len(ad)} prices but there are {il} items. Try again."
                )

    return np.array(data), sd


data, sd = Data_Structure()

df = pd.DataFrame(
    data,
    columns=sd,
    index=[f"Day{i+1}" for i in range(data.shape[0])]
)

print("\nOriginal Data")
print(df)


def Total_expense():

    result = df.copy()

    result["Total Spend Per Day"] = result.sum(axis=1)

    result.loc["Monthly Total"] = result.sum(axis=0)

    return result


t = Total_expense()

print("\nTotal Expense Analysis")
print(t)


def Category_Analysis():

     threshold = int(input("\nEnter threshold value: "))

     result = df.copy()
     result["Above Threshold"] = (result.where(result>threshold)).count(axis=1)
     df["Highest expense"]=df.max(axis=1)
     df["Lowest expense"]=df.min(axis=1)
     df["Average spending "]=df.mean(axis=1)
     return df
o=Category_Analysis()
print(o)

def most_expensive_category():
    result = df.copy()
    return f"\nMost Expensive Category: {result.sum(axis=0).idxmax()}"
c=most_expensive_category()
print(c)

def least_expensive_category():
    result = df.copy()
    return f"\nLeast Expensive Category: {result.sum(axis=0).idxmin()}"
d=least_expensive_category()
print(d)


def Category_Percentage():
    result=df.copy()
    category_total=result.sum(axis=0)
    overall_total=category_total.sum()
    percentage=(category_total/overall_total)*100
    print("\nCategory Percentage of Total Expenses:")
    return percentage
f=Category_Percentage()
print(f)


