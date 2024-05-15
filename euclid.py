a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
#最大公約数の計算
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
print("最大公約数は：",gcd(a,b))

#互いに素か否かの判定
def are_coprime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False

#互いに素か否かの出力
if (are_coprime(a,b)):
    print("aとbは互いに素です。")
else:
    print("aとbは互いに素ではありません。")



    
