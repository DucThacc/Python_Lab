# Bài 46: In 5 phần tử cuối của list bình phương 1..20
def squares_last5():
    ds = []
    for i in range(1, 21):
        ds.append(i*i)
    print(ds[-5:])

squares_last5()
