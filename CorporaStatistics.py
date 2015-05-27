# -*- coding: utf-8 -*-
import re
from collections import Counter
import sys
import csv

def sort_by_topic_prob(filepath, topic_number):
  with open(filepath, 'r') as f:
    rows = csv.reader(f, delimiter=',')
    sorted_list = sorted( rows, 
                          key = lambda x: float(x[topic_number]), 
                          reverse=True )
  return sorted_list



def write_csv(rows, output):
  with open(output, 'w') as f:
    for row in rows:
      join = ",".join(row) +"\n"
      f.write(join)

def test():
  TEST_IN  = "test_input/test-document-topic-dist.csv"
  for i in range(1,7):
    test_out = "test_output/sorted_by_{}_topic.csv".format(i)
    sorted_docs = sort_by_topic_prob(TEST_IN,i)
    write_csv(sorted_docs, test_out)
  

if __name__ == "__main__":
  test()


"""  
  INPUT  = "document-topic-distributions.csv"

  for i in range(7):
    output = "{}_topic_sorted".format(i)
    sorted_docs = sort_by_topic_prob(INPUT,i)
    write_csv(sorted_docs, TEST_OUT)
"""
"""

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


  """