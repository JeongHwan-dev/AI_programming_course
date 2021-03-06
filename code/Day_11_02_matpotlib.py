# Day_11_02_matpotlib.py
import matplotlib.pyplot as plt
import numpy as np

def plot_1():
    # plt.plot([1, 3, 5, 7])
    # plt.plot([1, 3, 5, 7], [1, 2, 3, 5])
    # plt.plot([1, 3, 5, 7], [1, 2, 3, 5], 'r')     # 꺽은선
    # plt.plot([1, 3, 5, 7], [1, 2, 3, 5], 'o')       # marker, 산점도
    plt.plot([1, 3, 5, 7], [1, 2, 3, 5], 'rx')
    plt.show()


# 문제
# 아래 수식을 그래프로 표현하세요.
# y = x ^ 2
def plot_2():
    # x = range(-5, 6)
    # y = [i*i for i in x]
    # plt.plot(x, y)

    x = np.arange(-5, 5, 0.1)
    plt.plot(x, x ** 2)
    plt.plot(x, x ** 2, 'x')
    plt.show()


# 문제
# 4개의 로그 그래프를 그리세요.
def plot_3():
    x = np.arange(0.1, 4, 0.1)

    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))

    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))
    plt.show()


# 문제
# 로그 그래프 4개를 4개의 칸으로 나워서 각 칸에 하나씩 그려보세요.
def plot_4():
    x = np.arange(0.1, 4, 0.1)

    plt.subplot(2, 2, 1)
    plt.plot(x, np.log(x))

    plt.subplot(2, 2, 2)
    plt.plot(x, -np.log(x))

    plt.subplot(2, 2, 3)
    plt.plot(-x, np.log(x))

    plt.subplot(2, 2, 4)
    plt.plot(-x, -np.log(x))

    plt.show()


def plot_5():
    x = np.arange(0.1, 4, 0.1)

    plt.figure(1)
    plt.plot(x, np.log(x), 'r')

    plt.figure(2)
    plt.plot(x, -np.log(x), 'g')

    plt.figure(2)
    plt.plot(-x, np.log(x), 'b')

    plt.figure(1)
    plt.plot(-x, -np.log(x), 'k')
    plt.show()


# plot_1()
# plot_2()
# plot_3()
# plot_4()
plot_5()
