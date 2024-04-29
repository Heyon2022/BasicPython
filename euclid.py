a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
#問3
while b != 0:
    gcd = b
    (a, b) = (b, a % b)
    print(gcd)
    
