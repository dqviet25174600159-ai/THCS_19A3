# Bài 1: Nhập giá sản phẩm và số lượng mua từ bàn phím.
# Tính tổng chi phí và thuế VAT (10%). In tổng tiền phải trả, làm tròn đến 2 chữ số thập phân.

# Nhập dữ liệu từ bàn phím
gia_san_pham = float(input("500000: "))
so_luong = int(input("5: "))

# Tính tổng chi phí
tong_chi_phi = gia_san_pham * so_luong

# Tính thuế VAT 10%
thue_vat = tong_chi_phi * 0.10

# Tính tổng tiền phải trả
tong_tien_phai_tra = tong_chi_phi + thue_vat

# In kết quả theo dạng tiền tệ, làm tròn 2 chữ số thập phân
print("Tổng tiền phải trả (đã bao gồm VAT): {:,.2f} VNĐ".format(tong_tien_phai_tra))