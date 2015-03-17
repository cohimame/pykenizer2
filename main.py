# -*- coding: utf-8 -*-
import os
import codecs
#--------------------
import Io
import Tokenizer
import CorporaStatistics

def dir_tokenize_one_file(raw,dest):
  output = codecs.open(dest, mode='w',encoding='utf-8')
  for author in os.listdir(raw):
    poem_file  = Io.read(raw+author)
    norm_poems = Tokenizer.tokenize(poem_file)
    for poem in norm_poems:
      output.write(poem)
  output.close()

def dir_tokenize(inp,outp):
  author_list = os.listdir(inp)
  for author in author_list:
    file_tokenize(inp+author, outp+author)

def file_tokenize(inp, outp):
  poem_file = Io.read(inp)
  norm_poems = Tokenizer.tokenize(poem_file)
  Io.write(norm_poems, outp)


if __name__ == "__main__":

  INPUT  = "input/"
  OUTPUT = "output/"
  ISPTM  = OUTPUT + "summary.txt"
  STATISTICS  = "output/statistics/"

  print "normalizing texts from \"{0}\"\n".format(INPUT)

  dir_tokenize_one_file(INPUT,ISPTM)

  print "saving in \"{0}\"\n".format(ISPTM)

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