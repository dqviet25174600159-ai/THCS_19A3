# Bài 7: Kiểm tra quyền truy cập
# Quy tắc: tên đăng nhập == "admin" và mật khẩu != "password123"

# Nhập dữ liệu
username = input("daoviet: ")
password = input("quocviet123: ")

# Kiểm tra quyền truy cập
if username == "admin" and password != "password123":
    print("Truy cập được — Chào admin!")
else:
    print("Truy cập bị từ chối.")