'''key value pair save garna use hunchha'''

#dictionary_1 = {'a':104, 4:'four', 'c':None}   #key:value ->key int,float,string j rakhna ni payo
# print(dictionary_1)

# print(dictionary_1['a'])                 #key diyo bhane tesko value print garchha

# print (len(dictionary_1))                   #gives dictionary_1 length

# print(dictionary_1.values())             #prints values of dictionary --> dict_values([104, 'four', None])
# print(type(dictionary_1.values()))      #dictionary_1.values() class ho bhanera dekhauchha

# print(dictionary_1.keys())                 #prints keys of dictionary -->dict_keys(['a', 4, 'c'])
# print(type(dictionary_1.keys()))          #(dictionary_1.keys()) class ho bhanera dekhauchha 

# for key,value in dictionary_1.items():    #keys ra values dekhaucha 
#     print(key)
#     print(value)
#     print(key,value)

# for key in dictionary_1.keys():
#     print(key)

# for value in dictionary_1.values():
#     print(value)


# #******************************************************
# my_dict = {1:"one",2:"two"}
# print(my_dict.items())               #prints -->dict_items([(1, 'one'), (2, 'two'), ('three', 3)])

# #Key diyera value ma k chha tyo print garna
# print(my_dict[1])
# #or
# print(my_dict.get(1))

# #to insert new key and value
# my_dict[3] = "Three"           #[key] = value
# my_dict["name"] = "Ram" 
# my_dict["Roll"] = '12'             
# print(my_dict)

# # key ma tyo value chha ki chhaina check garna
# print(my_dict[2] == 25)             #True 
# print(my_dict[2] == 'two')          #False

# #POP
# print(my_dict.pop(2))       #Key diyo bhane value return garchha ani teslai delete ni garchha
# print(my_dict)              # pop garesi deko key ra tesko value delete huncha

# #popitem
# print(my_dict.popitem())    #last ko key:value pop garchha ani teslai dictionary bata delete ni garnamilchha
# print(my_dict)              #last element delete bhaye pachiko dictionary print garchha

# #Update(to update value only)
# my_dict.update({"name":"Swornima"})   #name ko aghi ko value hatara "Swornima" haldinchha  
# print(my_dict)
# #print(my_dict.update({1:"ek"}))     #esari garda None bhanera bhancha

# #Dictionary bhitra Dictionary rakhna milchha
# my_dict["new_dict"] = {1:'a',2:'b',"college":"sagarmatha"}
# print(my_dict)

##NESTED DICTIONARY
# #EXAMPLE-1
# sagarmatha = {
#         "Education Department": {
#                 "Computer Science": {
#                         "HOD":"Bharat Bhatta", 
#                         "no_of_students": 100
#                 },
#                 "Civil": {
#                         "HOD":"Sudip Lamsal",
#                         "no_of_students": 200
#                 }
#         },
#         "Admin Department": {
#                 "Accounts": {
#                         "HOD":"Chaturbhuj Nepali",
#                         "no_of_students": 50
#                 }
#         }
# }
# print(sagarmatha)


# #EXAMPLE-2(TO ADD VAT TO EVERY VALUE AND SAVE THE UPDATED VALUE IN DICTIONARY AGAIN)
# price_of_item = {
#             'apple': 120,
#             'banana': 330,
#             'orange': 210,
#             'pear': 210,
#             'grape': 410,
#             'pineapple': 560,
#             'strawberry': 770,
#             'watermelon': 660
# }
# VAT_ADDED_PRICE = {}                     #assigning empty dictionary to save the vat added price in dictionary again
# for key,value in price_of_item.items():
#       value += (13/100) * value
#       print(key,value)
#       VAT_ADDED_PRICE [key] = value       #OR use; VAT_ADDED_PRICE.update({key:value})
# print(VAT_ADDED_PRICE)


# #EXAMPLE 3
# num = input("Enter a number : ")
# x = float(num)
# def get_funct(x):
#     return x * x + 5 * x + 1
# print("the value is",get_funct(x))


#   #using 'LAMBDA'    LAMBDA: Memory create huncha kaam sakaucha ani delete huncha, use for efficient coding
# #1
# f = lambda x:x * x + 5 * x + 1
# print(f(1))

# #2(can also be used in string)
# f = lambda name:name + "Shrestha" + "1"
# print(f("Swornima"))

# #3(passing two arguments)
# f = lambda x,y:x * 2 + 5 * x * y + 1
# print("The value is : ",f(2,3))





