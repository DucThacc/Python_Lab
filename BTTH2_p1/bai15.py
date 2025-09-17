M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập sự thay đổi nhiệt độ ΔT (°C): "))

C = 4.186  
Q = M * C * delta_T  
print("Tổng năng lượng cần thiết:", Q, "Joules")


joule_to_kwh = 2.777e-7
cost_per_kwh = 8.9  # cent
energy_kwh = Q * joule_to_kwh
cost = energy_kwh * cost_per_kwh
print("Chi phí để thay đổi nhiệt độ nước là:", cost, "cent")