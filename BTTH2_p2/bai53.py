# Bài 53: Trả về mọi danh sách con (subsets) của danh sách
def all_subsets(arr):
    res = [[]]
    for x in arr:
        new_sets = []
        for cur in res:
            new_sets.append(cur + [x])
        res += new_sets
    return res

s = input("Nhập danh sách số (phân tách bởi dấu phẩy): ")
arr = [x.strip() for x in s.split(",") if x.strip() != ""]
subs = all_subsets(arr)
print(subs)
