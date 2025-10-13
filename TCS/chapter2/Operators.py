"""Biểu thức toán tử

• Arithmetic Operators (Toán tử số học): 
    +, -, *, /, % (chia lấy dư), ** (luỹ thừa, mũ), // (chia lấy phần nguyên)
• Comparison Operators(Toán tử so sánh):
    ==, !=, >=, <=, >, <
• Logical Operators(Toán tử so sánh): 
    and (Và, chi đúng khi cả hai đúng) Ví dụ True and False = False
    or (Hoặc, chỉ sai khi cả hai sai) Ví dụ True or False = True
    not (Phủ định, đảo ngược giá trị) Ví dụ not True = False
• Identity Operators(Toán tử đồng nhất – so sánh vị trí trong bộ nhớ): 
    is (Đúng nếu 2 biến trỏ cùng 1 đối tượng) Ví dụ a is b = True nếu a và b trỏ cùng 1 đối tượng
    is not (Đúng nếu 2 biến trỏ khác đối tượng) Ví dụ a is not b = True nếu a và b trỏ khác đối tượng
    Lưu ý: is không giống ==. == so sánh giá trị, is so sánh địa chỉ bộ nhớ.
• Membership Operators(Toán tử thành viên – kiểm tra phần tử trong chuỗi, danh sách, v.v.): 
    in (Đúng nếu phần tử nằm trong tập) Ví dụ  5 in [1,2,3,4,5] = True, 'a' in 'apple' = True
    not in (Đúng nếu phần tử không nằm trong tập) Ví dụ 5 not in [1,2,3,4,5] = False, 'a' not in 'apple' = False
• Bitwise Operators(Toán tử bit – thao tác ở mức bit nhị phân): 
    & AND (và từng bit) Ví dụ (a = 5, b = 3) a & b = 1 (0101 & 0011 = 0001)
    | OR (hoặc từng bit) Ví dụ (a = 5, b = 3) a | b = 7 (0101 | 0011 = 0111)
    ^ XOR (hoặc loại trừ từng bit) Ví dụ (a = 5, b = 3) a ^ b = 6 (0101 ^ 0011 = 0110)
    ~ NOT (phủ định từng bit) Ví dụ (a = 5) ~a = -6 (~0101 = 1010)
    >>  Dịch phải từng bit Ví dụ (a = 5) a >> 1 = 2 (0101 >> 1 = 0010)
    <<  Dịch trái từng bit Ví dụ (a = 5) a << 1 = 10 (0101 << 1 = 1010)
• Assignment Operators (Toán tử gán) : 
    = gán giá trị cho biến x = 5 
    += gán cộng x += 3 (tương đương x = x + 3)
    -= gán tru x -= 3 (tương đương x = x - 3)
    *= gán nhân x *= 3 (tương đương x = x * 3)
    /= gán chia x /= 3 (tương đương x = x / 3)
    %= gán chia lấy dư x %= 3 (tương đương x = x % 3)
    **= gán luỹ thừa x **= 3 (tương đương x = x ** 3)
    //= gán chia lấy phần nguyên x //= 3 (tương đương x = x // 3)
    &= gán and x &= 3 (tương đương x = x & 3)
    >>= gán dịch phải x >>= 3 (tương đương x = x >> 3)
    <<= gán dịch trái x <<= 3 (tương đương x = x << 3)
    |= gán or x |= 3 (tương đương x = x | 3)
    ^= gán xor x ^= 3 (tương đương x = x ^ 3)
"""