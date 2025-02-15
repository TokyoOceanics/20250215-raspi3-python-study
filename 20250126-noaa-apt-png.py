from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# PNG画像を読み込み
def load_png_image(filepath):
    img = Image.open(filepath)
    img_data = np.array(img)
    return img_data

# 画像の表示
def display_image(image_data, title='Image'):
    plt.imshow(image_data, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# 画像の処理（例：赤外線データの温度変換）
def infrared_to_temperature(image_data):
    # 仮の温度変換（輝度を0-255から-50～50°Cにマッピング）
    temp_min, temp_max = -50, 50
    data_normalized = image_data / 255.0  # 0?1に正規化
    temperature = temp_min + (temp_max - temp_min) * data_normalized
    return temperature

# メイン処理
filepath = './01190155.png'

# PNG画像を読み込み
image_data = load_png_image(filepath)

# 可視化（そのまま表示）
display_image(image_data, 'Original Image')

# 赤外線データを温度に変換（仮定の例）
temperature_map = infrared_to_temperature(image_data)

# 温度マップを表示
display_image(temperature_map, 'Temperature Map')

