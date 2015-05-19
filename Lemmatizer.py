# -*- coding: utf-8 -*-
import subprocess
import re
import Io
from pprint import pprint

"""
  Команды mystem:
  -n  Построчный режим; каждое слово печатается на новой строке.
  -l  Не печатать исходные словоформы, только леммы и граммемы.
  -i  Печатать грамматическую информацию, расшифровка ниже.
  -g  Склеивать информацию словоформ при одной лемме (только при включенной опции -i).
  -d  Применить контекстное снятие омонимии.
"""

TMPIN  = "tmpin"
TMPOUT = "tmpout"
args = ("mystem","-l",TMPIN, TMPOUT)

brackets = re.compile(u"}{")
uncertainty = re.compile(u"(\?*\|[а-яё?]+|\?*)")

# обработка результата работы mystem
def parse(text):
  then = text[1:-1]
  then = re.sub(brackets, u' ', then)
  then = re.sub(uncertainty, u'', then)
  return then.split()

# эффективнее pymystem3? спорный вопрос.
def lemmatize(string):
  Io.write(string, TMPIN)
  subprocess.call(args,shell=True)
  lemmatizedString = Io.read(TMPOUT)
  return parse(lemmatizedString)

if __name__ == "__main__":
  text = "Кто-нибудь, из aalto позвоните Ёжи зачем-либо, щекотно-с кому-то ха-ха-ха-ха!\n"
  print(text)
  
  result = lemmatize(text)
  pprint(result)  
