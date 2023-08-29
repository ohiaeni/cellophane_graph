# 座標系としては一枚目のセロハンの長手方向を基準とする

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
import time
import japanize_matplotlib

# 光路差
d = 216.15

# それぞれの角度における強度を格納する配列
arr = np.zeros(181)
x = np.arange(181)


def jhons(theta):  # ジョーンズベクトル
    return np.array([[np.sin(theta)**2, -np.sin(theta)*np.cos(theta)], [-np.sin(theta)*np.cos(theta), np.cos(theta)**2]])


def main():  # メインの関数
    start_time = time.time()
    for rad in range(0, 181):
        # 強度
        I = 0
        # 入射前
        E_1 = np.array([[-np.sin(0)], [np.cos(0)]])
        # 偏光板二枚目の回転角
        a = np.deg2rad(-rad)

        for _ in range(380, 700+1):
            # E_2への変換
            E_2 = np.dot(jhons(a), E_1)
            I += np.abs(np.abs(E_2[0]**2) + np.abs(E_2[1]**2))
        arr[rad] = I
    plt.plot(x, arr, linestyle='solid')
    plt.xlim(0, 180)
    plt.ylim(0, 350)
    plt.xlabel("1枚目の偏光板に対する2枚目の偏光板の角度[°]")
    plt.ylabel("強度[a.u.]")
    plt.title("偏光板と強度の関係")
    plt.savefig("img.png")
    # グラフを表示する
    plt.show()

    end_time = time.time()
    print("実行時間:"+str(end_time-start_time)+"秒")


if __name__:
    main()
