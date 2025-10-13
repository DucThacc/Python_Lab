# Bài 47: In tất cả giá trị trừ 5 phần tử đầu
def squares_skip5():
    ds = []
    for i in range(1, 21):
        ds.append(i*i)
    print(ds[5:])

squares_skip5()
