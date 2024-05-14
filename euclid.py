a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
#最大公約数の計算
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
print("最大公約数は：", gcd(a, b))

#素数判定
def are_coprime(a, b):
    if gcd(a, b) == 1:
        return "aとbは互いに素です。"
    else:
        return "aとbは互いに素ではありません。"
print(are_coprime(a, b))
