
height = float(input("Nhập chiều cao thả vật (m): "))
g = 9.8  # gia tốc trọng trường (m/s^2)
v_i = 0  # tốc độ ban đầu (m/s)

v_f = (v_i ** 2 + 2 * g * height) ** 0.5
print("Tốc độ của vật khi chạm đất là:", v_f, "m/s")