# ============================================================
# 多倍長整数の四則演算(5桁=BASE ごとにブロック化、下位から並べる)
# 数の表現: (sign, digits)
#   sign  : +1(正) / 0(ゼロ) / -1(負)
#   digits: [下5桁, 次の5桁, ...] の絶対値リスト
# ============================================================

BASE = 100000

# ---------- 補助: 正規化・変換 ----------
def normalize(x):
    """上位の余分な0を除去(最低1ブロックは残す)"""
    x = x[:]
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x

def from_int(n):
    """普通の整数 -> (sign, digits)"""
    if n == 0:
        return (0, [0])
    sign = 1 if n > 0 else -1
    n = abs(n)
    digits = []
    while n > 0:
        digits.append(n % BASE)
        n //= BASE
    return (sign, digits)

def to_int(num):
    """(sign, digits) -> 普通の整数(検証・表示用)"""
    sign, digits = num
    v = 0
    for i in range(len(digits) - 1, -1, -1):
        v = v * BASE + digits[i]
    return sign * v

# ---------- 絶対値どうしの大小比較 ----------
def cmp_abs(a, b):
    """絶対値リスト a,b を比較。a>b:1, a<b:-1, a==b:0"""
    a, b = normalize(a), normalize(b)
    if len(a) != len(b):
        return 1 if len(a) > len(b) else -1
    for i in range(len(a) - 1, -1, -1):
        if a[i] != b[i]:
            return 1 if a[i] > b[i] else -1
    return 0

# ---------- 絶対値どうしの加算・減算(符号なしの部品) ----------
def add_abs(a, b):
    """絶対値どうしの足し算"""
    result = []
    carry = 0
    for i in range(max(len(a), len(b))):
        da = a[i] if i < len(a) else 0
        db = b[i] if i < len(b) else 0
        s = da + db + carry
        result.append(s % BASE)
        carry = s // BASE
    if carry:
        result.append(carry)
    return normalize(result)

def sub_abs(a, b):
    """絶対値どうしの引き算(a >= b 前提)"""
    result = []
    borrow = 0
    for i in range(max(len(a), len(b))):
        da = a[i] if i < len(a) else 0
        db = b[i] if i < len(b) else 0
        s = da - db - borrow
        if s < 0:
            s += BASE
            borrow = 1
        else:
            borrow = 0
        result.append(s)
    return normalize(result)

# ---------- 符号付き 加算・減算 ----------
def add(x, y):
    sx, ax = x
    sy, ay = y
    if sx == 0: return y
    if sy == 0: return x
    if sx == sy:
        # 同符号 -> 絶対値を足して、符号はそのまま
        return (sx, add_abs(ax, ay))
    # 異符号 -> 絶対値の大きい方から小さい方を引く
    c = cmp_abs(ax, ay)
    if c == 0:
        return (0, [0])
    elif c > 0:
        return (sx, sub_abs(ax, ay))
    else:
        return (sy, sub_abs(ay, ax))

def negate(x):
    s, a = x
    return (-s, a)

def sub(x, y):
    # x - y = x + (-y)
    return add(x, negate(y))

# ---------- 符号付き 乗算(筆算法) ----------
def mul(x, y):
    sx, ax = x
    sy, ay = y
    if sx == 0 or sy == 0:
        return (0, [0])
    result = [0] * (len(ax) + len(ay))
    for i in range(len(ax)):
        carry = 0
        for j in range(len(ay)):
            cur = result[i + j] + ax[i] * ay[j] + carry
            result[i + j] = cur % BASE
            carry = cur // BASE
        result[i + len(ay)] += carry
    return (sx * sy, normalize(result))

# ---------- 符号付き 除算(整数部+小数部) ----------
def divide(x, y, frac_blocks=2):
    """
    x / y を計算。整数部と小数部を返す。
    戻り値: (sign, int_digits, frac_digits)
      sign      : 全体の符号(+1/0/-1)
      int_digits: 整数部の絶対値リスト(下位から5桁)
      frac_digits: 小数部リスト(上位から5桁, frac_blocks個, 残りは切り捨て)
    """
    sx, ax = x
    sy, ay = y
    a = to_int((1, ax))   # 絶対値の整数
    b = to_int((1, ay))
    if b == 0:
        raise ValueError("0で割ることはできません")
    sign = sx * sy

    # 整数部: 引き算とビットシフトによる2進長除法
    quotient = 0
    remainder = a
    if a >= b:
        shift = 0
        while (b << (shift + 1)) <= a:
            shift += 1
        for s in range(shift, -1, -1):
            if remainder >= (b << s):
                remainder -= (b << s)
                quotient |= (1 << s)

    # 小数部: 余りを10進(5桁ずつ)で下ろす
    frac = []
    r = remainder
    for _ in range(frac_blocks):
        r *= BASE
        frac.append(r // b)
        r %= b

    # 商が0(整数部も小数部も0)なら符号は0に
    _, int_digits = from_int(quotient) if quotient != 0 else (0, [0])
    if quotient == 0 and all(f == 0 for f in frac):
        sign = 0
    return (sign, int_digits, frac)

# ---------- 表示用 ----------
def num_to_str(num):
    sign, digits = num
    if sign == 0:
        return "0"
    body = to_int((1, digits))
    return ("-" if sign < 0 else "") + str(body)

def div_to_str(result):
    sign, int_digits, frac = result
    int_val = to_int((1, int_digits))
    frac_str = "".join(f"{b:05d}" for b in frac)
    prefix = "-" if sign < 0 else ""
    return f"{prefix}{int_val}.{frac_str}"

# ============================================================
# 動作確認
# ============================================================
if __name__ == "__main__":
    print("=== 加算 ===")
    for A, B in [(50000,50000),(-30,70),(-100,-25),(12345,-12345)]:
        r = add(from_int(A), from_int(B))
        print(f"  {A} + {B} = {num_to_str(r)}  (正解 {A+B})")

    print("=== 減算 ===")
    for A, B in [(100000,50000),(530000,550000),(-100,-25),(7,7)]:
        r = sub(from_int(A), from_int(B))
        print(f"  {A} - {B} = {num_to_str(r)}  (正解 {A-B})")

    print("=== 乗算 ===")
    for A, B in [(99999,99999),(-1234,5678),(-12,-12),(0,999)]:
        r = mul(from_int(A), from_int(B))
        print(f"  {A} * {B} = {num_to_str(r)}  (正解 {A*B})")

    print("=== 除算(小数第10位まで, 残り切り捨て) ===")
    from decimal import Decimal
    for A, B in [(10,4),(100,3),(-22,7),(1234567890,123),(-1,-7)]:
        r = divide(from_int(A), from_int(B))
        got = div_to_str(r)
        exact = (Decimal(A)/Decimal(B)).quantize(Decimal(10)**-10, rounding='ROUND_DOWN')
        print(f"  {A} / {B} = {got}  (正解 {exact})")
