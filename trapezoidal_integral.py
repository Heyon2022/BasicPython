
# --example--
# print(sin(0))
# >>> 0
# -----------
#問2
from math import sin
from math import pi
# 区間の上限と下限
a = 0
b = pi / 2  # π/2

# 分割数
n = 100

# 分割幅
delta_x = (b - a) / n

# 台形積分の計算
integral = 0.5 * delta_x * (sin(a) + sin(b))

for i in range(1, n):
    integral += delta_x * sin(a + i * delta_x)

print("積分値の近似値:", integral)

