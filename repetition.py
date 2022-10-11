# 구구단 문제
# N = input()
# NE = int(N)

# for idx in range(1,10):
#     print(f'{NE} * {idx} = {idx*NE}')




# 합 문제 
# n = int(input())

# for idx in range(1):
# if n>=1 and n<=10000:
#     ret = 0
#     for idx in range(n+1):
#         ret += idx
#     print(ret)
    # sum = n*(n+1)//2
    # print(f'{sum}')




# X보다 작은수 문제 *****
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# user_input = input()
# n, x = user_input.split( " " ) # "10 5" -> ["10", "5"] -> n="10", x="5"
# n = int(n)
# x = int(x)

# if (n >= 1 and n <= 10000) and (x >= 1 and x <= 10000):
#     # 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다.
#     a = input()
#     a = a.split(' ') # "1 2 3 4 5 6 7" -> ["1", "2" , .. "7"]
#     if len(a) == n: # 1. 수열의 개수를 검사
#         # 수의 크기를 비교하는 코드
#         for item in a:
#             item = int(item)
#             if item < 1 or item > 10000:  # 1~10000 조건이 아닐 경우 exit로 프로그램 종료 
#                 print("범위가 틀렸습니다.")
#                 exit()

#         # 출력을 하기 위한 코드
#         for item in a:   # for item in ["1", "2" , .. "7"]
#             item = int(item)    # "1" -> 1
#             if item < x:    #x=3가정, 1 < 3, 2<3, 3<3, 4<3
#                 print( item, end=" " )
         


# A+B-3  문제
# var = input()
# num = int(var)
# temp =[]

# for idx in range(num):
#     k =input()
#     spl =k.split(" ")
#     A = int(spl[0])         
#     B = int(spl[1]) 
#     temp.append([A,B])
    
# if (A>0 and A<10) and (B>0 and B<10):         
        
        
#     for i in temp: 
#         a=i[0]
#         b=i[1]

#         print(a+b)




# 영수증 문제
    
# 영수증에 적힌 총 금액 :x
# 영수증에 적힌 구매한 물건의 종류의 수 n

# n개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다

# x= int(input())
# n = int(input()) 
# sum = 0
# for idx in range(n):
#     each = input() 
#     spl = each.split(" ")
#     a = int(spl[0]) 
#     b = int(spl[1]) 
#     sum = sum + a*b

# if sum == x:    
#     print("Yes")

# else:
#     print("No")





# 빠른 A+B문제
# import sys
# case_number = int(input())



# if case_number <= 1000000:    
    
#     for idx in range(case_number):
#         two_int = sys.stdin.readline()
#         two_int = two_int.strip()
#         spl =two_int.split(" ")
#         a =int(spl[0])     
#         b =int(spl[1])
 
#         print(a+b)





# A+B-7 문제
# case_number =int(input())
# k_list = [] 
          
# for idx in range(case_number):
#     two_int = input()
#     spl = two_int.split(" ")
#     a = int(spl[0])
#     b = int(spl[1])
#     k_list.append([a,b])

# sum = 0       
# for i in k_list:
#     a = i[0]
#     b = i[1]
#     sum = sum +1

#     print(f'Case #{sum}: {a+b}')



# A+B-8 문제
# case_number =int(input())
# k_list = [] 
          
# for idx in range(case_number):
#     two_int = input()
#     spl = two_int.split(" ")
#     a = int(spl[0])
#     b = int(spl[1])
#     k_list.append([a,b])

# sum = 0       
# for i in k_list:
#     a = i[0]
#     b = i[1]
#     sum = sum +1

#     print(f'Case #{sum}: {a} + {b} = {a+b}')





# 별 찍기 -1
# n =int(input())
# star = ""
# for idx in range(n):
#     star =star + "*"
    
     
#     print(f'{star}')





# 별찍기-2 *****

# n =int(input())

# for idx in range(1,n+1):       
#     for j in range(n-idx):     #  n을 5라 입력하면 idx는 1~5이기때문에 5-1 5-2 5-3 5-4
#         print(" ",end="")
#     for j in range(idx):     # 반대로 1~5로 가기때문에 1,2,3,4 
#         print("*",end="")    #end는 줄이 바뀌지않고 한줄에 다 나타낸다
 
#     print()





# A+B-5 문제
# k =[] 
# while True:
#     ab= input()
#     spl = ab.split(" ")
#     a = int(spl[0])
#     b = int(spl[1])
#     k.append([a,b])
#     if a == 0 and b == 0:
#         break
    
# for idx in k:
#     a= idx[0]
#     b= idx[1]
#     if a ==0 and b == 0:
#         break 
#     else:
#         print(a+b)        

# A+B-4 문제
# while True:
#     try:
#         ab = input()
#         temp = ab.split(" ")
#         a = int(temp[0])
#         b = int(temp[1])
#         print(a+b)
#     except:
#         break

          



# 더하기 사이클 문제
n = int(input())
cnt = 0   


if n>= 0 and n<= 99 :
    #최초 1회연산하는 코드 1회한것 이미
    origin_n = n   # 첫 변수를 저장하기 위해서 다시 저장한다
    temp = n//10 + n%10      # 첫자리계산         둘째자리계산 
    n = n%10*10 + temp%10  #첫 변수의 둘째자리   합한 수 둘째자리를 더해 n으로 저장한다
    cnt +=1  

    #2부터 시작
    while origin_n != n:    #첫입력한값과 변하는n이 같지 않는다면 계속 사이클이 돌아간다
        temp = n//10 + n%10    
        n = n%10*10 + temp%10   
        cnt += 1  #이 사이클의 길이값
    print( cnt )
        
        
   
# 중첩 반복문으로 구구단 구하기

# for i in range(2,10):    # 2,3,4,5,6,7,8,9
    
#     for j in range(1,10):  # 2.1,2.2,2.3,2.4,2.5....3.1,3.2....
#         print(f'{i}*{j}={i*j}')
            
        
# def minus(a,b):
#     x = a-b
#     return x            
             
# def plus(a,b,c):
#     three = a+b+c
#     return three

# one = 4
# two = 8
# thr = 5

# x = plus(one,two,thr)
# print(x)
       
# var1 = 3
# var2 = 6
# k =minus(var1,var2)    
        
# print(k)
         




                




        

    
      

         
    
    
    
    
          
 



