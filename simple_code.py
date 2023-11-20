class programs:
    def natural(self,num):
        while num <= 10:
            print(num)
            num+=1
        print()
            
    def Number_pattern(self,number):
        for i in range(0,number):
            sum = 1
            for j in range(0,i+1):
                print(sum,end=" ")
                sum = sum+1
            print()     
        print()
            
    def calculate(self,number):
        sum = 0
        for i in range(1,number+1):
            sum = sum+i
        print(sum,end=" ")     
        print()
         
        
    def multiplication(self,table):
        tab = 1
        while tab <= 10:
            print(table*tab)
            tab = tab+1 
        print()    
            
    def numbers(self,List):
        for i in List:
            if i > 150:
                if i > 500:
                    break
                continue
            if i % 5 == 0:
                print(i)  
        print()     
                
    def countdown(self,number):
        count = 0
        while (number > 0):
            count = count+1
            number = number//10
        print("Count the total number of digit : ",count)                  
        print()    
            
    def pattern(self,digit):
        for i in range(0,digit+1):
            for j in range(digit-i,0,-1):
                print(j,end=" ")
            print()      
    
    
    def reverse_list(self,List1):
        List1.reverse()
        print(List1)   
        
    def fun(self,number):
        for i in range(number-1,0,1):
            print(i)
       
    def loop(self,number):
        for i in range(number):
            print(i)
        else:
            print("Done!")  
            
              
    def func(self,lower,Upper):
        for i in range(lower,Upper+1):
            if i > 1:
                for j in range(2,i):
                    if (i%j) == 0:
                        break
                else:
                    print(i)
    
    def fibonacci(terms):
        n1,n2 = 0,1
        sum = 0
        if terms <= 0:
           print("Enter valid number")
        else:
            for i in range(0,terms):
                print(sum,end=" ")
                n1 = n2
                n2 = sum
                sum = n1,n2    
    
    def facto(self,num):
        temp = 1
        for i in range(1,num+1):
            temp = temp*i
        print(temp)     
    
        
    def reverse(self,num):
        reverse_num = 0
        while num != 0:
            digit = num%10
            reverse_num  = reverse_num*10+digit
            num = num//10
        print(str(reverse_num))        
    
    def odd_index(self,List2):
        for i in range(1,len(List2),2):
            print(List2[i])
            
    def cube(self,x):
        for i in range(1,x+1):
            cube = i**3
            print(f"Current number is : {i} and The cube is : {cube}")
            
            
    def seris(self,n):
        s = 0
        sum1 = 0
        for i in range(0,n):
            s = s*10+2
            print(s,end=" ")
            sum1 = sum1+s
        print()
        print(sum1)        
        
    def pyramid(self,rows):
        for i in range(0,rows):
            for j in range(0,i+1):
                print("*",end=" ")
            print()
        for i in range(rows,0,-1):
            for j in range(0,i-1):
                print("*",end=" ")
            print() 
        
    def OctalToDecimal(self,num):
        decimal_value = 0
        base = 1

        while num:
            last_digit = num % 10
            num = int(num / 10)
            decimal_value += last_digit * base
            base = base * 8
        print("The decimal value of",base, " is",decimal_value)                       
                
List = [12,75,150,180,145,525,50] 
List1 = [10,20,30,40,50] 
List2 = [10,20,30,40,50,60,70,80,90,100]                  
OBJ = programs()
OBJ.natural(1)            
OBJ.Number_pattern(5)
OBJ.calculate(10)            
OBJ.multiplication(2)
OBJ.numbers(List)
OBJ.countdown(75869)
OBJ.pattern(5)
OBJ.reverse_list(List1)
OBJ.fun(-10)
OBJ.loop(4)
OBJ.func(25,50)
OBJ.fibonacci
OBJ.facto(6)
OBJ.reverse(76542)
OBJ.odd_index(List2)
OBJ.cube(6)
OBJ.seris(5)
OBJ.pyramid(5)
OBJ.OctalToDecimal(10)

