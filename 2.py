import math
import random
r=random.uniform(1000000000000, 9000000000000)
r=float(r)
print(r)
count = 0
count = float(count) 
def take(r, count):
    while r>100.0:
        r=r/100.0
        count+=1
    return r, count
rlist=take(r, count)
smallenr=0
smallenr=float(smallenr)
smallenr=rlist[0]
rlistmigi=rlist[1]
ten = 10**rlistmigi
print(f'{ten}で割りました')
total = ten
count = 0
def divide4(r, count):
    while (r**2.0/4.0)>4.0:
        count+=1
        r=r/4.0
    return r,count
smallenr=float(smallenr)
rlist2 = divide4(smallenr, count)
smallenr=rlist2[0]
rlist2migi=rlist2[1]
four=0.0
four = 4**rlist2migi
print(f'{four}で割りました')
total = total*(4**rlist2migi)
print(f'totalは{total}です')
print(f'小さくなったrは{smallenr}です')
s=0.0
s=smallenr**2
print(f'r^2は{s}です')
t=0.0
t=float(t)
print(f'現在のルートの二乗は{s}です。')
def nibunhou(r, t):
    MAXTIMES = 10
    i=1
    k=1
    s=r**2
    t=math.floor(r)
                      
    #while k<=MAXTIMES:
        #print(f't、つまり小さくしたrの二乗のfloorは{t}です。')
#        if k==1:
#            k+=1
#            i+=1
#   
    print(f'rは{r}です。')
    while k<=MAXTIMES:
        print(f'tは{t}です。')
        
        if t**2<s:
            print(f'{0.5**i}を足します')
            t=t+0.5**i
    #        if tmp<s:
    #            t=t+0.5**i
        elif t**2>s:
            print(f'{0.5**i}を引きます')
            t=t-0.5**i
    #        if tmp<s:
    #            t=t-0.5**i
        else:
            print("ぴったりです")
            break
        i+=1
        k+=1
    print(f'tは{t}です。')    
    return t
root = total * nibunhou(smallenr,t)    
print(f'ルートは{root}です')