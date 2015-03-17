# -*- coding: utf-8 -*-
import os
import codecs
import re
#--------------------
import Io
import Tokenizer 
import Lemmatizer
import CorporaStatistics

"""
  TEST_INPUT  = "test_input/corpora/"
  TEST_OUTPUT = "test_output/"
  TEST_TOKENIZED_OUT  = TEST_OUTPUT + "tokenized_summary.txt"
  TEST_LEMMATIZED_OUT = TEST_OUTPUT + "lemmatized_summary.txt"

  RAWPATH = "poetry_raw/"
  NORMALIZEDPATH = "poetry_normalized/summary.txt"
"""

def file_tokenize(inp,outp):
  poem_file = Io.read(inp)
  norm_poems = Tokenizer.tokenize(poem_file)
  Io.write(norm_poems,outp)

def dir_tokenize(raw,norm):
  author_list = os.listdir(raw)
  for author in author_list:
    file_tokenize(raw+author, norm+author)
   
def dir_tokenize_one_file(raw,dest):
  output = codecs.open(dest, mode='w',encoding='utf-8')
  for author in os.listdir(raw):
    poem_file  = Io.read(raw+author)
    norm_poems = Tokenizer.tokenize(poem_file)
    for poem in norm_poems:
      output.write(poem)
  output.close() 

def file_lemmatize(inp,outp):
  poem_file = Io.read(inp)
  norm_poems = Lemmatizer.lemmatize(poem_file)
  Io.write(norm_poems,outp)

def dir_lemmatize(raw,out):
  author_list = os.listdir(raw)
  for author in author_list:
    file_lemmatize(raw+author, out+author)
 
def dir_lemmatize_one_file(raw,dest):
  output = codecs.open(dest, mode='w',encoding='utf-8')
  for author in os.listdir(raw):
    poem_file  = Io.read(raw+author)
    norm_poems = Lemmatizer.lemmatize(poem_file)
    for poem in norm_poems:
      output.write(poem)
  output.close()   


if __name__ == "__main__":
  INPUT       = "test_input/corpora/"
  TOKENOUTPUT = "test_output/tokenized/"
  LEMMAINPUT  = TOKENOUTPUT
  LEMMAOUTPUT = "test_output/lemmatized/"

  STATISTICS  = "test_output/statistics/"
  TOKENSTATS  = STATISTICS + TOKENOUTPUT
  LEMMASTATS  = STATISTICS + LEMMAOUTPUT

  print "normalizing texts from \"" + INPUT + "\"\n" 
  dir_tokenize(INPUT,TOKENOUTPUT)
  print "saving in " + TOKENOUTPUT + "\n"
 
  print "lemmatizing texts with pymorphy2 from \"" + TOKENOUTPUT + "\"\n" 
  dir_lemmatize(LEMMAINPUT,LEMMAOUTPUT)
  print "saving in " + LEMMAOUTPUT + "\n"

"""
  print "lemmatizing texts from \"" + TOKENOUTPUT + "\"\n" 
  dir_lemmatize_one_file(TOKENOUTPUT,LEMMAOUTPUT)
  print "saving in " + LEMMAOUTPUT + "\n"

  print "processing corpora statistics"
  wrdfrq,hyphfrq = CorporaStatistics.count_stats(LEMMAOUTPUT)  

  print "saving corpora statistics"
  CorporaStatistics.save_stats(LEMMASTATS+"/total.txt", wrdfrq)
  CorporaStatistics.save_stats(LEMMASTATS+"/hyphen.txt",hyphfrq)
  print "done"

"""