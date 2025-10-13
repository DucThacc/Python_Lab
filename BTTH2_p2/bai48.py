# Bài 48: Hàm trả về trung bình của 3 tham số
def avg3(a, b, c):
    return (a+b+c)/3

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("Trung bình =", avg3(a,b,c))
