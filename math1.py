
# 백준 손익분기점 문제
# abc = map(int,input().split(" "))
# _list = list(abc)
# if _list[2]>_list[1]:
#     res = _list[2]-_list[1]
#     share = _list[0]//res +1
# else:
#     share = -1    

# print(share)

# 백준 벌집 문제
# bee = int(input())   #계차수열 공식으로 푼 방식
# cnt = 0
# i = 1
  
# while bee>(3*i*i-3*i + 1):  # a = 3n제곱 -3n +1
#     i += 1
# else :
#     print(i)   
    
# 백준 분수찾기 
# fount = int(input())

# prev_max  = 0
# current_max = 1
# line = 0
# minus = 1

# while True:
#     current_max = prev_max + minus
#     k=[idx for idx in range(prev_max+1,current_max+1)]
   
#     if fount in k:
#         _line = line +1
#         _index= k.index(fount)
#         front_even = 1+_index
#         back_even = _line -_index
#         front_odd = _line-_index
#         back_odd = _index+ 1
        
#         if _line % 2 == 0:
#             print(f'{front_even}/{back_even}')  
#         else: 
#             print(f'{front_odd}/{back_odd}')     
#         break
#     prev_max = current_max
#     minus = 2 + line
#     line +=1

# 백준 달팽이는 올라가고 싶다    모범답안
# A, B, V = map(int, input().split())

# x = (V-B)/(A-B)
# if x == int(x):
#     print(int(x))
# else:
#     print(int(x) + 1)

#백준 달팽이느 올라가고 싶다 반복문으로 풀었을때
# abv = map(int,input().split(" "))
# abv_list = list(abv)
# print(abv_list)

# cnt = 1
# prev = 0

# while True:
#     current = abv_list[0] + prev
#     if current < abv_list[2]:
#         x = current - abv_list[1]
#     else:
#         break
#     cnt +=1
#     prev = x
    
# print(cnt) 
        
# 백준 ACM 호텔 문제
# data_num = int(input())
# for idx in range(data_num):
#     data = list(map(int,input().split(" ")))
    
#     cnt = 0     
#     for idx in range(1,data[1]+1):
#         for j in range(1,data[0]+1):
#             if idx < 10 :
#                 k = f'{j}0{idx}'
                
#             else:
#                 k = f'{j}{idx}'
#             cnt+=1
            
#             if cnt == data[2]:
#                  print(k)
           

#부녀회장이 될테야 백준 
# Test_case = int(input())           
# for idx in range(Test_case):
#     floor = int(input())                      
#     ho = int(input())                      
#     citizen = 0
#     _list=[]

#     for j in range(0,floor+1):    
#         if j == 0:
#             # citizen = idx 
#             a = [idx for idx in range(1,ho+1)]
#             _list.append(a)
#             print(_list)
#         else:
#             _list.append([])
#             print(_list)
#             for _ho in range(1, ho+1):
#                 x = sum([_list[j-1][idx] for idx in range(0, _ho)])
#                 print(x)
#                 _list[j].append(x)
#             print(_list[j])

#     print(_list[floor][ho-1])
# 백준 모범답안
# t = int(input())

# for _ in range(t):
#     floor = int(input())
#     num = int(input())
#     f0 = [x for x in range(1, num+1)]
#     for k in range(floor):
#         print(f0)  
#         for i in range(1, num):
#             f0[i] += f0[i-1]
#     print(f0[-1])    
# 백준 설탕 배달 모범 답안
# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)
            

# 백준 큰 수 A+B
# A,B = map(int,input().split(" "))         

# k=A+B
# print(k)
                

             
        
        

    
             
             
    
            


      
  
       

                    
            
            
            



    
    