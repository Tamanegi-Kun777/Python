import math
import numpy as np
def equal(a, b):
    SEIDO = 0.000000000000005 #ズレてくる桁の一つ上。50ズレれば等しいと判定されない。一回の計算で3～4ズレるので、13回ぐらい計算するとズレてしまう。
    if abs(a - b) < SEIDO:
        return round(a)
    else:
        return False
def bunkai(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

p_ = 104707
q = 87559

p = p_*q

d1 = 2003
d2 = 2104

n = p // d1
c = p % d1
print("n=", n)
check = equal(p, d1 * n  + c)
print("check=", check)
k=0
p2 = d2 * n + c
print("p2=", p2)
process_p_1=d1*(p2-c)/d2+c
if isinstance(d1*(p2-c)/d2, int):
    print("p is maybe prime...", p)
else:
    factors1=bunkai(d1)
    factors1_=bunkai(p2-c)
    factors1.extend(factors1_)
    factors2=bunkai(d2)
    first = 1
    i_=1
    dup=[]
    if factors1 == []:
        print("素因数なし")        
    else:
        print("factors1=", factors1)
        flen1=len(factors1)
        flen2=len(factors2)
        for i in range (flen1):
            index=1
            for j in range(flen2):
                if factors1[i] == factors2[j]:
                    print("これは素因数がある")        
                    print("index=",index)
                    print("i=",i)
                    print("j=",j)
                    print("factors2[j]=",factors2[j])
            
                    while factors2[j] % index+1 == 0:
                        factors2[j]=factors2[j]/i
                        i_=i_*i
                    if first == 1:
                        dup = [i_]
                        first = 0
                        index+=1
            #if index=1
            #    breakflag = 1
            #    break
            #    elif dup[index] == dup[index+1]:
                        
            #        elif (index==len(dup)):
            #            dup.extend([i_])
            #            index+=1
            #    if dup == None:
            #        noneflag = 1
            #    else:
            #        noneflag = 0
            #    break
                    print ("dup=", dup)
            #    if noneflag == 1:
            #        continue
            #    else:
            #        for k in range(len(dup)):
            #            print("dup=", dup[k])
                
    for l in range(len(dup)):
        process1 = d1*(p2-c)/dup[l]
        process2 = d2/dup[l]









factorsc = []
for i in range(2, int(math.sqrt(process1)) + 1):
    while n % i == 0:
        factorsc.extend([i])
        n //= i
if n > 1:
    factorsc.extend(process1)

#factorsc2=bunkai(c)


factorsc2 = []
for i in range(2, int(math.sqrt(c)) + 1):
    while n % i == 0:
        factorsc.extend([i])
        n //= i
if n > 1:
    factorsc.extend(c)




#factorsc2=bunkai(c)








pfac=1
print("factorsc=",factorsc)
#factorsc=np.array(factorsc).flatten()
#factorsc2=np.array(factorsc2).flatten()
#print("factorsc=",factorsc)

for i, factorsc in enumerate(factorsc):
    for j, factorsc2 in enumerate(factorsc2):
        if factorsc[i] == factorsc2[j]:
            pfac=pfac*i #素因数の積をpfacに入れる

if pfac == 1:
    print("答えはありません", pfac)
else:
    print("答えは", pfac)
    answer2=(process1+c)/pfac                
    print("と", answer2)

    
