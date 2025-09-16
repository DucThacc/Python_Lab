import math

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

print(f"Tổng của a và b: {a + b}")
print(f"Hiệu của a và b: {a - b}")
print(f"Tích của a và b: {a * b}")

if b != 0:
    print(f"Thương của a chia cho b: {a / b}")
    print(f"Phần còn lại khi a chia cho b: {a % b}")
else:
    print("Không thể chia cho 0.")

if a > 0:
    print("Kết quả của log_10 a: ""math.log10(a)}")
else:
    print("Không thể tính log_10 với a <= 0.")

print(f"Kết quả của a^b: {a ** b}")