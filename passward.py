import string
import random

if __name__ == "__main__":
    
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    passward_len = int(input("Enter passward length\n"))
    S = []
    S.extend(list(s1))
    S.extend(list(s2))
    S.extend(list(s3))
    S.extend(list(s4))
    # random.shuffle(S)
    print("Your passward is: ")
    # print("".join(S[0:passward_len]))
    print("".join(random.sample(S,passward_len)))
    
    
print("____________________________________________________")
# class Demo:
#     def Average(self,List):
#         total = 0
#         count = 0
#         for i in range(len(List)):
#             if List[i] == None:
#                     continue 
#             else:   
#                 total += List[i]
#                 count += 1
#         average = total/ count
#         print("Average of the List {}" .format("%.2f"%average))

# List = [12,3,4,56,70,0]     
# root = [4,8,5,0,1,None,6]   
# obj = Demo()
# obj.Average(List)       
# obj.Average(root) 