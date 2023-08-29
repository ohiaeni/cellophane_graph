# 座標系としては一枚目のセロハンの長手方向を基準とする

# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
import time
import japanize_matplotlib

# 計算のステップ間隔
step = 5

# 光路差
d = 216.15

cellophane_num1 = 1
cellophane_num2 = 1

# それぞれの座標における強度を格納する配列
arr = np.zeros((int(180/step)+1, int(180/step)+1))


def r_theta(theta):  # 回転行列R(θ）
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def mai_r_theta(theta):  # 回転行列R(-θ）
    return np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])


def jhons(theta):  # ジョーンズベクトル
    return np.array([[np.sin(theta)**2, -np.sin(theta)*np.cos(theta)], [-np.sin(theta)*np.cos(theta), np.cos(theta)**2]])


def main():  # メインの関数
    start_time = time.time()
    for y in range(0, 181, step):
        for x in range(0, 181, step):
            I = 0
            # 偏光板一枚目の回転角
            a = np.deg2rad(-x)
            E_1 = np.array([[-np.sin(a)], [np.cos(a)]])
            # セロハン二枚目の回転角
            b = np.deg2rad(y-x)
            # 偏光板二枚目の回転角
            c = np.deg2rad(-x-90)
            for i in range(380, 700+1):
                # 波長
                l = i
                # 位相差
                delta = cellophane_num1*2*d*np.pi/l
                # セロハンの項
                cello = np.array([[1, 0], [0, np.exp(-1j*delta)]])
                # E_2への変換
                E_2 = np.dot(cello, E_1)
                # 位相差
                delta = cellophane_num2*2*d*np.pi/l
                # セロハンの項
                cello = np.array([[1, 0], [0, np.exp(-1j*delta)]])
                # E_3への変換
                E_3 = np.dot(r_theta(b), np.dot(
                    cello, np.dot(mai_r_theta(b), E_2)))
                # E_4への変換
                E_4 = np.dot(jhons(c), E_3)
                I += np.abs(np.abs(E_4[0]**2) + np.abs(E_4[1]**2))
            print("2枚目の角度:"+str(x), "1枚目の角度:"+str(y))
            arr[int(y/step)][int(x/step)] = I[0]

    # メッシュグリッドを生成する
    X, Y = np.meshgrid(int(181/step)+1, int(181/step)+1)

    # サブプロットを生成する
    fig, ax = plt.subplots()

    # アクセズにグラフを入力する
    im = ax.imshow(arr, origin='lower', extent=(
        0, 180, 0, 180), vmin=0, vmax=400)

    # カラーバーを付加する
    plt.colorbar(im)

    # グラフを表示する
    plt.show()

    end_time = time.time()
    print("実行時間:"+str(end_time-start_time)+"秒")


if __name__:
    main()
