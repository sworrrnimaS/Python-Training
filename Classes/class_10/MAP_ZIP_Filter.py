# #***MAP*** (function name, ani tyo function ma list/tuple as an argument pathaune)
#    #i) same size milchha plus different length ko pathaye ni milchha 
      

# my_list = [1,2,3,4,5,6,7,8,9,10]
# next_list = my_list[::-1]
# my_tuple = (2,2,2,2,2,2,2,2,2,2)

# #function definition
# def sum_of_num(a,b,c):
#     return a + b + c

# #passing arguments in function
# print(sum_of_num(1,2,3))

# #using 'map'
# sum = map(sum_of_num, my_list, next_list, my_tuple)
#                           #print(sum) garda whole lai object mandera address diyo
# print(list(sum))




# #***ZIP*** (list ko element, index mileko haru ekei thau ma lyauchha ani tuple/list use garera lagne)
#       #i) farak length zip garda sabse kam length jun list ko chha teti nei length ko zippedlist hunchha

my_list1 = [1,2,3,4,5,6,7,8,9,10]
next_list1 = my_list1[::-1]
short_list = [2,4,6,8]  #just to check
my_tuple1 = (1,3,5,7)

#zip in LIST
zipped_list = list(zip(my_list1, next_list1,my_tuple1))
print(zipped_list)

#zip in TUPLE
zipped_list = tuple(zip(my_list1, next_list1,my_tuple1))
print(zipped_list)




#USE OF MAP AND LAMBDA
NEW_LIST1 =list(map(lambda x,y:x * x + x * y + 1, my_list1, next_list1))
print(NEW_LIST1)


#***FILTER***(True lai matra print garchha)
def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False
NEW_LIST2 = list(filter(check_even, my_list1))
print(NEW_LIST2)

#using filter and lambda
NEW_LIST2 = list(filter(lambda x : x%2 ==0, my_list1))
print(NEW_LIST2)