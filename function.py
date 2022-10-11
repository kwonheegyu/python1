# 정수 n개의 합
# def solve(a):
#     x = 0   
#     for i in range(len(a)):
        
#         x = x+a[i]

#     return  x            
           
# b=[4,3,4,6,2,6]

# s= solve(b)
# print(s)
 

# 한 수 문제


# def math(num):
#     cnt = 0
#     for idx in range(1,num+1):
#         num_list = list(map(int,str(idx)))
        
        
#         if idx <100:
#             cnt+=1
           
            
#         elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#             cnt +=1
#     return cnt
# num = int(input())    
# print(math(num))
     
#셀프 넘버 문제



# def self_num():
#     list_1=[]
#     for id in range(1,10000):    
#         # id = id//10 + id%10 + id
#         const = id//1000 + id//100%10 + id%100//10 + id%10 +id
#         list_1.append(const)
#     total_list =  [idx for idx in range(1,10000)]    
#     for idx in list_1:
#         if idx in total_list:
#             total_list.remove(idx)

#     for j in total_list:
#         print(j)    
        
#     return                       
        
        
# print(self_num())        
        


        
            
        
        
        
        
    
    
   
    