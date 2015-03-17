# -*- coding: utf-8 -*-
import re
import codecs
import Splitter
from collections import Counter

hyphWPat = re.compile(u".*[-–].*")

def count_word_freq(words):
  return Counter(words).most_common()

def count_hyphen_freq(words):
  hyphwords = [w for w in words if re.match(hyphWPat, w) is not None]
  return Counter(hyphwords).most_common()  

def save_stats(output, stats):
  output = codecs.open(output, mode='w',encoding='utf-8')
  for wf in stats:
    w = wf[0]
    f = str(wf[1])
    output.write(u'{0} - {1}\n'.format(w, f))
  output.close() 

if __name__ == "__main__":
  words = Splitter.split_big_file("test_output/test_summary.txt")
  total_freq       = count_word_freq(words)
  with_hyphen_freq = count_hyphen_freq(words)
  print "saving"
  save_stats("test_output/total.txt",total_freq)
  save_stats("test_output/hyphen.txt",with_hyphen_freq)
  print "done"