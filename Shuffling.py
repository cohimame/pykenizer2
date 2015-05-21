# -*- coding: utf-8 -*-
import os
import random
from pprint import pprint
import Io

"""
  Предположение: имя автора и число написанных им поэм
  не берется в расчет.
"""
def random_partition(source,number,size):
  ps = poets(source)
  rand_ps = random_poets(ps,size*number)

  print("got random poets")

  #range(a,b,i) не включает b
  result = [
    rand_ps[k:k+size] for k in range(0, size*(number-1), size)
    ] + [ rand_ps[size*(number-1):] ]

  return result
    
def random_poets(poets, n):
  result = set()
  while len(result) != n:
    rnd_poet = random.choice(poets)
    result.add(rnd_poet)   
  return list(result)
  
def poets(root):
  poets = [
  os.path.join(path, name)
    for path, subdirs, files in os.walk(root)
      for name in files]
  return poets 


# each time different partitions of same size
def test():
  test_root = "test_input\\tree\\"
  number = 4
  size = 3
  for i in range(4):
    partition = random_partition(test_root,number,size)
    pprint (partition)
    print()

if __name__ == "__main__":
  test()
  
