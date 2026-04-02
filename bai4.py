import math

# 1. Hàm tính tổng 2 số truyền vào
def tong_2_so(a, b):
    return a + b


# 2. Hàm tính tổng các số truyền vào
def tong_nhieu_so(*args):
    return sum(args)


# 3. Hàm kiểm tra một số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 4. Chương trình tìm các số nguyên tố trong khoảng [a, b]
def tim_so_nguyen_to_trong_khoang(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            ds.append(i)
    return ds


# 5. Hàm kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False

    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i

    return tong_uoc == n


# 6. Chương trình tìm các số hoàn hảo trong khoảng [a, b]
def tim_so_hoan_hao_trong_khoang(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            ds.append(i)
    return ds


# 7. Menu chọn thực thi các hàm trên
def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng nhiều số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm các số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm các số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát")
        print("==========================")

        chon = input("Nhập lựa chọn của bạn: ")

        if chon == "1":
            a = int(input("Nhập số a: "))
            b = int(input("Nhập số b: "))
            print("Tổng 2 số là:", tong_2_so(a, b))

        elif chon == "2":
            n = int(input("Nhập số lượng số muốn cộng: "))
            ds = []
            for i in range(n):
                x = float(input(f"Nhập số thứ {i + 1}: "))
                ds.append(x)
            print("Tổng các số là:", tong_nhieu_so(*ds))

        elif chon == "3":
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_nguyen_to(n):
                print(n, "là số nguyên tố")
            else:
                print(n, "không phải là số nguyên tố")

        elif chon == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ds = tim_so_nguyen_to_trong_khoang(a, b)
            print("Các số nguyên tố trong khoảng [{}, {}] là:".format(a, b))
            print(ds)

        elif chon == "5":
            n = int(input("Nhập số cần kiểm tra: "))
            if la_so_hoan_hao(n):
                print(n, "là số hoàn hảo")
            else:
                print(n, "không phải là số hoàn hảo")

        elif chon == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ds = tim_so_hoan_hao_trong_khoang(a, b)
            print("Các số hoàn hảo trong khoảng [{}, {}] là:".format(a, b))
            print(ds)

        elif chon == "0":
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


# Chạy chương trình
menu()
