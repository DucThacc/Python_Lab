"""Bài 9: Chạy chương trình Bài 7, nhập giá trị cho trường hợp tam giác đều (lưu ý: giá trị cạnh tam giác = giá trị cạnh tam giác Bài 8). Đánh giá kết quả khi chạy chương trình Bài 7 và Bài 8
"""

import math

a = float(input("Nhập giá trị cạnh a: "))
b = float(input("Nhập giá trị cạnh b: "))
c = float(input("Nhập giá trị cạnh c: "))
A = math.radians(float(input("Nhập giá trị góc A (radian): ")))
B = math.radians(float(input("Nhập giá trị góc B (radian): ")))
C = math.radians(float(input("Nhập giá trị góc C (radian): ")))

if a + b > c and b + c > a and c + a > b:
    area = 0.5 * a * b * math.sin(C)
    print("Diện tích tam giác là: ", area)
else:
    print("Không phải là tam giác hợp lệ.")