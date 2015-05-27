# -*- coding: utf-8 -*-
import csv

def read(input):
  with open(input,encoding='utf-8') as infile:
    text = infile.read()
  return text

def write(poems, output):
  with open(output,mode='w',encoding='utf-8') as outfile:   
    for poem in poems:
      outfile.write(poem)  

def write_csv(rows, output):
  with open(output, 'w') as f:
    for row in rows:
      join = ",".join(row) +"\n"
      f.write(join)
