# -*- coding: utf-8 -*-
import os
import Io
import pprint

DIR = "stopwords/"
TEST_OUTPUT = "test_output/stopwords_united_set.txt"

def collect_stopwords(directory=DIR):
  stopwords = set()
  for f in os.listdir(directory):
    stopwords = stopwords | read_set(directory+f)
  return stopwords

def read_set(source):
  words = set()
  with open(source,encoding='utf-8') as infile:
    for l in infile:
      word = l.split()[0]
      words.add(word)
  return words

if __name__ == "__main__":
  def test(sourcedir,output):
    stopwords = collect_stopwords()
    with open(output,mode='w',encoding='utf-8') as outfile:
      for word in stopwords:
        outfile.write(word+"\n")  


  print( "forming stop word list from \"{0}\" dir".format(DIR) )

  test(DIR,TEST_OUTPUT)

  print ("...done")
  print ("saving to \"" + TEST_OUTPUT + "\" file")