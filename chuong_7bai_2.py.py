# Bài 2: Nhập tổng số kẹo và số học sinh từ bàn phím.
# Tính số kẹo mỗi học sinh nhận được và số kẹo còn thừa (biết số kẹo chia đều).

# Nhập dữ liệu từ bàn phím
tong_so_keo = int(input("6: "))
so_hoc_sinh = int(input("6: "))

# Tính số kẹo mỗi học sinh nhận được (chia đều)
keo_moi_hoc_sinh = tong_so_keo // so_hoc_sinh  # phép chia lấy phần nguyên
keo_con_thua = tong_so_keo % so_hoc_sinh       # phép chia lấy phần dư

# In kết quả ra màn hình
print("Mỗi học sinh nhận được:", keo_moi_hoc_sinh, "kẹo")
print("Số kẹo còn thừa là:", keo_con_thua)
