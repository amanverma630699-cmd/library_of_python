import numpy as np
import pandas as pd

df=pd.read_csv('library_of_python/practice_pandas/movie_rating_&_recommendation_dash/movies_dashboard_dataset_200rows.csv')
df['Director']=df['Director'].fillna(0)
df['Language']=df['Language'].fillna("english")
df['Budget_Million']=df['Budget_Million'].fillna(df['Budget_Million'].mean())
df['Revenue_Million']=df['Revenue_Million'].fillna(df['Budget_Million'].mean())
df['Rating']=df['Rating'].fillna(df['Rating'].mean())
df['Votes']=df['Votes'].fillna(0)
# print(df.isnull().sum())
# print(df)


def Ratings():
    print(f"Highest rated movie :{'\n'}{df[df['Rating']==df['Rating'].max()]}")
    print(f"Lowest rated movie :{'\n'}{df[df["Rating"]==df['Rating'].min()]}")
    print(f" Top 10 movies rated :{'\n'}{df.nlargest(10,'Rating')}")
    print(f"the Average rating :{'\n'}{df['Rating'].mean():.2f}")
    print(f"the Median rating :{'\n'}{df['Rating'].median():.2f}")

# Rt_dic=Ratings()


def Revenue_Analysis():
    print(f"Highest revenue movie :{'\n'}{df[df['Revenue_Million']==df['Revenue_Million'].max()]}")
    print(f"{'\n'}Lowest revenue movie :{'\n'}{df[df["Revenue_Million"]==df['Revenue_Million'].min()]}")
    print(f"{'\n'}Top 10 movies revenue :{'\n'}{df.nlargest(10,'Revenue_Million')}")
    print(f"{'\n'}the Average revenue :{'\n'}{df['Revenue_Million'].mean():.2f} Million")
    print(f"the Total box office collection  :{'\n'}{df['Revenue_Million'].sum():.2f} Million")
# re_as=Revenue_Analysis()

def Budget_Analysis():
    print(f"Most expensive movie :{'\n'}{df[df['Budget_Million']==df['Budget_Million'].max()]}")
    print(f"{'\n'}chepest movie :{'\n'}{df[df["Budget_Million"]==df['Budget_Million'].min()]}")
    print(f"{'\n'}Top 10 movies expensive :{'\n'}{df.nlargest(10,'Budget_Million')}")
    print(f"{'\n'}the Average expensive :{'\n'}{df['Budget_Million'].mean():.2f} Million")
    
    
# bu_as=Budget_Analysis()

def Profit_Analysis():
    df["Profit"]=(df['Revenue_Million']-df['Budget_Million']).round(1)
    print(f"Most profited movie :{'\n'}{df[df['Profit']==df['Profit'].max()]}")
    print(f"{'\n'}least profited movie :{'\n'}{df[df["Profit"]==df['Profit'].min()]}")
    print(f"{'\n'}Top 10 movies profited :{'\n'}{df.nlargest(10,'Profit')}")
    print(f"{'\n'}the Average profited :{'\n'}{df['Profit'].mean():.2f} Million")
    

# po_as=Profit_Analysis()

def Genre_Analysis():
    print(f"Best genre by average rating :{'\n'}{df.groupby('Genre')['Rating'].mean()}")
    df["Profit"]=(df['Revenue_Million']-df['Budget_Million']).round(1)
    print(f"Most profitable genre :{'\n'}{df.groupby('Genre')['Profit'].max()}")
    print(f"Number of movies per genre :{'\n'}{df.groupby('Genre')['Movie_ID'].count()}")

# ge_as=Genre_Analysis()

def  Year_Analysis():
        df["Profit"]=(df['Revenue_Million']-df['Budget_Million']).round(1)
        print(f"Best year for movies:{'\n'}{df.groupby('Release_Year')['Profit'].max()}")
        print(f"Movies released per year:{'\n'}{df.groupby('Release_Year')['Movie_ID'].count()}")
        print(f"Movies released per year:{'\n'}{df.groupby('Release_Year')['Rating'].mean().round}")

# ye_as=Year_Analysis()

def Duration_Analysis():
    print(f"Longest movie :{'\n'}{df[df['Duration_Min']==df['Duration_Min'].max()]}")
    print(f"{'\n'}Shortest movie :{'\n'}{df[df["Duration_Min"]==df['Duration_Min'].min()]}")
    print(f"{'\n'}Top 10 Longest movie :{'\n'}{df.nlargest(10,'Duration_Min')}")
    print(f"{'\n'}Average duration :{'\n'}{df['Duration_Min'].mean():.2f} Million")
# du_as=Duration_Analysis()

def Voting_Analysis():
     print(f"most voted movie :{'\n'}{df['Votes'].max()}")
     print(f"most voted movie :{'\n'}{df['Votes'].mean().round(1)}")
# vo_as=Voting_Analysis()

def compearing():
     print(f"Budget vs Rating :{'\n'}{df.groupby(pd.qcut(df['Budget_Million'],q=3,labels=["low Budget","med Budget","high Budget"]),observed=False)['Rating'].mean().round(1)}")
     print(f"\nDuration vs Rating :{'\n'}{df.groupby(pd.qcut(df['Duration_Min'],q=3,labels=["low Duration","med Duration","high Duration"] ),observed=False)['Rating'].mean().round(1)}")
     print(f"\nVotes vs Rating :{'\n'}{df.groupby(pd.qcut(df['Votes'],q=3,labels=["low Votes","med Votes","high Votes"] ),observed=False)['Rating'].mean().round(1)}")
# co_as=compearing()




while True:
     print("movie Analysis \n")
     print("Type 1.Ratings  Analysis")
     print("Type 2.Revenue Analysis")
     print("Type 3.Budget Analysis")
     print("Type 4.Profit Analysis")
     print("Type 5.Genre Analysis")
     print("Type 6.Year Analysis")
     print("Type 7.Duration Analysis")
     print("Type 8.Voting Analysis")
     print("Type 9.compearing ")
     print("Type 10.for exit ")

     ty=(input("enter choose : "))
     if ty=='1':
          Ratings()
     elif ty=='2':
          Revenue_Analysis()
     elif ty=='3':
          Budget_Analysis()
     elif ty=='4':
          Profit_Analysis()
     elif ty=='5':
          Genre_Analysis()
     elif ty=='6':
          Year_Analysis()
     elif ty=='7':
          Duration_Analysis()
     elif ty=='8':
          Voting_Analysis()
     elif ty=='9':
          compearing()
     elif ty=='10':
          break
     else:
          print("error .... choose again")
     