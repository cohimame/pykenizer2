# -*- coding: utf-8 -*-

def read(input):
  with open(input,encoding='utf-8') as infile:
    text = infile.read()
  return text

def write(poems, output):
  with open(output,mode='w',encoding='utf-8') as outfile:		
    for poem in poems:
      outfile.write(poem)   	
  
def list_to_string(lisp, sep = u', '):
    return u"[{}]".format(sep.join(lisp))
