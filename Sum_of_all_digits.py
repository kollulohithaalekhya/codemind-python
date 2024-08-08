n=int(input())
t=n
r=0
s=0
while t>0:
    r=t%10
    s+=r
    t=t//10
print(s)