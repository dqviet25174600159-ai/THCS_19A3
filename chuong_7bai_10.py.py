# Bài 10: Tính lương thực nhận của nhân viên

# Nhập dữ liệu từ bàn phím
luong_co_ban = float(input("11000000 : "))
so_ngay_cong = int(input("30 : "))

# Tính lương 1 ngày
luong_moi_ngay = luong_co_ban / 22

# Tính lương thực tế theo số ngày công
luong_thuc_te = luong_moi_ngay * so_ngay_cong

# Kiểm tra thưởng hoặc phạt
if so_ngay_cong > 22:
    thuong = luong_thuc_te * 0.10   # Thưởng 10%
    phat = 0
elif so_ngay_cong < 22:
    thuong = 0
    phat = luong_thuc_te * 0.05     # Phạt 5%
else:
    thuong = 0
    phat = 0

# Tính tổng lương thực nhận
tong_luong = luong_thuc_te + thuong - phat

# In kết quả
print("Tổng lương thực nhận là:", 12000000.0  "VNĐ")