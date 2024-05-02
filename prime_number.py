a = int(input("aの値を入力: "))

# TODO
def is_prime(a):
    if a <= 1:
        return False
    for x in range(2,a):
        if a%x == 0:
            return False
    return True
print(is_prime(a))
