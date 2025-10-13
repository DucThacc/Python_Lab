
chuoi = input("Nhập chuỗi: ")
d = {"chu_thuong": 0, "chu_hoa": 0}
for ch in chuoi:
    if ch.isupper() == True:
        d["chu_hoa"] += 1
    elif ch.islower() == True:
        d["chu_thuong"] += 1
    else:
        pass
print("Số chữ cái thường:", d["chu_thuong"])
print("Số chữ cái hoa:", d["chu_hoa"])    