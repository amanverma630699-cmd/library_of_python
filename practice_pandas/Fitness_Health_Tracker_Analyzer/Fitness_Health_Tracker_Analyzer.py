import numpy as np
import pandas as pd

df=pd.read_csv('library_of_python\practice_pandas\Fitness_Health_Tracker_Analyzer\data.csv')
df['Sleep_Hours']=df['Sleep_Hours'].fillna(df.groupby('User_ID')['Sleep_Hours'].transform('median'))
df['Heart_Rate_Avg']=df['Heart_Rate_Avg'].fillna(df.groupby(['User_ID','Workout_Type'])['Heart_Rate_Avg'].transform('median'))
df['Water_Intake_L']=df['Water_Intake_L'].fillna(df.groupby('User_ID')['Water_Intake_L'].transform('median'))


def Steps_as():
    print("1.Total steps and Calories Burned")
    print("2.Average steps and Calories Burned")
    print("3.Maximum steps and Calories Burned")
    print("4.Minimum steps and Calories Burned")
    print("5.Moving average and Calories Burned")
    print("6. Total calories burned")
    print("7. Calories by workout type")
    qu=input("enter  you choose : ")
    if qu=='1':
        print(f"total steps and Calories Burned are :\n{df.groupby('User_ID')[["Steps",'Calories_Burned']].sum()}")
    elif qu=='2':
        print(f"Average steps and Calories Burned are :\n{df.groupby('User_ID')[["Steps",'Calories_Burned']].mean()}")
    elif qu=='3':
        print(f"Maximum steps and Calories Burned are :\n{df.groupby('User_ID')[["Steps",'Calories_Burned']].max()}")
    elif qu=='4':
        print(f"Minimum steps and Calories Burned are :\n{df.groupby('User_ID')[["Steps",'Calories_Burned']].min()}")
    elif qu=='5':
        print(f"Moving Average steps and Calories Burned are of 5 day :\n{df.groupby('User_ID')[["Steps",'Calories_Burned']].mean()}")
    elif qu=='6':
        print(f" Total calories burned :\n{df.groupby('User_ID')['Calories_Burned'].sum()}")
    elif qu=='7':
        print(f"Calories by workout type\n{df.groupby(['User_ID','Workout_Type'])['Calories_Burned'].sum()}")
        




def Sleep():
    print("1.Average sleep")
    print("2.Best sleep day")
    print("3.Sleep distribution")
    con=input("enter your choose :")
    if con=="1":
        print(f"average sleep \n{df.groupby('User_ID')['Sleep_Hours'].mean().round(1)}")  
    elif con=='2':  
        print(f"Best sleep day\n{df.groupby('User_ID')['Sleep_Hours'].max()}")
    elif con=='3':  
        print(f"Sleep distribution\n{df.groupby(['User_ID','Workout_Type'])['Sleep_Hours'].max()}")    



def Heart_Rate():
   print("1.Highest heart rate")
   print("2.Lowest heart rate")
   print("3.Average heart rate")
   ty=input("enter chose : ")
   if ty=="1":
        print(f"Highest heart rate\n{df.groupby('User_ID')['Heart_Rate_Avg'].mean().round(1)}")  
   elif ty=='2':  
        print(f"Lowest heart rate\n{df.groupby('User_ID')['Heart_Rate_Avg'].max()}")
   elif ty=='3':  
        print(f"Average heart rate\n{df.groupby(['User_ID','Workout_Type'])['Heart_Rate_Avg'].min()}")    


def Hydration():
     print("1.Average water intake")
     oo=input("ener choose : ")
     if oo=="1":
         print(f"average water intale \n {df.groupby('User_ID')['Water_Intake_L'].mean().round(2)}")
while True:
     print("Fitness_Health_Tracker_Analyzer  \n")
     print("Type 1.Steps  Analysis")
     print("Type 2.Sleep Analysis")
     print("Type 3.Heart Rate  Analysis")
     print("Type 4.Hydration Analysis")
     print("Type 5.to exit")

     ty=(input("enter choose : "))
     if ty=='1':
          Steps_as()
     elif ty=='2':
          Sleep()
     elif ty=='3':
          Heart_Rate()
     elif ty=='4':
          Hydration()
     elif ty=='exit':
          break
     else:
          print("error .... choose again")
     