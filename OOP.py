class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc=[]):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = khoaHoc

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        print("Danh sách khóa học đã đăng ký của", self.tenHV)
        for khoaHoc in self.khoaHoc:
            print(khoaHoc.thongTinKhoaHoc())

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Mã khóa học: {self.maKhoaHoc}, Tên khóa học: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi}"

# Tạo các đối tượng học viên và khóa học
hv1 = HocVien("HV001", "Nguyễn Văn A", "01/01/2000")
hv2 = HocVien("HV002", "Trần Thị B", "02/02/2000")

kh1 = KhoaHoc("KH001", "Lập trình Python cơ bản", "Online", 2000000)
kh2 = KhoaHoc("KH002", "Lập trình Web", "Offline", 3000000)

# Đăng ký khóa học
hv1.dangKyKhoaHoc(kh1)
hv1.dangKyKhoaHoc(kh2)
hv2.dangKyKhoaHoc(kh2)

# Hiển thị thông tin khóa học đã đăng ký của học viên
hv1.hienThiKhoaHoc()
hv2.hienThiKhoaHoc()