# -*- coding: utf-8 -*-
import os
import codecs
import re
import csv

def read(f):
  doc = codecs.open(f,encoding='utf-8')
  text = doc.read()
  doc.close()
  return text

def write(poems,dest):
  output = codecs.open(dest, mode='w',encoding='utf-8')
  for poem in poems:
    output.write(poem)
  output.close()

def list_to_string(lisp, sep = u', '):
    return u"[{}]".format(sep.join(lisp))
