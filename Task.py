class Number:
    def task(self,number_x):
        if number_x[0] == number_x[-1]:
           print("True")
        else:
           print(("False"))
           
    def number(self,list):
        List = []
        
        for i in list:
            
            if i % 5 == 0:
                List.append(i)
                
        print(f" this all are divisible By 5  {List}:")
        
    def strg(self, str_x):
            str_y = str_x.count("Emma")
            print(f" Emma appeared {str_y} times :")
            
    def pattern(self,num):
        for i in range(num):
            for j in range(1,i+1):
                print(i,end=" ") 
            print()        
            
    def Multi(self,x1,x2):
        Product = x1 * x2
        if Product >= 1000:
            print(Product) 
        else:
            print(x1+x2) 
            
    def Iterate(self,number):
        x = 0
        for i in range(number):
            previous_num = x + i
            print(f"Current number {i} Previous number {x} Sum:{x+i}")
            previous_num = i    
            
    def strg1(self,strg):
        str1 = str(strg)
        print(str1)
        strg2 = strg[0::2]
        for i in strg2:
            print(i)
    
    def Remove(self,n):
        strg = n[4::]
        print(strg) 
        
        strg1 = n[2::]  
        print(strg1) 
        
    def palindrome(self,number):
        number = str(number)
        reversed = number[::-1]
        if number == reversed:
            print("It's palindrome Number")
        else:
            print("It's not palindrome Number")   
            
    def Lst(self,lst1,lst2):
        lst3 = []
        for i in range(len(lst1)):
            if lst1[i] % 2 != 0:
                lst3.append(lst1[i])
                
            if lst2[i] % 2 == 0:
                lst3.append(lst2[i])
        print(lst1)
        print(lst2)
        print(lst3)        
    
    def pattern(self,star):
        for i in range(0,star):
            for j in range(star,i,-1):
                print("*",end=" ")
            print()    
            
    def table(self,tab):
        for i in range(1,tab):
            for j in range(1,tab):
                print(i*j,end=" ")        
            print()
    
    def extract(self,str1):
        strg = str(str1)
        strg1 = strg[::-1]
        for i in strg1:
            # print(f"'{i}'",end=" ")
            print('"',i,'"',end=" ")
        print("str1")
    
    def exponent(self,base,exp):
        # if base = 5 ,exp = 3 ,output = 125
        Output = 1
        for i in range(exp):
            Output = Output*base
        print(Output)
            
number_x = [10,20,30,40,10]
number_y = [75,65,35,75,30]
list = [10,20,33,46,55]
str_x = "Emma is good developer. Emma is a writer"
lst1 = [10,20,25,30,35]
lst2 = [ 40,45,60,75,90]

Obj = Number()
# Obj.task(number_x)        
# Obj.task(number_y) 
# print("_______________________________________________________") 
# Obj.number(list)
# print("_______________________________________________________") 
# Obj.strg(str_x)
# print("_______________________________________________________") 
# Obj.pattern(6)
# print("_______________________________________________________") 
# Obj.Multi(20,30)
# Obj.Multi(30,40)
# print("_______________________________________________________")
# print("Printing current and previous number sum in a range(10)") 
# Obj.Iterate(10)
# print("_______________________________________________________") 
# Obj.strg1("pynative")
# print("_______________________________________________________") 
# Obj.Remove("pynative")
# print("_______________________________________________________") 
# Obj.palindrome(121)
# Obj.palindrome(534)
# print("_______________________________________________________") 
# Obj.Lst(lst1,lst2)
# Obj.pattern(5)
# print("_______________________________________________________") 
# Obj.table(11)
print("___________________________________________________________")
Obj.extract(7536)
print("___________________________________________________________")
Obj.exponent(3,5)
Obj.exponent(5,4)