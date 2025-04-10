# -*- coding: utf-8 -*-
"""HW2_hash_practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1myu-WTPJc5iP248SWRWVWO35n5JC4M2A
"""

# Commented out IPython magic to ensure Python compatibility.
#載入存放檔案資料夾(雲端硬碟)和檔案
from google.colab import drive
drive.mount('/content/drive') #掛載在這個目錄下
# %cd /content/drive/MyDrive/Colab Notebooks/

import matplotlib.pyplot as plt

# 建立一個空的 hash/dictionary 來儲存字詞次數
word_count = {}

# 讀取資料檔案
with open('hw2_data.txt', 'r') as file:
    for line in file:
        word = line.strip()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 1. 不重複的英文字數量
print("不重複英文字的總數：", len(word_count))

# 2. 每個英文字出現次數
print("\n每個英文字出現次數：")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 3. 畫出直方圖（依照數量多寡排序）
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
labels, values = zip(*sorted_words)

plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.xticks(rotation=45)
plt.title("英文字出現頻率統計圖")
plt.xlabel("英文字")
plt.ylabel("出現次數")
plt.tight_layout()
plt.show()

