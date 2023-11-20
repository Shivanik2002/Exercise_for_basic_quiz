def Myfun(name,age):
    print(name,age)

Myfun("Shivani",21)    

def func1(*arguments):
    for i in arguments:
        print(i)

func1(20,40,60)
print()    
func1(80,100)    

def calculation(a,b):
    addition = a+b
    subtraction = a-b
    return addition,subtraction

print("Return both addition and subtraction in a single return call")
final = calculation(40,10)
print(final)

def show_employee(name,salary=9000):
   print(name,salary)
   
show_employee("Ben",12000) 
show_employee("Jessa")   

def recursive_fun(numbers):
    if numbers:
        return numbers + recursive_fun(numbers-1)
    else:
        return 0
    
obj = recursive_fun(10)
print(obj)    

def func1(number1,number2):
    list = []
    for i in range(number1,number2,2):
        list.append(i)
    print(list)
        
func1(4,30)        
        
def display_student(name,age):
    print(name,age)
    
display_student("Emma",26)
show_student = display_student
show_student("Emma",26)      

def larger(List):
    max = List[0]
    for i in List:
        if i > max:
            max = i    
    print(f"largest number of the List : {max}")      

List = [4,6,8,24,12,2]    
larger(List)    

def outer_fun(a,b):
    def inner_fun(a,b):
        return a+b
    addition = inner_fun(a,b)
    return addition+5

final = outer_fun(5,10)
print(final)