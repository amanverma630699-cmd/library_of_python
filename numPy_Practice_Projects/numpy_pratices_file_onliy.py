import numpy as np
# # n= np.array([[2,4],[5,6]])
# # b=np.array([[4,5], [6,7]])
# # ar=np.concatenate((n,b),axis=1)
# # print(ar)
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


arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
a1,a2,a3=np.split(arr,[2,2])
print(a1)
print(a2)
# print(a3)