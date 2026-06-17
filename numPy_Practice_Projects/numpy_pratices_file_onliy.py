# import numpy as np
# n= np.array([[2,4],[5,6]])
# b=np.array([[4,5], [6,7]])
# ar=np.concatenate((n,b),axis=1)
# print(ar)
# # lis=[1,2,3,5,4,5,3,4,3,4,3,4,3,4,3,4,3,43,3,]
# # r=lis[3:9]
# # r[1:3]=67
# # print(r)
# # arr=np.array([[1,2,3,2,3],
# #               [4,5,6,4,5],
# #               [7,8,9,7,8]])
# arr=np.array([[[1,2,3,2,3],
#               [4,5,6,4,5],
#               [7,8,9,7,8]],
#               [[3,2,3,2,3],
#               [4,5,6,4,5],
#               [7,4,9,7,8]]])
# # arr=np.array([
#             #    [1,4,5]])
# # arr1=arr[:2,1:3]
# # print(arr.ndim)
# # print(arr1)

# # arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# # r=arr[1,0:3,0:2]
# # r[0:3,0:2]=67
# # print(r)
# ar=arr[0:2].copy()
# print(ar)
# s=np.arange(1,10).reshape(3,3)
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# # c=np.concatenate((s,b),axis=0) # 0==down 1==right

# print(c)


# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# a1,a2,a3=np.split(arr,[2,2])
# print(a1)
# print(a2)
# print(a3)
import numpy as np
import pandas as pd
class student:
  def __init__(self):
    self.data= np.array([])
  def Add_data(self,data):
    self.data=np.array(data)
    print(self.data)
  def Total(self):
      n=(np.sum(self.data, axis=1)).reshape(-1,1)
      s=np.append(self.data,n,axis=1)
      print(s)
      
      
  def average(self):
    p=np.average(self.data,axis=1).reshape(-1,1)
    s=np.hstack([self.data,p])
    print(s)

  def pass_fail(self):
    if  self.data.size==0:
          print("array is empty")
    else: 
        n=(np.sum(self.data, axis=1))
        con=[(n>=50),(n<=40)]
        ch=["pass","fail"]
        gr=np.select(con,ch,default="fail")
        gr_rol=gr.reshape(-1,1)
        re=np.hstack([self.data,gr_rol])
        print(re)
  def lower_upper(self):
    n=(np.sum(self.data, axis=1))
    print(f"the highest score in class is {np.max(n)}")
    print(f"the lowerest score in class is {np.min(n)}")
  def Grade_Distribution(self):
    if  self.data.size==0:
          print("array is empty")
    else: 
        n=(np.sum(self.data, axis=1))
        con=[
                (n>=90),
                (n>=80)&(n<90),
                (n>=60)&(n<80),
                (n>=50)&(n<60)]
        ch=["a","b","c","d"]
        gr=np.select(con,ch,default="fail")
        gr_rol=gr.reshape(-1,1)
        re=np.hstack([self.data,gr_rol])
        print(re)
      
        
#         for i in range(num.shape[0]):
#             for j in range(num.shape[1]):
#              if num[i][j] in range(90,100):
#                     np.append(p,"A")             
#              elif num[i][j] in range(80,90):
#                     np.append(p,"B")              

#              elif num[i][j] in range(60,80):
#                     np.append(p,"c")

#              elif num[i][j] in range(50,60):
#                     np.append(p,"D")

#              else:
#                    np.append(p,"fail")
#         p=np.array(p).reshape(-1,1)
#         s=np.hstack([self.data,p])
#         print(s)









st=student()
st.Add_data([
    [20,25,25,25],   # 95 -> A
    [20,20,20,25],   # 85 -> B
    [15,15,20,20],   # 70 -> C
    [15,15,10,15],   # 55 -> D
])
st.Total()
st.average()
st.pass_fail()
st.lower_upper()
st.Grade_Distribution()