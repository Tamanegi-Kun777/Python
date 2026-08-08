import random

list= random.sample(range(100), k=100)
i=0
j=0
k=0
tmp=0
while i<16:
#list[0]>15 or list[1]>15  or list[2]>15  or list[3]>15 or list[4]>15  or list[5]>15  or list[6]>15:

    if list[j] > 15:
        print('list[j] > 15')
        print('list[j]=',list[j])
        k=16
        while True:
            
            if list[k] > 15:
                k+=1
                print('k=',k)
                if k==100:
                    print('break100')
                    break
            else:
                print('break')
                print('list[k]=',list[k])
                break
        print('k=',k)
        print('list[k]=',list[k])
        #if list[k] <= 15 and k < 100:
        tmp=list[j]
        print('tmp=',tmp)
        list[j]=list[k]
        print('list[j]=',list[j])
        list[k]=tmp
        k=0
        print('list[j]=',list[j])
        print('list[k]=',list[k])
    else:pass
    j+=1

    i+=1

print(list)
i=99
j=16
while i>=84:
    j=83
    while True:
        if list[j] > 83:
            print('list[j] > 84')
            print('list[j]=',list[j])
            print('break')
            break        
        else:
            j-=1
            if j==0:
                print('break0,j')
            print('list[j] <= 84')
            print('list[j]=',list[j]) 
            print('j=',j)   
    k=99
    while True:
        if list[k] < 84:
            tmp=list[k]
            print('tmp=',tmp)
            list[k]=list[j]
            print('list[k]=',list[k])
            list[j]=tmp
            print('list[j]=',list[j])
            break
    #    print('list[k] < 84, list[k]=',list[k])
        else:
            k=k-1
            if k==83:
                print('break83,k')
                break     
    print('list[k]=',list[k])
    print('list[j]=',list[j])
    
    i=i-1    

print(list)
