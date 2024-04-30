a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
#問3
while b != 0:
    (a, b) = (b, a % b)
    gcd = a
print(a)
    
