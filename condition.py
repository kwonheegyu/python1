
# 두 수 비교하기 문제
# two = input("")
# split = two.split(" ")
# var1 = int(split[0])
# var2 = int(split[1])

# if ((var1 >= -10000) and (var1 <= 10000) and (var2 >= -10000) and (var2 <= 10000)) :
#   if var1 > var2: 
#     print(">")
#   elif var1 < var2:
#     print("<")
#   elif var1 == var2:
#     print("==")




 
# 시험 성적 문제 
# testscore = input("")
# var1 = int(testscore) 

# if((var1>= 0) and (var1<=100) ):
#     if  var1 >= 90: 
#         print("A")
#     elif var1 >= 80 and var1<=89: 
#         print("B")
#     elif var1 >= 70 and var1<=79: 
#         print("C")
#     elif var1 >= 60 and var1<=69: 
#         print("D")  
#     else:
#         print("F")





# 윤년 문제
        
# year = input("")
# var1 = int(year)

# if((var1 >=1) and (var1<=4000)):
#   if ((var1%4 == 0) and (var1%100 != 0)) or (var1%400 == 0):
#       print("1") 
#   else:
#       print("0")







#사분면 고르기 문제  
        
# Rectangle1 = input("")
# Rectangle2 = input("")
# x = int(Rectangle1)
# y = int(Rectangle2)

# if (x>= -1000) and (x<= 1000) and  (y>= -1000) and (y<= 1000) and (x != 0) and (y !=0):
#     if(x>0) and (y>0):
#         print("1")    
#     elif(x<0) and (y>0):
#             print("2")   
#     elif(x<0) and (y<0):
#             print("3")   
#     elif(x>0) and (y<0):
#             print("4")   







# 알람 시계 문제 *****
clock = input("")
split = clock.split(" ") 
H = int(split[0])           #알람시간의 시
M = int(split[1])          #알람시간의 분



if  (H>=0) and (H<=23) and (M>=0) and (M<=59):
    if (M-45<0):           # 알람시간의  분의 45분을 빼서 0보다 작으면
        M = (60+(M-45))   # 60분을더해준다
        
        
        if(H == 0):  # 0이랑 같다면
           H= 24     #   그 시는 24시이다
           H= H-1   #  시는 -1을 한다
        elif(H!=0):  # 0이랑 같지 않다면
           H =H-1   # 그냥 -1을 한다
    else:                
        M = (M-45)  #그냥 45분을 빼준다
    print(H,M)       





# 오븐 시계 문제 *****

nowtime = input("")
split = nowtime.split(" ")
NT = int(split[0])
NT2 = int(split[1])

cooktime = input("")
CT = int(cooktime)    
   

if(NT>=0) and (NT<=23) and (NT2>=0) and (NT2<=59):
   
    if  (CT>=0)and (CT<=1000):
       
        CT_h = CT // 60      #  조리타임 시  계산
        CT_m = CT % 60    # 조리타임 분 계산
   
        NT_h = NT + CT_h     #현재시간과 의 시 와 조리시간의 시
        NT_m = NT2 + CT_m  #현재시간과 의 분 와 조리시간의 분


        if (NT_m >=60):    # 현재시간의 분이 60분보다 높다면 
            NT_h += 1      # 현재시간 1시간을 추가시킨다 
            NT_m = NT_m - 60  #60분을 빼면 현재시간의 분이다
           
        if (NT_h >=24):    #현재시간의 시가 24보다 높거나 같으면
            NT_h =NT_h - 24  #  24시간을 빼준다 
        print(NT_h,NT_m)       #출력은 현재시간의 시와 현재시간의 분이다

    




    
# 주사위 세개 문제 
# dice = input()    
# spl = dice.split(" ")
# dice1 =int(spl[0])
# dice2 =int(spl[1])
# dice3 =int(spl[2])


# if dice1 == dice2 == dice3 :
#    print( 10000 + dice1 * 1000)
# elif dice1 == dice2 or dice1 == dice3 :
#     print( 1000 + dice1 * 100)
# elif dice2 == dice3:
#     print( 1000 + dice2 * 100)   

# else: 
#      print(max(dice1,dice2,dice3) * 100)

    




    
    
    
    

    
    
    
       