# -*- coding: utf-8 -*-
import subprocess
import re
import Io
from pprint import pprint as pp

brackets = re.compile(u"}{")
uncertainty = re.compile(u"(\?*\|[а-яё?]+|\?*)")

def lemmatize(string):
  def parse(text):
    first = re.sub(brackets, u' ', text[1:-1])
    then  = re.sub(uncertainty, u'', first)
    return then.split()

  args = ("mystem","-l","tmpin","tmpout" )
  Io.write(string, args[2])
  subprocess.call(args,shell=True)

  return parse(Io.read(args[3]))


if __name__ == "__main__":
  text = u"Кто-нибудь, из aalto позвоните Ёжи зачем-либо, щекотно-с кому-то ха-ха-ха-ха!\n"
  print(text)
  result = lemmatize(text)
  pp(result)