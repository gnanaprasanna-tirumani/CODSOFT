import random
print("welcome")
a=int(input("how amny letters you want in your password"))
b=int(input("how many symbols you want in your password:"))
c=int(input("enter how many numbers you want in your password:"))
string=[]
string2=''
for i in range(a):
    k=random.randint(65,122)
    #print(chr(91))
    if k>=91 and k<=96:
        print(chr(k))
        k+=6
    string+=chr(k)
for i in range(b):
    k=random.randint(33,47)
    string+=chr(k)
for i in range(c):
    k=random.randint(48,57)
    string+=chr(k)
#print(string) 
random.shuffle(string)
#print(string)
"""for i in string:
    string2+=i
print(string2)"""
string2=''.join(map(str,string))
print(string2)
  