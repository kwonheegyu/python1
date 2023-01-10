# 소수 찾기 백준
# num = int(input())
# self_num = map(int, input().split())

# sosu = 0
# for j in self_num:
#     error=0
#     if j>1:
#         for k in range(2,j):
#             if j%k ==0:
#                 error +=1
#         if error == 0:
#             sosu+=1    
# print(sosu)         
#백준 모범 답안        
# n = int(input())
# numbers = map(int, input().split())
# sosu = 0
# for num in numbers:
#     error = 0
#     if num > 1 :
#         for i in range(2, num):  # 2부터 n-1까지
#             if num % i == 0:
#                 error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
#         if error == 0:
#             sosu += 1  # error가 없으면 소수.
# print(sosu)            
               
#백준 소수
# M = int(input())
# N = int(input())    
# sum = 0   
# a = []     
# for idx in range(M,N+1):
#     check = 0
#     if idx>1:
#         for j in range(2,idx):
#             if idx % j == 0:
#                 check +=1 
#         if check == 0:
#             sum += idx
#             a.append(idx)
            
# if not a:
#     print(-1)
# else:
#     print(sum)    
#     print(a[0])               

# 백준 소인수분해
                  
# N = int(input())
# a=[]
# if N == 1:
#     print('')
# for idx in range(2,N+1):
#     if N%idx ==0:
#         a.append(idx)
#         while N % idx ==0:
#             print(idx)
#             N = N//idx 

# 백준 소수 구하기
# sosu = list(map(int,(input().split())))
# a =[]
# for idx in range(sosu[0],sosu[1]):
    
#     check = 0
#     for j in range(2,idx):
#         if idx%j == 0:
#             check +=1
#     if check == 0:
#         a.append(idx)
# # print(a)        
        
# for idx in a:
#     print(idx)         


# 백준 모범답안 제곱근을 이용한 소수 구하기 그래야 초과가 안된다
# m,n=map(int,input().split())
# for i in range(m,n+1):
#     if i==1:#1은 소수가 아니므로 제외
#         continue
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0: #약수가 존재하므로 소수가 아님
#             break   #더이상 검사할 필요가 없으므로 멈춤
#     else:
#         print(i)


#베르트랑 공준 문제

# while True:
#     x=int(input())
#     if x == 0:
#         break
#     n = 2*x
#     a = [False,False] + [True]*(n-1)
#     primes = []
#     for i in range(2,n+1):
#         if a[i]:
#             if i > x :
#                 primes.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False 
          
#     print(len(primes)) 


        
     
# 골드바흐의 추측     
# sosu = [0 for i in range(10001)]
# print(sosu)
# sosu[1] = 1
# print(sosu[1])
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         sosu[j] = 1
# t = int(input())
# for i in range(t):
#     a = int(input())
#     b = a // 2
#     for j in range(b, 1, -1):
#         if sosu[a - j] == 0 and sosu[j] == 0:
#             print(j, a - j)
#             break

    




    
            


        
          
         


                
     