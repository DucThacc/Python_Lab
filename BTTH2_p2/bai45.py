# Bài 45: Tạo list bình phương 1..20 và in 5 phần tử đầu
def squares_first5():
    ds = []
    for i in range(1, 21):
        ds.append(i*i)
    print(ds[:5])

squares_first5()
