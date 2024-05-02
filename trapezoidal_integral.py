from math import sqrt, exp, sin, pi
# --example--
# print(sin(0))
# >>> 0
# -----------

def trapezoidal_integral(f, a=0, b=1, n=100):
    """
    台形積分を行う関数
    
    :param f: 積分する関数
    :param a: 区間の下限
    :param b: 区間の上限
    :param n: 区間の分割数
    :return: 台形積分による積分値
    """
    # 分割幅
    delta_x = (b - a) / n

    # 台形積分の計算
    integral = 0.5 * (f(a) + f(b))  # 区間端点の値を初期化

    for i in range(1, n):
        x = a + i * delta_x
        integral += f(x)

    integral *= delta_x
    return integral
if __name__ == "__main__":
    # (1) 関数 sin⁡x を区間 [0,π/2] で台形積分 (n=50)
    integral_1 = trapezoidal_integral(sin, a=0, b=pi/2, n=50)
    print(f"(1) 関数 sin⁡x を区間 [0,π/2] で台形積分 (n=50): {integral_1}")

    # (2) 関数 4/(1+x^2) を区間 [0,1] で台形積分 (n=100)
    def f2(x):
        return 4 / (1 + x**2)
    
    integral_2 = trapezoidal_integral(f2, a=0, b=1, n=100)
    print(f"(2) 関数 4/(1+x^2) を区間 [0,1] で台形積分 (n=100): {integral_2}")

    # (3) 関数 √(π)exp⁡(−x^2) を区間 [−100,100] で台形積分 (n=1000)
    def f3(x):
        return sqrt(pi) * exp(-x**2)
    
    integral_3 = trapezoidal_integral(f3, a=-100, b=100, n=1000)
    print(f"(3) 関数 √(π)exp⁡(−x^2) を区間 [−100,100] で台形積分 (n=1000): {integral_3}")