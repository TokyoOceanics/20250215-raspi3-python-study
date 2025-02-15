#!/usr/bin/evn python3

#from chat GPT
#2025/01/26


import numpy as np
import matplotlib.pyplot as plt
import cv2

# RAWデータの読み込み
def load_raw_data(filepath):
    # RAWデータを読み込む
    with open(filepath, 'rb') as f:
        raw_data = np.frombuffer(f.read(), dtype=np.uint8)
    return raw_data

# 同期信号の検出
def detect_sync_signals(data, sync_pattern):
    sync_positions = []
    for i in range(len(data) - len(sync_pattern)):
        if np.array_equal(data[i:i + len(sync_pattern)], sync_pattern):
            sync_positions.append(i)
    return sync_positions

# データを画像に変換
def raw_to_image(data, sync_positions, line_length):
    images = []
    for i in range(len(sync_positions) - 1):
        start = sync_positions[i] + len(sync_pattern)
        end = sync_positions[i + 1]
        line_data = data[start:end]
        if len(line_data) == line_length:
            images.append(line_data)
    return np.array(images)

# 赤外線データから温度マップを作成
def infrared_to_temperature(data):
    # 輝度値を温度に変換（仮定: 線形変換）
    temp_min, temp_max = -50, 50  # 温度範囲（例）
    data_normalized = data / 255.0  # 輝度値を0～1に正規化
    temperature = temp_min + (temp_max - temp_min) * data_normalized
    return temperature

# メイン処理
filepath = 'path_to_your_raw_file.raw'
sync_pattern = np.array([0x55, 0x55, 0x55, 0x30], dtype=np.uint8)  # 仮の同期パターン
line_length = 2080  # 1行のデータ長（仮）

# RAWデータを読み込み
raw_data = load_raw_data(filepath)

# 同期信号を検出
sync_positions = detect_sync_signals(raw_data, sync_pattern)

# 画像データに変換
image_data = raw_to_image(raw_data, sync_positions, line_length)

# 赤外線データを温度に変換
temperature_map = infrared_to_temperature(image_data[:, 1040:])  # 2つ目のチャンネルを使用

# 可視光データの表示
plt.imshow(image_data[:, :1040], cmap='gray')
plt.title('Visible Light Image')
plt.show()

# 温度マップの表示
plt.imshow(temperature_map, cmap='hot')
plt.colorbar(label='Temperature (°C)')
plt.title('Infrared Temperature Map')
plt.show()

