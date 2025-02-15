#!/usr/bin/env python3
#
#
#良い例
#
#for i in range(0,10,1):
#    print(i)
    
#for i in (1,2,3,4,5,6,7,8):
#    print(i)
#
#ダメな例 
#for double_value in range (-10.0, +10.0, 3.14):
#    print(double_value)

#for文で浮動小数点値を扱う代替例
#https://atmarkit.itmedia.co.jp/ait/articles/2205/31/news032.html
# range関数で得た値に係数をかける
for num in [num * 0.1 for num in range(0, 4)]:
    print(num)
print()
   
## 浮動小数点の誤差をround関数で丸める
for num in [round(num * 0.1, 1) for num in range(0, 4)]:
    print(num)
print()
# 出力結果：※見た目は丸められているが、浮動小数点数値なので誤差は含まれている
 
#
# 開始値、終了値、ステップ値に浮動小数点数値を受け取る関数の定義
def frange(start, end , step):
    if step == 0:
        raise ValueError('step must not be zero')

    start = float(start)
    end = float(end)
    step = float(step)

    # range関数と同様な振る舞いにする
    if abs(step) > abs(start - end):
        return [start]
    if step > 0 and end - start < 0:
        return []
    elif step < 0 and end - start > 0:
        return []

    exp = len(str(step).split('.')[1])  # 丸める際に使用する桁数
    result = [start]
    val = start
    if step > 0:
        while (val := round(val + step, exp)) < end:
            result.append(val)
    else:
        while (val := round(val + step, exp)) > end:
            result.append(val)
    return result

for num in frange(0.0, 0.5, 0.1):
    print(num)
print()


# 
# range関数を使うバージョン
def frange2(start, end, step):
    if step == 0:
        raise ValueError('step must not be zero')

    start = float(start)
    end = float(end)
    step = float(step)
    if abs(step) >= abs(start - end):
        return [start]

    exp = len(str(step).split('.')[1])  # ステップ値から整数化に使用する値を得る
    start = int(start * 10 ** exp)
    end = int(end * 10 ** exp)
    step = int(step * 10 ** exp)

    result = [round(val * 10 ** -exp, exp) for val in range(start, end, step)]
    return result

for num in frange2(0.0, 0.5, 0.1):
    print(num)
print()
print(frange(0.0,0.5,0.1))
print(frange2(0.0,0.5,0.1))

print()

import numpy as np

for num in np.arange(0.0, 0.5, 0.1):
    print(num)
# 出力結果
#0.0
#0.1
#0.2
#0.30000000000000004
#0.4

for num in np.linspace(0.0, 0.5, 5):  # 0.0～1.0の範囲を5要素で等分割する
    print(num)
# 出力結果：
#0.0
#0.125
#0.25
#0.375
#0.5

for num in np.linspace(0.0, 0.5, 6):  # 0.0～0.5の範囲を6要素で等分割する
    print(num)
# 出力結果：
#0.0
#0.1
#0.2
#0.30000000000000004
#0.4
#0.5

for num in np.linspace(0.0, 0.5, 5, endpoint=False):  # 終了値を含まない
    print(num)
# 出力結果：
#0.0
#0.1
#0.2
#0.30000000000000004
#0.4
