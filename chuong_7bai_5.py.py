# Bài 5: Nhập số tiền gửi ban đầu và lãi suất hàng năm từ bàn phím.
# Tính số tiền lãi nhận được sau 1 tháng, 2 quý, 3 năm (lãi đơn).

# Nhập dữ liệu
tien_gui = float(input("10000000 VNĐ): "))
lai_suat_nam = float(input("6 (%): "))

# Chuyển lãi suất phần trăm sang dạng thập phân
lai_suat_nam = lai_suat_nam / 100

# Tính tiền lãi (theo công thức lãi đơn: I = P * r * t)
# t: thời gian tính theo năm

lai_1_thang = tien_gui * lai_suat_nam * (1/12)
lai_2_quy = tien_gui * lai_suat_nam * (6/12)   # 2 quý = 6 tháng
lai_3_nam = tien_gui * lai_suat_nam * 3

# In kết quả
print("Tiền lãi sau 1 tháng là:", round(lai_1_thang, 2), "VNĐ")
print("Tiền lãi sau 2 quý là:", round(lai_2_quy, 2), "VNĐ")
print("Tiền lãi sau 3 năm là:", round(lai_3_nam, 2), "VNĐ")