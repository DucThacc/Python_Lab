
tien_an = float(input("Nhập chi phí bữa ăn (VNĐ): "))
tip = tien_an * 0.18
tax = tien_an * 0.05
total = tien_an + tip + tax
print("Tiền bữa ăn: ", tien_an ," VNĐ")
print(f"Tiền thuế: ", tax ," VNĐ")
print(f"Tiền boa: ", tip ," VNĐ")
print(f"Tổng cộng: ", total ," VNĐ")
