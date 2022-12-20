# my_list = [1,2,3,4,5,6,7,8,9,10]
# next_list = my_list[::-1]
# NEW_LIST = []
# for index in range(len(my_list)):
#     NEW_LIST.append(my_list[index]+next_list[index])
# print(NEW_LIST)

# #loop banara garda dherai time lagchha tei ghatauna ko lagi 'map' use garne


#FUNCTION TO CHECK IF IT EVEN 
my_list3 = [1,20,3,4,5,6,7,8,9,10]
even_list = []
odd_list = []

# for element in my_list3:
#     #print(element)
#     if element % 2 == 0:
#         even_list.append(element)
# print(even_list)     #prints even list
    
# #     else:
# #         odd_list.append(element)
# # print(odd_list)
# #ifelse sadhai sanga huna parcha teibhara last ma print garna parchha

#esari
for element in my_list3:
    #print(element)
    if element % 2 == 0:
        even_list.append(element)
    else:
        odd_list.append(element)
print(odd_list)
print(even_list)
    

 
