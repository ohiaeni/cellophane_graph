# ライブラリのインポート
from PIL import Image
import os
# 画像を入れる箱を準備
pictures = []

DIR = 'fig'
file_count = sum(os.path.isfile(os.path.join(DIR, name))
                 for name in os.listdir(DIR))

# 画像を箱に入れていく
for i in range(file_count):
    pic_name = 'fig/'+str(i*5) + '.png'
    img = Image.open(pic_name)
    pictures.append(img)
# gifアニメを出力する
pictures[0].save('anime.gif', save_all=True, append_images=pictures[1:],
                 optimize=True, duration=100, loop=0)
