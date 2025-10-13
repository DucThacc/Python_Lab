"""Sử dụng cấu trúc từ điển, viết một chương trình nhập một câu, in số chữ cái và chữ số trong câu đó. 
Giả sử đầu vào chuỗi: hello world! 123
"""

chuoi = input("Nhập chuỗi: ")
d={"chu_cai":0 , "chu_so":0}
for ch in chuoi:
    if ch.isalpha():
        d["chu_cai"]+=1
    elif ch.isdigit():
        d["chu_so"]+=1
    else:
        pass
print("Số chữ cái:",d["chu_cai"])
print("Số chữ số:",d["chu_so"])