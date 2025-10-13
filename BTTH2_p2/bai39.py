# Bài 39: Tạo dict (i, i*i) 1..n
n = int(input("Nhập n: "))
d = {i: i*i for i in range(1, n+1)}
print(d)
