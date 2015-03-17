# -*- coding: utf-8 -*-
import pymorphy2
import subprocess
import re
import Io

class ILemmatizer:
  def __init__(self):
    pass
  def __repr__(self):
    return "abstract lemmatizer does nothing"  
  def lemmatize(self, t):
    pass

class FastYaLemmatizer(ILemmatizer):
  brackets = re.compile(u"}{")
  uncertainty = re.compile(u"(\?*\|[а-яё?]+|\?*)")

  def __init__(self):
    self.args = ("mystem","-l","tmpin","tmpout" )

  def __repr__(self):
    return "pymystem3 lemmatizer"

  def lemmatize(self, text):
    def parse(t):
      first = re.sub(self.brackets, u' ', t[1:-1])
      then  = re.sub(self.uncertainty, u'', first)
      return then.split()

    Io.write(text, self.args[2])
    subprocess.call(self.args,shell=True)
    return parse(Io.read(self.args[3]))

class PyMorphyLemmatizer(ILemmatizer):
  def __init__(self):
    self.morph = pymorphy2.MorphAnalyzer()

  def __repr__(self):
    return "pymorphy2 lemmatizer"

  def lemmatize(self, text):
    nf = lambda x: self.morph.parse(x)[0].normal_form
    tokens = text.split()
    lemmas = [nf(t) for t in tokens]
    return lemmas

if __name__ == "__main__":
  import Normalizer

  mystem = FastYaLemmatizer()
  pymorpher = PyMorphyLemmatizer()
  
  text = u"Кто-нибудь, позвоните Ёжи зачем-либо, щекотно-с кому-то\n"
  norm      = Normalizer.normalize(text)

  print "input: " + text  
  print u"mystem output: " + Io.list_to_string(mystem.lemmatize(text))
  print u"mystem output: " + Io.list_to_string(mystem.lemmatize(norm))

  print u"pymorphy output: " + Io.list_to_string(pymorpher.lemmatize(text))
  print u"pymorphy output: " + Io.list_to_string(pymorpher.lemmatize(norm))

