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
