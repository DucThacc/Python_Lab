# Bài 34: Đổi thập phân sang nhị phân (không dùng bin())
n = int(input("Nhập số nguyên dương: "))
if n == 0:
    print("0")
else:
    bits = ""
    x = n
    while x > 0:
        bits = str(x % 2) + bits
        x //= 2
    print(bits)
