# bin = ["hello",1,2,4,["h","e","e"]]
'''
# print(bin[-1][1])

binList = []
user = input("다섯가지의 숫자의 리스트는?") 
binList.extend(user) 
print(binList) 


binList.sort()
print(binList)

binList.reverse()
print(binList)

binList.clear()
print(binList)


bindict = {}

bindict["다이소"] = "diso"
bindict["티슈"] = "tissu"
bindict["파이썬"] = "python"
bindict["내 몸무게"] = "68kg"
bindict["키"] = "171cm"

print(bindict)


print(bindict["내 몸무게"])
print(bindict["티슈"])
print(bindict["파이썬"])
print(bindict["키"])
print(bindict["다이소"])

del bindict["티슈"]
print(bindict)
'''
two = input("숫자는:")
split = two.split(" ")
var1 = int(split[0])
var2 = int(split[1])

if((var1 >= -10000) and (var1 <= 1000)) and ((var2 >= -10000) and (var2 <= 1000)):
  if var1>var2: 
    print(">")
  elif var1<var2:
    print("<")
  elif var1 == var2:
    print("==")