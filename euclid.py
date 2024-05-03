a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
print(gcd(a,b))