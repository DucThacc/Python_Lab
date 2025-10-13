# Bài 42: Hàm giai thừa, in kết quả
def fact(n):
    if n == 0:
        return 1
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

n = int(input("Nhập n: "))
print(fact(n))
