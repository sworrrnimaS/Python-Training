#list comprehension is basically used for loops, it is advaced form of python


# my_es = "Hi and hello and bye hehe"
# enu_list = my_es.split(" ")
# print(enu_list)
# for index,item in enumerate(enu_list):
#     print(index,item)

##normal way of using enumeration
# for index,item in enumerate(enu_list):     #jaile agadi ko le index ani pachadi ko le item ho
#     if index % 2 == 0:
#         enu_list[index] = item.upper()
# print(enu_list)

##Using list comprehension
# b = [item.upper() for item in enu_list if enu_list.index(item) % 2 == 0]
# #k garne ho,loop,condition
# print(b)


#2-D matrix addition
# Program to add two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)