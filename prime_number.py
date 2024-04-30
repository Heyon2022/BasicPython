a = int(input("aの値を入力: "))

# TODO
#問1
if a <=1:
    print(False)
else:
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            print(False)
            break
    else:
      print(True)

