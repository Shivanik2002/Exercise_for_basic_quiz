# file = open('test.txt','r')
# lines = file.readlines()
# print(lines)
# file.close()

# file1 = open('New.txt','w')
# line = file1.write("lines")
# # print(line)
# for i in line:
#     if i == line4:
#         i+1
#         continue
#     else:
#         print(i)        
# with open('test.txt','r') as input:
#     with open('New.txt','w') as output:
#         for line in input:
#             if input[line] == "line4":
#                 i = i+1
#                 continue
#             else:
#                 output.write(line) 
                
# class Numbersys:
#     def octdec(self,octalval):
#         decimal_number = 0
#         position = 0
#         while octalval!= 0:
#             decimal = octalval % 10
#             decimal_number =  decimal_number + decimal * pow(8,position)
#             octalval= octalval//10
        #     position = position+1
        # return decimal_number

# octalval = int(input("Enter Any number"))
# obj = octdec(octalval)
# print("Decimal value:" octalval," = ", obj)
# obj = Numbersys()
# obj.octdec(305)          

# with open('test.txt','r') as f:
#     lines = f.readlines()
    
#     with open('New.txt','w') as fp:
#         count = 0
#         for line in lines:
#             if count == 4:
#                 count = count+1
#                 continue
#             else:
#                 fp.write(line)
            
#             count = count+1  
        
           
# class A:
#     def OctalToDecimal(self,num):
#         decimal_value = 0
#         base = 1

#         while num:
#             last_digit = num % 10
#             num = int(num / 10)
#             decimal_value += last_digit * base
#             base = base * 8
#         print("The decimal value of",base, " is",decimal_value)
    
# obj = A()
# obj.OctalToDecimal(234)        
            
# import os

# size = os.stat("test.txt").st_size
# if size == 0:
#     print("File is empty") 

# strOne = str("pynative")
# strTwo = "pynative"
# print(strOne == strTwo)
# print(strOne is strTwo)

# str = "My salary is 7000"
# print(str.isalnum())

# s1 = "Abc"
# s2 = "Xyz"

# s1_length = len(s1)
# s2_length = len(s2)

# result = ""

# s2 = s2[::-1]

# for i in range(s1_length):
#     if i < s1_length:
#         result = result + s1[i]
#     if i < s2_length:
#         result = result + s2[i]

# print(result)

# def string_balance(s1,s2):
#         flag = True
#         for char in s1:
#                 if char in s2:
#                         continue
#                 else:
#                         flag = False
                        
#         return flag                
        
# s1 = "Yn"
# s2 = "PYnative"
# s3 = string_balance(s1,s2)    
# print("s1 ans s2 are balanced : ",s3)            

# s1 = "Ynf"
# s2 = "PYnative"
# flag = string_balance(s1, s2)
# print("s1 and s2 are balanced:", flag)

# str1 = "Welcome to USA. usa awesome, isn't it?"
# # sub_string = "USA"
# Lower_case = str1.lower()
# count = Lower_case.count("usa")
# print("The USA count is : ",count)

# my_string = "PYnative29@#8496"
# total = 0
# count = 0
# for char in my_string:
#         if char.isdigit():
#                 total+=int(char)
#                 count+=1
# average = total/count
# print(("Sum is:", total, "Average is ", average))    

# string = "Apple"

# My_dict = dict()
# for char in string:
#         count = string.count(char) 
#         My_dict[char] = count     
# print("Result : ",My_dict)             
                
# str1 = "PYnative"
# print("Original string is : ",str1)

# reverse_str1 = str1[::-1]      
# print("Reversed string is : ",reverse_str1)          

# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Original String is:", str1)

# index = str1.rfind("Emma")
# print("Last occurrence of Emma starts at index:", index)

# str1 = "Emma-is-a-data-scientist"
# str2 = str1.split("-")
# print("Displaying each substring")
# for i in str2:
#         print(i)

# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# print("Original list of strings :")
# print(str_list)
# str_list2 = []

# for i in str_list:
#         if i == "":
#                 continue
#         else:
#                str_list2.append(i)
               
# print("After removing empty strings" )               
# print(str_list2)               

# import string

# str1 = "/*Jon is @developer & musician"
# print("Original string is ", str1)

# new_str = str1.translate(str.maketrans('', '', string.punctuation))

# print("New string is ", new_str)

# str1 = 'I am 25 years and 10 months old'

# for i in str1:
#         if i.isdigit():
#                 print(i,end="")

# str1 = "Emma25 is Data scientist50 and AI Expert"
# print("The original string is : " + str1)

# res = []
# temp = str1.split()

# for item in temp:
#     if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
#         res.append(item)

# print("Displaying words with alphabets and numbers")
# for i in res:
#     print(i)


# import string

# str1 = '/*Jon is @developer & musician!!'
# print("The original string is : ", str1)

# for char in string.punctuation:
#         str1 = str1.replace(char,"#")
        
# print("The strings after replacement : ",str1)        

# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# print("first_set",first_set)
# print("Second_set",second_set)

# intersection = first_set.intersection(second_set)
# print("Intersection is : ",intersection)
# for i in intersection:
#         first_set.remove(i)
        
# print("First set after removing common element ", first_set)        
        
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}  

# print("First_set :",first_set)
# print("Second_set :",second_set)

# print("First set is subset of second set : ",first_set.issubset(second_set))      
# print("Second set is subset of First set : ", second_set.issubset(first_set))

# print("First set is Super set of second set : ",first_set.issuperset(second_set))
# print("Second set is Super set of First set : ",second_set.issuperset(first_set))

# if first_set.issubset(second_set):
#     first_set.clear()
    
# if second_set.issubset(first_set):
#     second_set.clear(first_set)        
    
# print("First Set ", first_set)
# print("Second Set ", second_set)    

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# print("List:", roll_number)
# print("Dictionary:", sample_dict)

# roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
# print("after removing unwanted elements from list:", roll_number)

# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# New_speed_list = list()

# for value in speed.values():
#         if value not in  New_speed_list:
#                 New_speed_list.append(value)
                
# print("Unique list ", New_speed_list)   

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# lst = []

# for i in sample_list:
#         if i not in lst:
#                 lst.append(i)
# print(lst)         

# Tuple =  tuple(lst)
# print(type(Tuple))
# print("Maximun number :",max(Tuple))
# print("Minimum number :",min(Tuple))


