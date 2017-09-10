class check:
    def __init__(self,c):
        self.c=c
    def dec(self):
        self.c-=1
    def done(self):
        return self.c==0
def find_next(t,i):
    c=0
    while True:
        i+=1
        if t[i]=='(':c+=1
        if t[i]==')':c-=1
        
        if c==0:break
    i-=1
   
    if t[i] not in ('(',')'): return i
    while True:
      
        
        if t[i]=='(':c+=1
        if t[i]==')':c-=1
        i-=1
        if c==0:return i
        
    
def calc(t,i):
    global var
    global func
    if t[i] in ('(',')'):return calc(t,i+1)
    
    if t[i] in var:
        if var[t[i]]==None:
            x=input('Input:'+t[i]+'=')
            x=int(x)
            var[t[i]]=x
            
        return var[t[i]]
    if t[i]=='h':
        return calc(t,i+1)+1
    if t[i]=='f': return calc(t,i+1) + calc(t,find_next(t,i))
    if t[i]=='g': return calc(t,i+1) * calc(t,find_next(t,i))

s=input().replace(' ','')
t=''

var={'x':None,'y':None,'z':None,'c':0}
func=['f','g','h']
l=[]

for i in s:
    if i in func:
        t+=i
        if i=='h':
            l.append(check(1))
        else:
            l.append(check(2))
        t+='('
    if i in var:
        l[-1].dec()
        t+=i
    while True:
        if l[-1].done():
            l.pop()
            t+=')'
            if len(l)==0:break
            l[-1].dec()
            continue
        break
print(t)

print('result:',calc(t,0))
        
    
