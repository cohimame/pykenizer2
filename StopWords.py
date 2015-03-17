# -*- coding: utf-8 -*-
import os
import codecs
from sets import Set
import Io

DIR = "stopwords/"
TEST_OUTPUT = "test_output/stopwords_united_set.txt"

def collect_stopwords(directory=DIR):
  stopwords = Set()
  for f in os.listdir(directory):
    stopwords = stopwords | read_set(directory+f)
  return stopwords

def read_set(source):
  f = Io.read(source)
  words = f.split("\r\n")
  return Set(words)


if __name__ == "__main__":

  def test(sourcedir,output):
    output = codecs.open(output, mode='w',encoding='utf-8')
    for word in collect_stopwords(sourcedir):
      output.write(word+"\n")
    output.close()

  print "forming stop word list from \"{0}\" dir".format(DIR)
  test(DIR,TEST_OUTPUT)


  print "...done"
  print "saving to \"" + TEST_OUTPUT + "\" file"
