try:
    a = int(input("aの値を入力: "))
    if a <= 0:
        raise ValueError("自然数を入力してください。")
except ValueError as message:
    message = "自然数を入力してください。"
    print(message)
    exit()
else:
    # 自然数が入力された場合にのみ、is_prime 関数を実行
    def is_prime(a):
        if a == 1:
            return False
        for x in range(2, a):
            if a%x == 0:
                return False
        return True
    
    print(is_prime(a))
    