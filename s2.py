import math
import random
import numpy as np
#TRIL=1000000000000
TRIL=100000
num=1000000
rlist=[0]*num
i=0
sum=[0,0,0,0]
l=[0.0]
for i in range(num):
#    rlist[i]=r=random.uniform(500000000000, 10000000000000)
    rlist[i]=r=random.randint(500000000000*1000, 10000000000000*1000)
print(rlist)
while i<num:
    k=0
    l=0
    sum[0]+=rlist[i]
    print('sum[0]=',sum[0])
#    if sum>=TRIL
    def minus(sum0):
        j=1
        sum1=1
        if sum0<TRIL**4:
            pass
        elif sum0>=TRIL**4:
            print('sum0=',sum0)
            j=1
            while sum0>=TRIL**4:
                sum0=sum0-TRIL**4
                j+=TRIL**4
                print('sum0=',sum0)
                print('j=',j)
        sum1+=j
        if sum0<TRIL**3:
            pass
        elif sum0>=TRIL**3:
            j=1
            while sum0>=TRIL**3:
                sum0=sum0-TRIL**3
                j+=TRIL**2
        sum1+=j
        if sum0<TRIL**2:
            pass
        elif sum0>=TRIL**2:
            j=1
            while sum0>=TRIL**2:
                sum0=sum0-TRIL**2
                j+=TRIL
        sum1+=j
        if sum0<TRIL:
            pass
        elif sum0>=TRIL:
            print('sum0=',sum0)
            print('sum0はTRILより大きい')
            j=1
            while sum0>=TRIL:
                sum0=sum0-TRIL
                j+=1
        sum1+=j
        return sum0,sum1
    l=minus(sum[0])
    sum[0]=l[0]
    sum[1]=l[1]        
    print('l[0]=',l[0])
    print('l[1]=',l[1])
    l=minus(l[1])
    print('l[0]=',l[0])
    print('l[1]=',l[1])

    sum[1]=l[0]
    sum[2]=l[1]    
    print('sum[2]=',sum[2])
    l=minus(l[1])
    print('l[0]=',l[0])
    print('l[1]=',l[1])
    print('sum[3]=',sum[3])
    sum[2]=l[0]    
    sum[3]=l[1]
    print('sum[3]=',sum[3])
    if sum[3]>=TRIL:
        print('数が大きすぎます。sum[3]=',sum[3])
    print(sum)
    
    i+=1