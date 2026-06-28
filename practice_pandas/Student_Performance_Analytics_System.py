# Student Performance Analytics System
# What it does

# Stores marks of hundreds of students and performs complete academic analysis.

# Features
# Add student records
# Subject-wise marks
# Calculate total marks
# Calculate percentage
# Find topper
# Find weakest student
# Pass/Fail analysis
# Subject averages
# Class ranking
# Attendance analysis
# Grade generation




import numpy as np
import pandas as pd


name_class=list(map(str,input("enter the name of class : ").split()))
all_student=[]
all_subject=[]
for i in range(len(name_class)):
    name_student=list(map(str,input(f"enter the name of student of class {i+1} : ").split()))
    name_subject=list(map(str,input(f"enter the name of subject of class {i+1} : ").split()))
    all_student.append(name_student)
    all_subject.append(name_subject)



def add_student_records():
  for p in range(len(name_class)):
    total_class=len(name_class)
    total_student=all_student[p]
    total_subject=all_subject[p]
    layer,row,column=total_class,len(total_student),len(total_subject)
    all_data=np.zeros((layer,row,column))
    for i in range(layer):
        print(f"enter the data of  {i+1} : ")
        for j in range(row):
          while True:
            row_input=input(f"enter number of student{j+1} of  {name_class[i]} : ")
            row_data=np.fromstring(row_input,sep=' ')
            if row_data.size==column:
                all_data[i,j, : ]=row_data
                break
            else:
                print(f"enter the exactly number of subject of mark")
                print("enter again")
                
    return np.array(all_data)
total_data=add_student_records() 
siz1=total_data.shape
class_data={}
for i in range(siz1[0]):
   
   df=pd.DataFrame(total_data[i],columns=all_subject[i],index=[all_student[i]])
   # class_data[f"{name_class[i]}"]=pd.DataFrame(total_data[i],columns=all_subject[i],index=[all_student[i]])
   class_data[f"{name_class[i]}"]=df

for class_name, df in class_data.items():
    print(f"{class_name}:")
    print(df)
    print() # Adds a blank line between classes for readability



# Find topper
# Find weakest student
# Pass/Fail analysis
# Subject averag
# Class ranking
# Attendance analysis
# Grade generation



def data_analytics():
   data = class_data.copy()
   for class_name, df in data.items():
    df["total"] = df.sum(axis=1)
    df["percentage"] = (df["total"] / ((len(df.columns) - 2)*100)) * 100
    df["grade"] = pd.cut(df["percentage"], bins=[0, 40, 60, 80, 100], labels=["D", "C", "B", "A"])
    df["pass_fail"] = np.where(df["percentage"] >= 40, "Pass", "Fail")
    df["rank"] = df["total"].rank(ascending=False, method="min")
    df["attendance"] = np.random.randint(50, 101, size=len(df))  # Random attendance percentage
    df["attendance_status"] = np.where(df["attendance"] >= 75, "Satisfactory", "Unsatisfactory")

   for class_name, df in data.items():
    print(f"{class_name}:")
    print(df)
    print()
data1=data_analytics()
print(data1)