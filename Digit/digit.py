import random
import time
import threading

def calc(n):
    s=0
    i=0
    while n>0:
        t=min(9*10**i,n)
        s+=t*(i+1)
        n=n-t
        i+=1
        
    return s


    
def digit(x):
    i=1
    while True:
        t=calc(i)
        if x-t<=0:
            
            break
        x-=t
        i+=1
    i = 1
    c = 9
    while x > i * c:
        x -= i * c
        i += 1
        c *= 10
    x-=1
    s=x/i
    t=x%i
    result = c/9+s
    return int(str(result)[t])
    


def makestring(n):
    i=1
    t=''
    s=''
    while True:
        t+=str(i)
        s+=t
        if len(s)>=n:break
        i+=1
    return s[0:n]
n=1000
start=time.time()
print(calc(4))

print('n=',n,'\n',time.time()-start)
    
