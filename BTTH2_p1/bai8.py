"""Viết chương trình tính diện tích tam giác đều theo định lý Heron. Yêu cầu nhập vào cạnh tam giác đều.
"""

import math

a = float(input("Nhập giá trị cạnh tam giác đều: "))

s = (a * a) * (math.sqrt(3) / 4)
print("Diện tích tam giác đều là: ", s)