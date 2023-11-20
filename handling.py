with open('hello.txt','r') as f:
    lines = f.readlines()
    
    for line in lines:
        if line.strip() == "":
            print("The line is empty")
            
        else:
            print("The line is not empty",line)    
            
import os
size = os.stat("test.txt").st_size
if size == 0:
    print("File is empty")            

print("_____________________________________________")

filename = input("File: ")
line_number = int(input("Line: "))

file = open("test.txt", "r")
lines = file.readlines()
print(lines[line_number-1])
file.close()
# line = lines[line_number - 1]
# print(line)

print("_____________________________________________")

# write a program to use string.format method to format teh following three variables per the expected output
totalMoney = 1000
quantity = 3
price = 450


Total = "I have {0} dollers so I can buy {1} football for {2:.2f} dollers.".format(1000,3,450)
print(Total)

print("_____________________________________________")

name1,name2,name3 = input("Enter three names :").split()
print("Name1:",name1)
print("Name2:",name2)
print("Name3:",name3)

print("_____________________________________________")

numbers = []
for i in range(0,5):
    digit = float(input("Enter the number : "))
    numbers.append(digit)
    
print("User List:", numbers)    
    
print("_____________________________________________")

num = 458.541315
decimal = format(num,".2f")
print("Display float number with 2 decimal places :" ,decimal)

print("_____________________________________________")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

Calculate = num_1 * num_2

print(f"Product of {num_1} and {num_2} is : {Calculate}")    

print("_____________________________________________")

print("My","Name","Is","James",sep="**")

print("_____________________________________________")


with open('test.txt','r') as f:
    lines = f.readlines()
    
    with open('New.txt','w') as fp:
        count = 0
        for line in lines:
            if count == 4:
                count = count+1
                continue
            else:
                fp.write(line)
            
            count = count+1  
        
class Numbersys:
    def octdec(self,num):
        sum = 0
        i = 0
        while num!= 0:
            reminder = num%10
            sum = reminder*pow(8,i)
            i = i +1
            num = num//10
        return sum
obj = Numbersys()
obj.octdec(1534)        