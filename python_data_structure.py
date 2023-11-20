l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
List = list()

odd_index = l1[1::2]
print("Element at odd-index positions from list one")
print(odd_index)

even_index = l2[0::2]
print("Element at even-index positions from list two")
print(even_index)

print("Printing Final third list")
List.extend(odd_index)
List.extend(even_index)
print(List)

print("___________________________________________________")

sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
number = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2,number)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(number)
print("List after Adding element at last ", sample_list)

print("___________________________________________________")

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length/3)
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start,end)
    
    list_chunk = sample_list[indexes]
    print("Chunk" , i,list_chunk)
    
    print("After reversing it ", list(reversed(list_chunk)))
    
    start = end
    end += chunk_size
 
print("___________________________________________________")
   
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_occurence = dict()
for item in sample_list:
    if item in count_occurence:
        count_occurence[item] += 1
    else:
        count_occurence[item] = 1
        
print("Printing count of each item  ", count_occurence)            

print("___________________________________________________")

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print("First List ", first_list)
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

print("___________________________________________________")

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("first_set",first_set)
print("Second_set",second_set)

intersection = first_set.intersection(second_set)
print("Intersection is : ",intersection)
for i in intersection:
        first_set.remove(i)
        
print("First set after removing common element ", first_set)        

print("___________________________________________________")
        
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}            

print("First_set :",first_set)
print("Second_set :",second_set)

print("First set is subset of second set : ",first_set.issubset(second_set))      
print("Second set is subset of First set : ", second_set.issubset(first_set))

print("First set is Super set of second set : ",first_set.issuperset(second_set))
print("Second set is Super set of First set : ",second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()
    
if second_set.issubset(first_set):
    second_set.clear(first_set)        
    
print("First Set ", first_set)
print("Second Set ", second_set)    

print("___________________________________________________")

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("List:", roll_number)
print("Dictionary:", sample_dict)

roll_number[:] = [item for item in roll_number if item in sample_dict.values()]

print("after removing unwanted elements from list:", roll_number)

print("___________________________________________________")

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

New_speed_list = list()

for value in speed.values():
        if value not in  New_speed_list:
                New_speed_list.append(value)
                
print("Unique list ", New_speed_list)  

print("_________________________(second way)__________________________")

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
lst = []

for i in sample_list:
        if i not in lst:
                lst.append(i)
print(lst)         

Tuple =  tuple(lst)
print(type(Tuple))
print("Maximun number :",max(Tuple))
print("Minimum number :",min(Tuple))

print("+++++++++++++++++++++++++++++++++++++++")

print("Original list :",sample_list)
new = list(set(sample_list))
print("Unique_list :",new)

t = tuple(new)
print("Tuple ", t)
print("Minimum number is : ",min(t))
print("Maximum number is : ",max(t))