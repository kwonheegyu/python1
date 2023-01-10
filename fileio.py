
# fd = open("git.py","a")
# fd.write("delete\n") 
# fd.close()

# fd = open("git.py","r")

# var = fd.readlines()
# for idx in var:
    
#     print(idx.strip())
# fd.close()
fd = open("input.txt","r")
var = fd.readlines()
cnt = 0
input = ""
for idx in var:
    cnt+=1
    k=idx.strip()
    input +=  f"{cnt} {k}\n"
fd.close()

fd = open("out.txt","w")
var = fd.write(input)
fd.close()

