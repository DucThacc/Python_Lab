"""Bài 5: Viết một chương trình nhập vào 1 chuỗi. Sau đó, xuất ra màn hình: 
5 ký tự cuối cùng; 5 ký tự đầu tiên. 
4 chuỗi trên một dòng cách 1 khoảng trắng.
4 chuỗi trên 4 dòng.
"""

st = input(" Enter your string: ")
First_five_characters = st[:5]
Last_five_characters = st[len(st)-5:]
four_Str_1_line = 4 * (st + " ")
four_Str_4_line = 4 * (st + "\n")

print("First five characters are: " + First_five_characters)
print("Last five characters are: " + Last_five_characters)
print("Four strings of one line are: " + four_Str_1_line)
print("Four strings of four line are: \n" + four_Str_4_line)