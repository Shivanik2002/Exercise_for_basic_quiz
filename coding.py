class function:
    def OddEven(self,number):
        if (number % 2) == 0:
            print("{0} is even number" .format(number))
        else:
            print("{0} is odd number" .format(number))
            
    def compare(self,num):
        if num > 0:
            print("It's positive number")
            
        elif num == 0:
            print("It's Zero")
            
        else:
            print("It's Negative number")
    
    def SUM(self,number1,number2):
        sum = number1 + number2
        print(sum)     
        
    def palin(self,num):
        
        reverse = 0
        digit = num
        
        while digit > 0:
            remainder = digit % 10
            reverse = (reverse * 10) + remainder
            digit = digit//10
            
        if num == reverse:
            print("This is a Palindrome number")
        
        else:
            print("Not Palindrome") 
            
    def Number(self,List):
        value = []
        for i in List:
            c=0
            for j in range(1,i):
                if i % j == 0:
                    c+=1
            if c==1:
                value.append(i) 
        print("this is the list of prime number ")          
        print(value) 
         
    def armstrong(self,temp):
        number = 0
        num = temp
        while num > 0:
            digit = num % 10
            number = number + digit**3
            num = num // 10
        if temp == number:
            print(temp,"Is an armstrong number")
            
        else:
            print(temp,"is not an Armstrong number")   
            
    def anagram(self,str1,str2):
        # if len(str1) == len(str2):
            # print("Anagram")
            if sorted(str1) == sorted(str2):
                print("Given number is anagram")
            else:
                print("Given number is not anagram")
        # else:
        #     ("Not anagram")      
        
    def maximum(self,num1,num2):
        if num1 >= num2:
            print("Maximum of two numbers",num1)
        else:
            print("Maximum of two numbers",num2) 
                
    def minimum(self,num1,num2):
        if num1 <= num2:
            print("Minimum of two numbers",num1)
        else:
            print("Minimum of two numbers",num2)  
            
    def max(self,a,b,c):
        if (a > b) and (a > c):
            print("largest number is : ",a)
        elif (b > a) and (b > c):
            print("largest number is : ",b)
        else:
            print("largest number is : ",c)
    
    def mini(self,a,b,c):
        if (a < b) and (a < c):
            print("smallest number is : ",a)
        elif (b < a) and (b < c):
            print("smallest number is : ",b)
        else:
            print("smallest number is : ",c)        
            
    def facto(self,number):
        if number < 0:
            print("Factorial of this number does not exist")
        elif number == 0:
            print("The factorial of 0 is : 1")
        else:        
            fact = 1
            for i in range(1,number+1):
                fact = fact*i   
            print(f"The factorial of {number} isn: ",fact)   
            
    def fibonacci(self,num):
        n1,n2 = 0,1
        sum = 0
        if num <= 0:
            print("Please enter the positive number")
            
        elif num == 1:
            print("Fibonacci sequence upto",num,":")    
            
        else:
            print("Fibonacci sequence : ")
            while sum < num+1:
                print(n1)
                nth = n1+n2
                n1 = n2
                n2 = nth
                sum += 1
                
    def gcd(self,num1,num2):
        if num1 < num2:
            mn = num1
        else:
            mn = num2
        
        for i in range(1,mn+1):
            if num1%i == 0 and num2%i == 0:
                gcd = i 
        
        print(f"The gcd of these two numbers is {gcd}")                          
                
    def star(self,num):
        for i in range(0,num):
            for j in range(0,i+1):
                print("*",end=" ")
            print("\r")   
            
    def number_pattern(self,num):
        for i in range(0,num):
            num = 1
            for j in range(0,i+1):
                print(num,end=" ") 
                num = num+1
            print()          
            
    def pattern(self,digit):
        num = 1
        for i in range(0,digit):
            for j in range(0,i+1):
                print(num,end=" ")
                num = num+1
            print("\r")             
    
    def alphabet(self,n):
        num = 65
        for i in range(0,n):
            for j in range(0,i+1):
                ch = chr(num)
                print(ch,end=" ")
            num = num+1
            print()   
            
    def contalpha(self,n):
        num = 65
        for i in range(0,n):
            for j in range(0,i+1):
                ch = chr(num)
                print(ch,end=" ")
                num = num+1
            print()    
            
    def tringle(self,num):
        for i in range(0,num):
            for j in range(0,num-i-1):
                print(' ',end=" ")
            for k in range(2*i+1):
                print('*',end=" ")
            print()      
            
    def myfun(self,n):
        k = n-1
        for i in range(0,n):
            for j in range(0,k):
                print(end=" ")
            k = k-1
            for j in range(0,i+1):
                print("*",end=" ")
            print()                      
                         
List = [5,13,56,91,33,79,29,81,67,56,81,111]
obj = function()
obj.OddEven(3)            
obj.compare(33)
obj.SUM(23,23)
obj.palin(121)
obj.Number(List)
obj.armstrong(234)
obj.anagram("heart","earth")
obj.anagram("bad","dad")
obj.maximum(12,34)
obj.minimum(12,2)
obj.max(1,2,3)
obj.mini(2,3,4)
obj.facto(5)
obj.fibonacci(5)
obj.gcd(12,6)
obj.star(5)
obj.number_pattern(5)
obj.pattern(5)
obj.alphabet(5)
obj.contalpha(6)
obj.tringle(5)
obj.myfun(4)