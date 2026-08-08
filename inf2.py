def plus(x, y):
    while y != 0:
        carry = x & y      # 両方1のビット = 繰り上がりが発生する桁
        x = x ^ y          # 繰り上がりを無視した各桁の和(XOR)
        y = carry << 1     # 繰り上がりを1つ上の桁へ
    return x

print(plus(50000, 50000))  # 100000