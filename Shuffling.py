# -*- coding: utf-8 -*-
import os
import random
from pprint import pprint
import Io

def random_partition(dir):
  files = [dir + f for f in os.listdir(dir)]
  random.shuffle(files)
  k = len(files) // 3
  partition = (files[:k], files[k:2*k], files[2*k:])
  return partition

# each time different partitions of same size
def test():
  test_root = "test_input/corpora/"
  for i in range(4):
    partition = random_partition(test_root)
    pprint (partition)

if __name__ == "__main__":
  test()