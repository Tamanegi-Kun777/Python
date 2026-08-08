def russian_multiply(a, b):
    a = a[:]        # 元のリストを壊さないようコピー
    b = b[:]
    result = [0]
    while not is_zero(a):
        if is_odd(a):
            result = add(result, b)   # aが奇数なら b を足す
        a = halve(a)                  # a を半分に
        b = double(b)                 # b を2倍に
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

BASE = 100000
FRAC_BLOCKS = 2

def divide_by_shift(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")

    # ===== 整数部: 引き算とビットシフトによる2進長除法 =====
    quotient = 0
    remainder = a
    if a >= b:
        shift = 0
        while (b << (shift + 1)) <= a:   # bをaの直下まで持ち上げる
            shift += 1
        for s in range(shift, -1, -1):   # シフトを1つずつ下げる
            if remainder >= (b << s):    # 引けるか?
                remainder -= (b << s)    # 引く
                quotient |= (1 << s)     # 商のビットsを立てる
    int_part = quotient

    # ===== 小数部: 余りを10進で下ろす =====
    frac_blocks = []
    r = remainder
    for _ in range(FRAC_BLOCKS):
        r *= BASE
        frac_blocks.append(r // b)
        r = r % b

    int_blocks = [int_part % BASE, (int_part // BASE) % BASE]
    return int_blocks, frac_blocks

#BASE = 100000
#FRAC_BLOCKS = 2  # 小数部のブロック数(2ブロック = 小数第10位まで)

def divide(a_digits, b_digits):
    a = to_int(a_digits)
    b = to_int(b_digits)
    if b == 0:
        raise ValueError("0で割ることはできません")

    # 整数部と余り
    int_part = a // b
    remainder = a % b

    # 小数部: 余りを BASE 倍しては割る、を繰り返す
    frac_blocks = []
    for _ in range(FRAC_BLOCKS):
        remainder *= BASE
        frac_blocks.append(remainder // b)
        remainder = remainder % b
    # (残った remainder は切り捨て)

    return to_digits(int_part), frac_blocks

#BASE = 100000

def multiply(a_digits, b_digits):
    result = [0] * (len(a_digits) + len(b_digits))

    for i in range(len(a_digits)):
        carry = 0
        for j in range(len(b_digits)):
            cur = result[i + j] + a_digits[i] * b_digits[j] + carry
            result[i + j] = cur % BASE
            carry = cur // BASE
        result[i + len(b_digits)] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result
#BASE = 100000
#FRAC_BLOCKS = 2

def divide_by_shift(a, b):
    if b == 0:
        raise ValueError("0で割ることはできません")

    # ===== 整数部: 引き算とビットシフトによる2進長除法 =====
    quotient = 0
    remainder = a
    if a >= b:
        shift = 0
        while (b << (shift + 1)) <= a:   # bをaの直下まで持ち上げる
            shift += 1
        for s in range(shift, -1, -1):   # シフトを1つずつ下げる
            if remainder >= (b << s):    # 引けるか?
                remainder -= (b << s)    # 引く
                quotient |= (1 << s)     # 商のビットsを立てる
    int_part = quotient

    # ===== 小数部: 余りを10進で下ろす =====
    frac_blocks = []
    r = remainder
    for _ in range(FRAC_BLOCKS):
        r *= BASE
        frac_blocks.append(r // b)
        r = r % b

    int_blocks = [int_part % BASE, (int_part // BASE) % BASE]
    return int_blocks, frac_blocks

def add_bignum(a_digits, b_digits):
    # a_digits, b_digits は下位から [下5桁, 次の5桁, ...] のリスト
    result = []
    carry = 0
    for i in range(max(len(a_digits), len(b_digits))):
        da = a_digits[i] if i < len(a_digits) else 0
        db = b_digits[i] if i < len(b_digits) else 0
        s = da + db + carry
        result.append(s % 100000)   # この桁に残す分
        carry = s // 100000         # 上の桁へ繰り上げる分
    if carry:
        result.append(carry)
    return result
a_digits = [50000,48000]  # 4800050000
b_digits = [50000,4000]  # 400050000
result = add_bignum(a_digits, b_digits)
print(result)  # [0, 1] つまり 100000

def sub_bignum(a_digits, b_digits):
    result = []
    borrow = 0                        # carry ではなく borrow(借り)
    if len(a_digits) < len(b_digits):
        tmp = a_digits
        a_digits = b_digits
        b_digits = tmp
        tmp= -1
    for i in range(max(len(a_digits), len(b_digits))):
        da = a_digits[i] if i < len(a_digits) else 0
        db = b_digits[i] if i < len(b_digits) else 0
        s = da - db - borrow          # 足すのではなく引く
        if s < 0:                     # 引けない(マイナス)なら
            s += BASE                 # 上の桁から BASE を借りる
            borrow = 1
        else:
            borrow = 0
        result.append(s)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result*tmp