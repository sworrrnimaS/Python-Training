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
# # #using dicitonary comprehension
# # #change the value,for every key and value in given dicitionary 
# # VAT_ADDED_PRICE = { key : value+value*0.13 for key,value in price_of_item.items()} 
# # print(VAT_ADDED_PRICE)

# # CHANGING_KEY = {f"{key}'s" : value+value*0.13 for key,value in price_of_item.items()}   #key laini change garera hereko
# # print(CHANGING_KEY)

# #USING FUNCTION (TO SHOW USE OF DEFAULT ARGUMENTS)
# def get_price_of_item(price_of_item, tax_rate = 0.13):
#     return {key : value+value * tax_rate for key,value in price_of_item.items()}
# print(get_price_of_item(price_of_item))       #prints vat added price
# print(get_price_of_item(price_of_item,0.15))    #uses tax_rate = 0.15 instead of 0.13


