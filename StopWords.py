# -*- coding: utf-8 -*-
import os
import Io
import pprint

DIR = "stopwords/"
TEST_OUTPUT = "test_output/stopwords_united_set.txt"

def extract(directory=DIR):
  stopwords = set()
  for f in os.listdir(directory):
    stopwords = stopwords | read_set(directory+f)
  return stopwords

def read_set(source):
  with open(source,encoding='utf-8') as infile:
    stopwords = [word.strip() for word in infile]  
  return set(stopwords)

def test(sourcedir,output):
  stopwords = extract()
  sw = [word+"\n" for word in stopwords]
  Io.write(sw,output)  

if __name__ == "__main__":
  print( "forming stop word list from \"{0}\" dir".format(DIR) )
  test(DIR,TEST_OUTPUT)
  print ("saving to \"" + TEST_OUTPUT + "\" file")