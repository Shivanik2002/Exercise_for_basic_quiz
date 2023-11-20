def palin(num):
        
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
            
palin(101)            