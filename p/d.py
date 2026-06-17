data = [[3,7],[],[1,5],[],[],[],[],[],[0,4],[],[2,6],[],[],[],[],[]]
byteSize = 4
depth=0
j=0
l=[]
i=0
k=0
while data!=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]:
    print('data=',data)
    print('k=',k)
    i=0  
    while i<16:
        print('i=',i)    
        print('data[[i][depth]]=',data[[i][depth]])
        print('depth=',depth)
        if data[[i][depth]]!=[]:
            print('hit1')
#        print('data[[i][j]][0]=',data[[i][j]][0])
            print('depth=',depth)
            if data[[i][0]][0]==j:
                print('i=',i)
                print('hit2',data[[i][0]][0])
                del data[[i][0]][0:1]
                if data[[i][0]]!=None:
                    print('削除後',data[[i][0]])
                l.append(i)
                j+=1
#            l.append(data[[i][j]].pop(0))
            print(l)            
#    print('i=',i)
        i+=1
    k+=1
lstr = list(map(str, l))
print(lstr)

#String=''.join([str(i) for i in lstr])
#print(String)

#print(*[str(i) for i in lstr], sep='')
#decoded_string = bytes.fromhex(String).decode('utf-8')