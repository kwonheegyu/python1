#아스키 코드 문제

# aski_code = input()
                           
# print(ord(aski_code))   # ord 문자열에서 아스키 코드 값을 리턴하는 함수    

#숫자의 합 문제

# the_num = int(input())
# num = input()
# num_list =list(map(int,[idx for idx in num]))

# cnt = 0  
# for j in num_list:
#     cnt +=j
# print(cnt)

# 알파벳 찾기 문제
# word = input()
# askii_list = list(map(chr,[idx for idx in range(97,123)]))
# find_list = list(map(str,[word.find(idx) for idx in askii_list]))
# ans = ' '.join(find_list)

# print(ans)

# for idx in askii_list:
#     k = word.find(idx)
    


# 문자열 반복 문제

    
# s = int(input())

# for idx in range(s):
#     thr = input()
#     spl = thr.split(" ")
    
#     num_n = spl[0]
#     int_1 = int(num_n)
#     str_1 = spl[1]
#     list_1 =  [k for k in str_1]
#     list_2 = [j*int_1 for j in list_1]
#     answer = ''.join(list_2)
#     print(answer)   


# 단어 반복 문제 *****

# word = input()

# word_list =[idx for idx  in word]
# print(word_list)

   
# count_list = list(map(int,[word_list.count(idk) for idk in word_list]))
# print(count_list)

# dictionary = dict(zip(word_list,count_list))
# print(dictionary) 
# keys_1 = list(dictionary.keys())
# values_1 = list(dictionary.values())
# max_1 = max(values_1)
# print(max_1)
# position = values_1.index(max_1)
# print(keys_1[position])
# a=[]
# for letter in dictionary:
    
#     if dictionary.get(letter) == max_1:
#         a.append(max_1)
        
#         print(a)
# if len(a)>=2:
#     print("?")        
# else:
#     print("".join(a).upper())        

# 단어의 개수 문제


# eng_word = input()
# _split = eng_word.split(" ")

# res = []
# for idx in _split:
#     if idx.strip():  # 
#         res.append(idx)
    
# print(len(res))
        
# 상수 문제

# num = input()
# spl = num.split(" ")
# x = spl[0]
# num_1 = [idx for idx in x]
# num_1.reverse()
# join_1="".join(num_1)

# y = spl[1]
# num_2 = [id for id in y]
# num_2.reverse()
# join_2="".join(num_2)

# print(max(join_1,join_2))




# 다이얼 문제 

        
# 백준 모범답안
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):   # 입력한 값의 개수 
#     for i in dial:      #이중 반복문을 통해 
#         if a[j] in i:   # dial 하나씩 입력한 값의 위치가 맞는다면
#             ret += dial.index(i)+3 # 이 위치의 +3을 한다
# print(ret)
 
# 문제 푸는 순서
# 리스트를 만든 이 위치+3을 한것들을 합친다    
          
           
# 크로아티아 알파벳
# croatia=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpabet = input()
# cnt = 0
# for i in croatia:
#     if i in alpabet:
#         alpabet = alpabet.replace(i,"@")
        
# print(len(alpabet))



# 최댓값,최솟값 구하는 코드 (max,min 없이)

# int_1 =  list(map(int,input().split(" ")))

# max1 = int_1[0]

# for idx in range(1,len(int_1)):
#     print(idx)
#     if int_1[idx] > max1:
#         max1 = int_1[idx]
# print(max1)        


#그룹 단어 체커 문제
words_num = int(input())
cnt = 0
_sum = 0  
for idx in range(words_num):
    word = input()
    new  = ''
    prev = ''
    for i in word:
    
        if len(new)== 0: #첫 문자만 성립
            new += i
            prev = i
        if i == prev: # 문자가 전에꺼랑 같으면 건너뛰기
            continue
        else:
            new += i #두번째 문자에서부터 차근차근 저장 
            prev = i  #그래서 결국 답은 happy에서 hapy
      
    if  len(new)==len(set(new)):
        cnt += 1
print(cnt)    
        

          
      

        
            
    


        
        
    
    
     














    
    
    
    
  
    



    
    
  
    
    
    
    
    
   