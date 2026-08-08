#def ketakesi(y):
#    while y >> 1 == y:
#        y = y >> 1 
#    return y
MAX = 100000
higher = MAX/2
def plus(x,y,higher):
    x2 = 0
    count = 0
    count2 = 0
    kuriagari = 0
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y != 0:
        return y
    elif x != 0 and y == 0:
        return x
    if x % 2 == 0 and y % 2 == 0:
        x >>= 1
        y >>= 1
        count += 1
        if x2 != 0:
            x2 <<= (count2+1)
            count+=count2+1
            count2=0
        elif x2 == 0:
            count2 += 1
        print("1:x=",x)
        print("1:y=",y)
        print("1:x2=",x2)
        kuriagari = 0
    elif (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
        x2 += 1
        x >>= 1
        y >>= 1
        kuriagari = 0
        if x2 != 0:
            x2 <<= (count2+1)
            count+=count2+1
            count2=0
        elif x2 == 0:
            count2 += 1
        print("2:x=",x)
        print("2:y=",y)
        print("2:x2=",x2)
    elif (x % 2 == 1 and y % 2 == 1):
        x2 += 2
        x2 <<= (count2+1)
        count += 1
        x >>= 1
        y >>= 1
        kuriagari = 1
        if x2 != 0:
            x2 <<= (count2+1)
            count+=count2+1
            count2=0
        elif x2 == 0:
            count2 += 1
        print("3:x=",x)
        print("3:y=",y)
        print("3:x2=",x2)
    while (x != 0 or y != 0):
        if x % 2 == 0 and y % 2 == 0 and kuriagari == 0:
            x >>= 1
            y >>= 1
            x2 <<= (count2+1)
            count += 1
            kuriagari = 0        
            if x2 != 0:
                x2 <<= (count2+1)
                count+=count2+1
                count2=0
            elif x2 == 0:
                count2 += 1
        elif ((x % 2 == 1 and y % 2 == 0 and kuriagari == 0) or (x % 2 == 0 and y % 2 == 1 and kuriagari == 0) or (x % 2 == 0 and y % 2 == 0 and kuriagari == 1)):
            x2 += 1
            x2 <<= (count2+1)
            count += 1
            x >>= 1
            y >>= 1
            kuriagari = 0 
            if x2 != 0:
                x2 <<= (count2+1)
                count+=count2+1
                count2=0
                print("4:x=",x)
                print("4:y=",y)
                print("4:x2=",x2)
            elif x2 == 0:
                count2 += 1
        elif (x % 2 == 1 and y % 2 == 1 and kuriagari == 0) or (x % 2 == 0 and y % 2 == 1 and kuriagari == 1) or (x % 2 == 1 and y % 2 == 0 and kuriagari == 1):
            x2 += 2
            count += 1
            x >>= 1
            y >>= 1
            kuriagari = 1 
            if x2 != 0:
                x2 <<= (count2+1)
                count+=count2+1
                count2=0
                print("6:x=",x)
                print("6:y=",y)
                print("6:x2=",x2)
            elif x2 == 0:
                count2 += 1
        elif (x % 2 == 1 and y % 2 == 1) and kuriagari == 1:
            x2 += 3
            count += 1
            x >>= 1
            y >>= 1
            kuriagari = 1 
            print("6:x=",x)
            print("6:y=",y)
            print("6:x2=",x2)
            if x2 != 0:
                x2 <<= (count2+1)
                count+=count2+1
                count2=0
                print("7:x=",x)
                print("7:y=",y)
                print("7:x2=",x2)
            elif x2 == 0:
                count2 += 1
        if x == 0:
            x2 += (y >> count)
            return x2
        elif y == 0:
            x2 += (x >> count)
            return x2
        if x2 >= MAX:
            x2 = 0
            higher += 1
    return x2
y=50000
x=50000
result = plus(x,y,higher)
print(result)



    