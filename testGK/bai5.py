Diem_Nguon_DS=[]

print("Nhap diem nguon hoặc no de ket thuc: ")
while True:
    user_input = input()
    if user_input.lower() == "no":
        break
    try:
        score = float(user_input)
        if 0<= score <= 10:
            Diem_Nguon_DS.append(score)
        else:
            print("Diem khong hop le")
    except:
        print("Diem khong hop le")

Dau_DS = [diem for diem in Diem_Nguon_DS if diem >= 5]

print("Danh sách điểm đậu (>= 5.0):", Dau_DS)

    