# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser

class PoemHTMLParser(HTMLParser):
  def __init__(self):
    self.reset()      
    self.poems = []    

  def handle_data(self, data):
    self.poems.append(data)

  def getPoems(self):
    return self.poems

def extract_poems(text):
  parser = PoemHTMLParser()
  parser.feed(text)
  poems = parser.poems
  parser.close()
  return poems