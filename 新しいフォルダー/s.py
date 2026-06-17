import math
import random
#TRIL=1000000000000
TRIL=100000
num=1000000
rlist=[0]*num
i=0
sum=[0,0,0,0]
for i in range(num):
    rlist[i]=r=random.uniform(500000000000, 10000000000000)
print(rlist)
while i<num:
    j=0
    k=0
    l=0
    sum[0]+=rlist[i]
    print('sum[0]=',sum[0])
#    if sum>=TRIL
    while sum[0]>=TRIL:
        sum[0]-=TRIL
        j+=1
    sum[1]+=j
    print('sum[1]=',sum[1])
    while sum[1]>=TRIL:
        sum[1]-=TRIL
        k+=1
    sum[2]+=k
    print('sum[2]=',sum[2])
    while sum[2]>=TRIL:
        sum[2]-=TRIL
        l+=1
    print('sum[3]=',sum[3])
    sum[3]+=l
    if sum[3]>=TRIL:
        print('数が大きすぎます。sum[3]=',sum[3])
    print(sum)
    
    i+=1