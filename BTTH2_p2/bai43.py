# Bài 43: Hàm in chuỗi dài hơn (hoặc cả hai nếu bằng nhau)
def longer(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

a = input("Chuỗi 1: ")
b = input("Chuỗi 2: ")
longer(a, b)
