import math

def sin_approx(x, n):
    if n<0:
        print("  Gia tri n khong phu hop")
        return None
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result

def cos_approx(x, n):
    if n<0:
        print("  Gia tri n khong phu hop")
        return None
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        result += term
    return result

def sinh_approx(x, n):
    if n<0:
        print("  Gia tri n khong phu hop")
        return None
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result

def cosh_approx(x, n):
    if n<0:
        print("  Gia tri n khong phu hop")
        return None
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / math.factorial(2 * i)
        result += term
    return result

# Ví dụ sử dụng
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lần lặp n: "))

print(f"sin({x}) ≈ {sin_approx(x, n)}")
print(f"cos({x}) ≈ {cos_approx(x, n)}")
print(f"sinh({x}) ≈ {sinh_approx(x, n)}")
print(f"cosh({x}) ≈ {cosh_approx(x, n)}")

