# Reverse a list in Python
list1 = [100,200,300,400,500]

list1.reverse()
print(list1)

# Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

print("Original list1 :",list1)
print("Original list2 :",list2)
list3 = [i+j for i ,j in zip(list1,list2)]
print("The list after element concatenation is : " +  str(list3))

# Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]
print("Original Numbers of list :",numbers)
List = list()
for i in range(1,len(numbers)):
    List.append(i**2)
print(List)    

# Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
lis = []
# list3 = [i+j for i , j in zip(list1,list2)]
# print("The list after element concatenation is : " +  str(list3))
for i in list1:
    for j in list2:
        lis.append(i+j)
print(lis)

# Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i , j in zip(list1,list2[::-1]):
    print(i,j)        
    
# Remove empty strings from the list of strings    

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = []
print("Original List :",list1)
for i in range(len(list1)):
    if list1[i] == "":
        continue
    else:
        list2.append(list1[i])      
print(list2)        

# Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)

# Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

# Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]

index = list1.index(20)
list1[index] = 200
print(list1)

# Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]
list = []

# for i in range(len(list1)):
#     if list1[i] == 20:
#         continue
#     else:
#         list.append(list1[i])
# print(list)        

def func(list1,number):
    for i in range(len(list1)):
        if list1[i] == number:
            continue
        else:
            list.append(list1[i])
    print(list)        
func(list1,20)    