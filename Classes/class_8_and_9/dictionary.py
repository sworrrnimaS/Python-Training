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

#NESTED DICTIONARY
sagarmatha = {
        "Education Department": {
                "Computer Science": {
                        "HOD":"Bharat Bhatta", 
                        "no_of_students": 100
                },
                "Civil": {
                        "HOD":"Sudip Lamsal",
                        "no_of_students": 200
                }
        },
        "Admin Department": {
                "Accounts": {
                        "HOD":"Chaturbhuj Nepali",
                        "no_of_students": 50
                }
        }
}
print(sagarmatha)
