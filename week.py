
name = input("나의 이름은? ")
age = input("나의 나이는?")
python_start = input("파이썬 시작한 날짜는?")
gosu = input("숨은 고수 선생님의 이름은?")

print("all answer",name ,age , python_start , gosu)
print("all answer %s %s %s %s" % (name, age ,python_start ,gosu) )
print("all answer {0} {1} {2} {3}" .format (name, age ,python_start ,gosu) )
print(f"all answer  {name} {age}  {python_start} {gosu}" )


typecasting1 = input("형 변환 숫자 : ")
typecasting2 = input("형 변환 숫자 : ")

print(int(typecasting1) + int(typecasting2) ) 
print(str(typecasting1) + str(typecasting2) )


number1 = 10
number2 = 3 

print(number1 ,"+", number2, "=" , number1 + number2 )


num1 = input("number1:")
num2 = input("number2:")


print(num1, "+" , num2, "=", int(num1) + int(num2))
print(num1, "-" , num2, "=",int(num1) - int(num2))
print(num1, "*" , num2, "=",int(num1) * int(num2))
print(num1, "/" , num2, "=",int(num1) / int(num2))
print(num1, "//" , num2, "=",int(num1) // int(num2))
print(num1, "%" , num2, "=",int(num1) % int(num2))
print(num1, "**" , num2, "=",int(num1) ** int(num2))



num1 = input("number1:")
num2 = input("number2:")

print(f"{num1} + {num2} =",int(num1) + int(num2))
print(f"{num1} - {num2} =",int(num1) - int(num2))
print(f"{num1} * {num2} =",int(num1) * int(num2))
print(f"{num1} / {num2} =",int(num1) / int(num2))
print(f"{num1} // {num2} =",int(num1) // int(num2))
print(f"{num1} % {num2} =",int(num1) % int(num2))
print(f"{num1} ** {num2} =",int(num1) ** int(num2))

print("{0} + {1} = {2}".format(num1,num2,int(num1)+int(num2))
      )



