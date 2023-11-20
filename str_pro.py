str1 = "James"
print("Orignal List : ",str1)
first_char = str1[0]
l = len(str1)
middle_char = int(l/2)
result = first_char+str1[middle_char]
result = result+str1[l-1]
print("New string : ",result)

print("_____________________________________________________________")

def middle_three_char(str1):
    print("Orignal string is " ,str1)
    middle_char = int(len(str1)/2)
    result = str1[middle_char-1:middle_char+2]
    print("Middle three chars are : ",result)
    
middle_three_char("JhonDipPeta")
middle_three_char("JaSonAy")  

print("_____________________________________________________________")  
    
def append_middle(s1,s2):      # s1 = Ault s2 = Kelly expected_output = AuKellylt 
    print("Orignal strings are : ",s1,s2)
    middle_char = int(len(s1)/2)
    x = s1[:middle_char:]    
    x  = x + s2
    x = x + s1[middle_char:]
    print("After appendding new string in middle : ",x)
    
append_middle("Ault","Kelly")   

print("_____________________________________________________________") 

str1 = "PYnAtive"

print("Original strings : ",str1)
lower_char = []
upper_char = []

for chars in str1:
    if chars.islower():
        lower_char.append(chars)
    else:
        upper_char.append(chars)
        
sorted_str = ''.join(lower_char+upper_char)
print(sorted_str)            

print("_____________________________________________________________")

# str1 = "P@#yn26at>&i5ve"
def find_digit_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    
    for char in sample_str:
        if char.isalpha():
            char_count += 1
            
        elif char.isdigit():
            digit_count += 1
        
        else:
            symbol_count += 1        
            
    print("Chars =" , char_count , "Digits =" , digit_count , "Symbol =", symbol_count)        
    
sample_str =  "P@#yn26at>&i5ve"
print("Total counts of chars, Digits, and symbols \n")
find_digit_chars_symbols(sample_str)   

print("_____________________________________________________________")

s1 = "Abc"
s2 = "Xyz"

s1_length = len(s1)
s2_length = len(s2)

result = ""

s2 = s2[::-1]

for i in range(s1_length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

print("_____________________________________________________________")

def string_balance(s1,s2):
        flag = True
        for char in s1:
                if char in s2:
                        continue
                else:
                        flag = False
                        
        return flag                
        
s1 = "Yn"
s2 = "PYnative"
s3 = string_balance(s1,s2)    
print("s1 ans s2 are balanced : ",s3)            

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance(s1, s2)
print("s1 and s2 are balanced:", flag)

print("_____________________________________________________________")

str1 = "Welcome to USA. usa awesome, isn't it?"
# sub_string = "USA"
Lower_case = str1.lower()
count = Lower_case.count("usa")
print("The USA count is : ",count)

print("_____________________________________________________________")

my_string = "PYnative29@#8496"
total = 0
count = 0
for char in my_string:
        if char.isdigit():
                total+=int(char)
                count+=1
average = total/count
print(("Sum is:", total, "Average is ", average))    

print("_____________________________________________________________")

string = "Apple"

My_dict = dict()
for char in string:
        count = string.count(char) 
        My_dict[char] = count     
print("Result : ",My_dict)             

print("_____________________________________________________________")
                
str1 = "PYnative"
print("Original string is : ",str1)

reverse_str1 = str1[::-1]      
print("Reversed string is : ",reverse_str1)  
        
print("_____________________________________________________________")

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)

print("_____________________________________________________________")

str1 = "Emma-is-a-data-scientist"
str2 = str1.split("-")
print("Displaying each substring")
for i in str2:
        print(i)

print("_____________________________________________________________")

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print("Original list of strings :")
print(str_list)
str_list2 = []

for i in str_list:
        if i == "":
                continue
        else:
               str_list2.append(i)
               
print("After removing empty strings" )               
print(str_list2)               

print("_____________________________________________________________")

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

print("_____________________________________________________________")

str1 = 'I am 25 years and 10 months old'

for i in str1:
        if i.isdigit():
                print(i,end="")
                
print()
                
print("_____________________________________________________________")

str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
    
print("_____________________________________________________________")

import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

for char in string.punctuation:
        str1 = str1.replace(char,"#")
        
print("The strings after replacement : ",str1)    