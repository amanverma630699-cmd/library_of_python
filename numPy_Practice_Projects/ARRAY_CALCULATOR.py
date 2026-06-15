# ===== ARRAY CALCULATOR =====

# 1. Create Array
# 2. View Array
# 3. Add Number
# 4. Subtract Number
# 5. Multiply Number
# 6. Divide Number
# 7. Sum
# 8. Average
# 9. Maximum
# 10. Minimum
# 11. Exit
# Enter Choice: 1
# Enter Numbers:
# 1 2 3 4 5
# Array Created Successfully!
# Enter Choice: 2
# [1 2 3 4 5]
# Enter Choice: 3
# Enter Value: 10
# [11 12 13 14 15]
# Enter Choice: 7
# Sum = 15
import numpy as np
class array_calculator:
  def __init__(self):
    self.array=np.array([])
  def create_array(self):
      self.array=np.array(list(map(int,input("Enter Numbers: ").split())))
  def view_array(self):
    print(self.array)
  def Add_Number(self,num):
    print(f"the sum of {num } on array are {self.array+num}")
  def Subtract_Number(self,num):
    print(f"the subtract of {num } on array are {self.array-num}")
  def Multiple_Number(self,num):
    if num==0:
      print("you can't multiple by zero")
    else:
      print(f"the multiple of {num } on array are {self.array*num}")
  def divide_Number(self,num):
    if num==0:
      print("you can't divide by zero")
    else:
      print(f"the divide of {num } on array are {self.array/num}")
  def array_sum(self):
    print(f"the sum array are {np.sum(self.array)}")
  def average(self):
    if self.array.size==0:
      print("array is empty")
    else:
       print(f"the average of array are {np.average(self.array)}")
  def array_max(self):
    if self.array.size==0:
      print("array is empty")
    else:
      print(f"the max of  array are {np.max(self.array)}")
  def array_min(self):
    if self.array.size==0:
      print("array is empty")
    else:
      print(f"the min of  array are {np.min(self.array)}")
arr=array_calculator()
while True:
  print("\n1. Create Array")
  print("2. View Array")
  print("3. Add Number")
  print("4. Subtract Number")
  print("5. Multiply Number")
  print("6. Divide Number")
  print("7. Sum")
  print("8. Average")
  print("9. Maximum")
  print("10. Minimum")
  print("11. Exit")
  ch=int(input("Enter Choice: "))
  if ch==1:
        arr.create_array()
  elif ch==2:
        arr.view_array()
  elif ch==3:
        num=int(input("Enter Value: "))
        arr.Add_Number(num)
  elif ch==4:
        num=int(input("Enter Value: "))
        arr.Subtract_Number(num)
  elif ch==5:
        num=int(input("Enter Value: "))
        arr.Multiple_Number(num)
  elif ch==6:
        num=int(input("Enter Value: "))
        arr.divide_Number(num)
  elif ch==7:
        arr.array_sum()
  elif ch==8:
        arr.average()
  elif ch==9:
        arr.array_max()
  elif ch==10:
        arr.array_min()
  elif ch==11:
        print("Goodbye!")
        break
  else:
        print("invalid choice")     