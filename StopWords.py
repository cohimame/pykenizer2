# -*- coding: utf-8 -*-
import os
import codecs
from sets import Set
import Splitter
import Io

DIR = "stopwords/"
TEST_OUTPUT = "test_output/stopwords_united_set.txt"

def collect_stopwords(directory=DIR):
  stopwords = Set()
  for f in os.listdir(directory):
    sw = read_set(directory+f)
    stopwords = stopwords | sw
  return stopwords

def read_set(source):
  f = Io.read(source)
  words = Splitter.split(f)
  return Set(words)

def test(sourcedir,output):
  output = codecs.open(output, mode='w',encoding='utf-8')
  for word in collect_stopwords(sourcedir):
    output.write(word+"\n")
  output.close()

if __name__ == "__main__":
  print "forming stop word list from \"{0}\" dir".format(DIR)
  test(DIR,TEST_OUTPUT)
  print "...done"
  print "saving to \"" + TEST_OUTPUT + "\" file"
