import time

while True:
    print("\n===== MENU =====")
    print("1. Kiểm tra số chẵn/lẻ")
    print("2. Kiểm tra 3 cạnh tam giác")
    print("3. Tính tuổi từ năm sinh")
    print("0. Thoát")

    chon = input("Chọn bài (0-3): ")

    if chon == "1":
        n = int(input("Nhập số nguyên dương: "))
        if n % 2 == 0:
            print("Đây là một số chẵn")
        else:
            print("Đây là một số lẻ")

    elif chon == "2":
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        c = int(input("Nhập c: "))

        if a + b > c and a + c > b and b + c > a:
            print("Độ dài ba cạnh tam giác")
        else:
            print("Đây không phải độ dài ba cạnh tam giác")

    elif chon == "3":
        nam_sinh = int(input("Nhập năm sinh: "))
        nam_hien_tai = time.localtime().tm_year
        tuoi = nam_hien_tai - nam_sinh

        print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi")

    elif chon == "0":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
import time
import math

while True:
    print("\n===== MENU =====")
    print("1. Kiểm tra số chẵn/lẻ")
    print("2. Kiểm tra 3 cạnh tam giác")
    print("3. Tính tuổi từ năm sinh")
    print("4. Kiểm tra chia hết cho 2 và 3")
    print("5. Giải phương trình bậc 2")
    print("0. Thoát")

    chon = input("Chọn bài (0-5): ")

    if chon == "1":
        n = int(input("Nhập số nguyên dương: "))
        if n % 2 == 0:
            print("Đây là một số chẵn")
        else:
            print("Đây là một số lẻ")

    elif chon == "2":
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        c = int(input("Nhập c: "))

        if a + b > c and a + c > b and b + c > a:
            print("Độ dài ba cạnh tam giác")
        else:
            print("Đây không phải độ dài ba cạnh tam giác")

    elif chon == "3":
        nam_sinh = int(input("Nhập năm sinh: "))
        nam_hien_tai = time.localtime().tm_year
        tuoi = nam_hien_tai - nam_sinh

        print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi")

    elif chon == "4":
        # Bài 4
        n = int(input("Nhập số nguyên dương: "))
        if n % 2 == 0 and n % 3 == 0:
            print("Số chia hết cho cả 2 và 3")
        elif n % 2 == 0:
            print("Số chia hết cho 2")
        elif n % 3 == 0:
            print("Số chia hết cho 3")
        else:
            print("Không chia hết cho 2 và 3")

    elif chon == "5":
        # Bài 5
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: "))

        if a == 0:
            if b == 0:
                if c == 0:
                    print("Phương trình vô số nghiệm")
                else:
                    print("Phương trình vô nghiệm")
            else:
                x = -c / b
                print("Phương trình bậc nhất, nghiệm x =", x)
        else:
            delta = b**2 - 4*a*c

            if delta > 0:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                print("2 nghiệm phân biệt:")
                print("x1 =", x1)
                print("x2 =", x2)
            elif delta == 0:
                x = -b / (2*a)
                print("Nghiệm kép x =", x)
            else:
                print("Phương trình vô nghiệm")

    elif chon == "0":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại!")
# Bài 1
print("=== Bài 1 ===")
n = int(input("Nhập số nguyên n: "))
for i in range(1, n):
    print(2 * i)

# Bài 2
print("\n=== Bài 2 ===")
n = int(input("Nhập số nguyên n: "))
if n > 10:
    print("Số nhập vào phải bé hơn 10")
else:
    print("Các số chẵn từ 1 đến", n, ":")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

# Bài 3
print("\n=== Bài 3 ===")
for i in range(80, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

# Bài 4
print("\n=== Bài 4 ===")
n = int(input("Nhập số nguyên n < 20: "))
for i in range(1, n):
    if i % 5 == 0 or i % 7 == 0:
        print(i)
