#최소,최대 문제

# N = int(input())  # N정수의 개수
# N_num = input()
# N_num = N_num.split(" ")
# k = []
# if len(N_num) == N:
#     for idx in N_num:
#         idx = int(idx)
#         k.append(idx)   #정수된것을 리스트로 묶는다
        # 그래야지 min,max함수를 사용할 수 있다 
    
        
#     print(min(k),max(k),end='')        


#최댓값 문제
# k=[]    
   
# for idx in range(9):
#     idx = int(input()) 
#     k.append(idx)
#     x=max(k)       #최댓값을 x로 저장
    
    
# print(x,k.index(x)+1,sep='\n')    #index 함수는 몇번째인지 알려준다 
                                    # 0부터 세기때문에 +1을한다


# 나머지 문제

# li =[]

# for i in range(10):
#     num = int(input())  
    
#     x= num%42
#     li.append(x)    # 나머지 [1,2,3,4,5,6,7,8,9,10]  # 나머지 [0,0,0,0,0,0,0,0,0,0]
#     a =(set(li))      #set 함수는 중복된것을 빼준다
        
# print(len(a))   #len을 넣으면 개수를 출력시킨다
    

# 평균 문제
# subject_num = int(input())
# subject = input()
# spl=subject.split(" ")

# li = []   

# for i in spl:
#     i = int(i)
#     li.append(i)   
# var = 0    
# for idx in range(subject_num):
    
   
#     var += li[idx]/max(li)*100    # var = var + li[idx]/max(li)*100 하나를 저장
#                                 #저장한 값을 또 넣어준다   
# print(var/subject_num)    
   

# case_num = int(input())        



# ox퀴즈 문제 풀이

# case = int(input())

# for idx in range(case):
#     quiz = input()
#     score = 0

#     for i in range(len(quiz)):
#         item = quiz[idx]
#         count = 0
#         if item == "O":
#             for j in range([i,-1,-1]):
#                 item2 = quiz[j]
#                 if item2 == 'O':
#                     count += 1
#                 elif item2 == "X":
#                     break
                
                
#         score+= count         
#     print(score)             



# # ox 문제 다른 풀이
# case_num = int(input())
# for idx in range(case_num):     
#     quiz = list(input())        #[O,X,O,X,O,X,O,O,X,O] 이거를 다섯번
#     count = 0          # 0이 몇개 연속되어 있는지 저장할 변수
#     sum_score = 0      # 총 점수 변수 저장
#                        ##새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다
#     for i in quiz:       # 하나씩 하나씩 점수 구하기
#         if i == 'O':     # 임의 변수 i가 O이라면
#             count +=1     # O이 연속 되면 점수가 1씩 터진다
#             sum_score += count   
#         else:           
#             count = 0    
                    
#     print(sum_score)   

      
# 평균은 넘겠지 문제            
# test_case = int(input())


# for idx in range(test_case):
#     std_num = input()
#     split_1 = std_num.split(" ")
#     list_1 = list(map(int,[i for i in split_1]))
#     std_num =list_1[0]
#     score =list_1[1:]    
#     avr= sum(score)/len(score)
    
#     cnt=0
#     for j in score:
        
#         if  j> avr:
#             cnt +=1
            
   
#     percent = (cnt/std_num)*100     
#     print("{0:0.3f}%".format(percent))             
    
            
    
            

    

        
            

       
    
   
    
    
               
    
  


    



        
          
    
    
    
    