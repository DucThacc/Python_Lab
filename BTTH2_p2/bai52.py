# Bài 52: Kiểm tra số hoàn hảo và liệt kê 1..10000
def is_perfect(n):
    if n < 2:
        return False
    s = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i += 1
    return s == n

x = int(input("Nhập số cần kiểm tra: "))
print("Hoàn hảo" if is_perfect(x) else "Không hoàn hảo")

print("Các số hoàn hảo từ 1..10000:")
for v in range(2, 10001):
    if is_perfect(v):
        print(v, end=" ")
print()
