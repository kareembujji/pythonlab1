my_str = 'bujji is the best . bujji loves to cook biryani. Jane and Will cook together'
print("The string is : ")
print(my_str)
replace_dict = {'bujji' : 'he' }
my_list = my_str.split(' ')
my_result = ' '.join([replace_dict.get(val) if val in replace_dict.keys() and my_list.index(val) != idx else val for idx, val in enumerate(my_list)])
print("The string after replacing with values is : ")
print(my_result)
