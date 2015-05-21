# -*- coding: utf-8 -*-
from pprint import pprint
import Shuffling
import Io
import Tokenizer
import subprocess


"""
  Формируем названия файлов на которых 
  будет происходить проверка гипотез.
"""
def form_batches(random_datasets,output):
  size = len(random_datasets)
  rang = range(size)

  h1_names = ["{}tok{}.csv".format(output,idx) for idx in rang ]
  h2_names = ["{}lem{}.csv".format(output,idx) for idx in rang ]

  batch1 = zip(h1_names, random_datasets)
  batch2 = zip(h2_names, h1_names)

  return batch1,batch2

"""
  берем кортеж вида (имя, случайный список файлов) 
  и формируем токенизированные файлы для обучения
"""
def hypothesis1(batch1): 

  def tok(output,files):
    with open(output, mode='w', encoding='utf-8') as outfile: 
      for file in files:
        poem_file  = Io.read(file)
        norm_poems = Tokenizer.tokenize(poem_file)
        for poem in norm_poems:
          outfile.write(poem) 
   
  for (name, part) in batch1:  
    print(name, part)
    tok(name, part)


"""
  берем предыдущие три токенизированных файла,
  лемматизируем с помощью mystem, пишем на диск

  Mystem при лемматизации не сохраняет структуру 
  файла, поэтому каждая поэма помечается меткой, 
  которая после лемматизации удаляется.

  Влияет ли наличие метки на качество снятия
  омонимии? Мне неизвестно.
"""
def hypothesis2(batch2):
  def form_labeled_files(input,output):
    with open(output, mode='w', encoding='utf-8') as outfile:
      with open(input, encoding='utf-8') as infile:
        for line in infile:
          mod  = line.strip() + " SPLIT\n" 
          outfile.write(mod)

  def remove_labels(input,output):
    with open(output, mode='w', encoding='utf-8') as outfile:
      with open(input,encoding='utf-8') as infile:
        for line in infile:
          if line != "SPLIT??\n":
            mod  = line.strip() + " " 
            outfile.write(mod) 
          else:
            outfile.write("\n")          

  def mass_lemmatize(inp,output):
    args = ("mystem", "-nlde", "utf-8", inp, output)
    subprocess.call(args, shell=True)
    return 0
   
  def lem(output, input):
    labeled = input + "_labeled"
    lemmed  = input + "_labeled_lemmatized"
    print(input)
    print(lemmed)
    form_labeled_files(input, labeled)
    mass_lemmatize(labeled, lemmed)
    remove_labels(lemmed,output)

  for (lemmatized, tokenized) in batch2:  
    lem(lemmatized, tokenized)            


if __name__ == "__main__":
  TEST_ROOT = "test_input\\tree\\"
  TEST_OUT  = "test_output\\"
  NUMBER = 4
  SIZE = 3
  random_datasets = Shuffling.random_partition(TEST_ROOT,NUMBER,SIZE)

  test_batch1, test_batch2 = form_batches(random_datasets,TEST_OUT)

  #pprint(list(test_batch1))

  hypothesis1(list(test_batch1))

  #pprint(list(test_batch2))

  hypothesis2(test_batch2)
