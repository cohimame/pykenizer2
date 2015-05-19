# -*- coding: utf-8 -*-

import Shuffling
import Hypothesis


ROOT = "E:/topic_modeling/may_hypothesis_dataset/input/"
OUTPUT = "output/"


"""
  Разбиваем все файлы в папке root
  на три случайных непересекающихся списка  
"""
random_datasets = Shuffling.random_partition(root)

"""
  Формируем названия файлов на которых 
  будет происходить проверка гипотез.
"""
batches = form_batches(random_datasets,output)

"""
  вход: batch1 - список пар (имя_i, список файлов_i) 
  выход: по файлу "имя_i" на каждый кортеж в списке,
         каждый файл содержит в себе токенизированные поэмы,
         извлеченные из "список файлов_i" в формате 
         одна строка - одна нормализованная поэма
"""
batch1 = batches[0] 
hypothesis1(batch1)

"""
  вход: batch2 - список пар (имя_лемм_i, имя_токен_i)
        где имя_токен_i - имя токенизированного файла, 
                          подготовленного выше
            имя_лемм_i  - имя лемматизированного файла             

  выход: по файлу "имя_лемм_i" на каждый "имя_токен_i" в списке,
         в формате одна строка - одна лемматизированная поэма 
"""
batch2 = batches[0]
hypothesis2(batch2)
