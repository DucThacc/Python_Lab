"""File test để sử dụng các hàm từ tu_dien.py"""

from tu_dien import *

# Test với Max = 5
Max = 5
print(f"Tao tu dien voi Max = {Max}")

# Tạo từ điển
TD = Tao_TD(Max)

# Test các hàm
Print_Item(TD)
print()
Print_Key(TD)
print()
Print_Value(TD)
