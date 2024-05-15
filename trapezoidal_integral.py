#関数作成
def trapezoidal_integral(f, a=0, b=1, n=100):
    """
    与えられた分割数 n の下で、関数 f を区間 [a, b] で台形積分する

    :param f: 積分対象の関数
    :param a: 区間の下限
    :param b: 区間の上限
    :param n: 区間の分割数
    :return: 積分値（float 型）
    """
    # 分割幅
    delta_x = (b - a) / n

    # 台形積分の計算
    integral = 0.5 * delta_x * (f(a) + f(b))

    for i in range(1, n):
        integral += delta_x * f(a + i * delta_x)

    return integral

#実行
from math import sin, pi, sqrt, exp

# (1) 関数 sin⁡x を区間 [0,π/2] で台形積分してください。ただし、分割数は n=50 です。
integral_1 = trapezoidal_integral(sin, 0, pi / 2, 50)
print("(1) 関数 sin(x) の区間 [0, π/2] での台形積分:", integral_1)

# (2) 関数 4/(1+x^2) を 区間 [0,1] で台形積分してください。ただし、分割数は n=100 です。
def f2(x):
    return 4 / (1 + x ** 2)

integral_2 = trapezoidal_integral(f2, 0, 1, 100)
print("(2) 関数 4/(1+x^2) の区間 [0, 1] での台形積分:", integral_2)

# (3) 関数 √(π)exp⁡(−x^2) を 区間 [−100,100] で台形積分してください。ただし、分割数は n=1000 です。
def f3(x):
    return sqrt(pi) * exp(-x ** 2)

integral_3 = trapezoidal_integral(f3, -100, 100, 1000)
print("(3) 関数 sqrt(π)*exp(−x^2) の区間 [−100,100] での台形積分:", integral_3)


