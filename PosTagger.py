# -*- coding: utf-8 -*-
import subprocess
import re
import Io
from pprint import pprint as pp

"""
  Части речи
  A прилагательное
  ADV наречие
  ADVPRO  местоименное наречие
  ANUM  числительное-прилагательное
  APRO  местоимение-прилагательное
  COM часть композита - сложного слова
  CONJ  союз
  INTJ  междометие
  NUM числительное
  PART  частица
  PR  предлог
  S существительное
  SPRO  местоимение-существительное
  V глагол

  -n  Построчный режим; каждое слово печатается на новой строке.
  -l  Не печатать исходные словоформы, только леммы и граммемы.
  -i  Печатать грамматическую информацию, расшифровка ниже.
  -g  Склеивать информацию словоформ при одной лемме (только при включенной опции -i).
  -d  Применить контекстное снятие омонимии.

"""

non  = re.compile("{[a-z?]*}")
pre  = re.compile("{[-а-яё?]*=")
post = re.compile("=*}") 

def postag(string):
  def parse(line):
    then  = line.strip().split(',')[0]
    then  = re.sub(non,"_UNK",then)
    then  = re.sub(pre, '_', then)
    then  = re.sub(post, '', then)
    return then
  
  args = ("mystem","-nigd","tmpin","tmpout" )

  Io.write(string, args[2])
  subprocess.call(args,shell=True)

  
  with open(args[3],encoding='utf-8') as infile:
    tagged_tokens = [parse(l) for l in infile]  
  return tagged_tokens


if __name__ == "__main__":
  text = "Кто-нибудь, из aalto позвоните Ёжи зачем-либо, щекотно-с кому-то ха-ха-ха-ха!\n"
  print(text)
  result = postag(text)
  pp(result)  