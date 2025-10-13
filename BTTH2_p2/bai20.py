"""Viết một chương trình tính và in kết quả giai thừa của một số nhập vào từ bàn phím. """

def giaithua(x):
    if x == 0:
        return 1
    return x * giaithua(x - 1)

x = int(input("Nhập số cần tính giai thừa: "))
print("Giai thừa của", x, "là:", giaithua(x))
