"""Viết chương trình tính diện tích tam giác theo công thức. Yêu cầu nhập vào 3 cạnh và các góc A,B và C (radian)
"""

import math

a = float(input("Nhập giá trị cạnh a: "))
b = float(input("Nhập giá trị cạnh b: "))
c = float(input("Nhập giá trị cạnh c: "))
A = math.radians(float(input("Nhập giá trị góc A (radian): ")))
B = math.radians(float(input("Nhập giá trị góc B (radian): ")))
C = math.radians(float(input("Nhập giá trị góc C (radian): ")))


area = 0.5 * a * b * math.sin(C)
print("Diện tích tam giác là: ", area)
