# -*- coding: utf-8 -*-
import Shuffling
import Hypothesis

SOURCE = "D:\\poetry\\"
OUTPUT = "output\\"

"""
  Из файлов в папке SOURCE сэмплируем
  три случайных непересекающихся списка  
"""
PARTS = 3
SIZE  = 4200
random_datasets = Shuffling.random_partition(SOURCE,PARTS,SIZE)

"""
  Формируем названия файлов на которых 
  будет происходить проверка гипотез.
"""
batches = Hypothesis.form_batches(random_datasets,OUTPUT)


print("done forming batches")

"""
  вход: batch1 - список пар (имя_i, список файлов_i) 
  выход: по файлу "имя_i" на каждый кортеж в списке,
         каждый файл содержит в себе токенизированные поэмы,
         извлеченные из "список файлов_i" в формате 
         одна строка - одна нормализованная поэма
"""
batch1 = batches[0] 
Hypothesis.hypothesis1(batch1)

"""
  вход: batch2 - список пар (имя_лемм_i, имя_токен_i)
        где имя_токен_i - имя токенизированного файла, 
                          подготовленного выше
            имя_лемм_i  - имя лемматизированного файла             

  выход: по файлу "имя_лемм_i" на каждый "имя_токен_i" в списке,
         в формате одна строка - одна лемматизированная поэма 


"""
batch2 = batches[1]
Hypothesis.hypothesis2(batch2)
