ped = 1013
prod = 568
#ped = bin(ped)
#prod = bin(prod)
sum = 0
print(prod)
print(ped)
bitshifttimes = 0
mid = prod
while mid != 0:
    if mid % 2 == 0:
        print('mid % 2 == 0')
        print('mid = ', mid)
        bitshifttimes += 1
        print('bitshifttimes = ', bitshifttimes)
        mid = mid >> 1
        print('mid >> 1 = ', mid)
 
    else:
        print('mid % 2 == 1')
        print('mid = ', mid)
        print('bitshifttimes = ', bitshifttimes)
        print('2**bitshifttimes = ', 2**bitshifttimes)
        #if mid == 1:
        #    print('midが1です。')
        #    break
        sum += ped*(2**bitshifttimes)
        bitshifttimes += 1

        #bitshifttimes2 = 1
        #if mid <=1:
        #   print('midが1以下です。')
        #    break
        mid = mid // 2
        print('mid // 2 = ', mid)
        
#sum += ped*(2**bitshifttimes)
print('sum = ', sum)
    
