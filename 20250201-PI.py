#!/usr/bin/evn python3

#https://zenn.dev/kota_yata/articles/a0c9f55bf118dd7711cf

import random
import matplotlib.pyplot as plt

def GenerateRandom():
  x, y = random.random(), random.random()
  number = x ** 2 + y ** 2
  return [number, x, y]

iteration = 10000

for ite in range(iteration):
  check = GenerateRandom()
  if (check[0] < 1):
    plt.scatter(check[1], check[2], c = 'red', s = 10)
  else:
    plt.scatter(check[1], check[2], c='blue', s = 10)

plt.title('Monte Carlo Method')
plt.xlabel("x")
plt.ylabel("y")
plt.show()