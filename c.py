import os
import numpy as np
current_dir = os.getcwd()
print(f"現在の作業ディレクトリ: {current_dir}")


f = open('data.py', 'rb')
byteSize = 4
data = f.read(byteSize).hex()

print(list(data))
length=len(data)
new=[]
for i in range (length):
    new.append(int(data[i],16))
#    data[i] =  format(data[i], 'x')
print(list(new))
index=0
l=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

j=0
for i in range (byteSize*2):
    if new[i]==0:
        index=0
        l[index].append(j)
        print(f'0のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==1:
        index=1
        l[index].append(j)
        print(f'1のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==2:
        index=2
        l[index].append(j)
        print(f'2のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==3:
        l[index].append(j)
        print(f'3のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==4:
        l[index].append(j)
        print(f'4のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==5:
        l[index].append(j)
        print(f'5のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==6:
        l[index].append(j)
        print(f'6のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==7:
        index=7
        l[index].append(j)
        print(f'7のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==8:
        index=8
        l[index].append(j)
        print(f'8のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==9:
        l[index].append(j)
        print(f'9のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==10:
        index=10
        l[index].append(j)
        print(f'10のデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==0x0a:
        l[index].append(j)
        elev.append(j)
        print(f'aのデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==0x0b:
        l[index].append(j)
        print(f'bのデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==0x0c:
        l[index].append(j)
        print(f'cのデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==0x0d:
        l[index].append(j)
        print(f'dのデータが{i}で入りました',i)
        print(f'lは',l)
    elif new[i]==0x0e:
        l[index].append(j)
        print(f'eのデータが{i}で入りました',i)
        print(f'lは',l)
    j+=1
#index=array[0x00][0]

#print(new[[0][0]]) 
         
print(l)



f.close()