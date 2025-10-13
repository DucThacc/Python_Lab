# Bài 36: Nhập số (kết thúc bằng 0), in theo thứ tự tăng dần (bỏ 0)
nums = []
print("Nhập số, nhập 0 để dừng:")
while True:
    x = int(input())
    if x == 0:
        break
    nums.append(x)
nums.sort()
for v in nums:
    print(v)
