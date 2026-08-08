import copy
import math
import random
from itertools import accumulate
from typing import List

list= random.sample(range(100), k=100)
print(list)

#list=list.extend([0,0,0,0,0,0,0,0,0,0])
sumnum = 0
average = 0
MAX_LENGTH = 100
#def averagecalc(list):
#    length=MAX_LENGTH
#    i=0
#    sum=0
#    for i in range(len(list)):
#        sum += list [i]
#    if length == 0:
#        return 0
#    average = sumnum / length 
#    return average
def mergesortseed(migi,hidari):
    if hidari > migi:
        tmp = migi
        migi = hidari
        hidari =tmp
    print(f'migi={migi},hidari={hidari}')
    return migi,hidari
    j=0
    k=0
    l=0
    m=0
    n=0

def mergesort(place,list):
    k=0
    j=0
    l=0
    i=place
    for i in range (8):
        print('list[j]=',list[j])
        list[j],list[j+1]=mergesortseed(list[j],list[j+1])
        j+=2        
    for i in range (4):
        list[k],list[k+2]=mergesortseed(list[k],list[k+2])
        list[k+1],list[k+3]=mergesortseed(list[k+1],list[k+3])
        k+=3
    for i in range (2):
        list[l],list[l+4]=mergesortseed(list[l],list[l+4])
        list[l+2],list[l+6]=mergesortseed(list[l+2],list[l+6])
    return list

def mergesort2(place,list):
    k=0
    j=0
    l=0
    m=0
    i=place
    for i in range (16):
        list[j],list[j+1]=mergesortseed(list[j],list[j+1])
        j+=2        
    for i in range (8):
        list[k],list[k+2]=mergesortseed(list[k],list[k+2])
        list[k+1],list[k+3]=mergesortseed(list[k+1],list[k+3])
        k+=4
    for i in range (4):
        list[l],list[l+4]=mergesortseed(list[l],list[l+4])
        list[l+2],list[l+6]=mergesortseed(list[l+2],list[l+6])
        l+=8
    for i in range (2):
        list[m],list[m+8]=mergesortseed(list[m],list[m+8])
        list[m+4],list[m+12]=mergesortseed(list[m+4],list[m+12])
        m+=16
    return list
def mergesort3(place,list):
    minus = 3
    h=0
    l=0
    k=0
    j=0
    n=0
    revl=0
    dist=4
    i=place
    for i in range (9):
        list[j],list[j+1]=mergesortseed(list[j],list[j+1])
        j+=2
    for i in range (4):    
        list[n],list[n+2]=mergesortseed(list[n],list[n+2])
        list[n+1],list[n+3]=mergesortseed(list[n+1],list[n+3])
        n+=4
    for i in range (2):
        tmp=0
        
        for k in [0,dist]:
            list[k],list[k+8]=mergesortseed(list[k],list[k+8])
        for l in range (4):
            revl=3-l
            if list[revl+minus*4] < list[revl+minus*3]:
                tmp = list[revl+minus*4]
                list[revl+minus*4] = list[revl+minus*3]
                list[revl+minus*3] = tmp
        for h in range (2):
            list[h],list[h+8]=mergesortseed(list[h],list[h+8])
    return list          

length=MAX_LENGTH
i=0
sum=0

#for i in range(110):
#    sum += list [i]
#sum=[accumulate(list_calc)-1]

if length == 0:
    zeroflag = True
else:
    zeroflag = False
average = sumnum / length 
if zeroflag == True:
    print("0")
ave=int(average/3)
def calcdistance(list_tmp,m):
    for i in range (ave*2):
        if abs(list_tmp[m]-average) < ave:
            list_tmp.append(list[m])

    mergesort2(35,list)
    return list
            
list=mergesort(0,list)
print(list)
j=0
list=mergesort(84,list)
j=0
list_tmp=calcdistance(list,17)
list=mergesort3(65,list)
j=0
list=mergesort3(64,list)
j=0
k=0
n=0

print(list)