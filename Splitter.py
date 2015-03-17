# -*- coding: utf-8 -*-
import re
import codecs

ru = re.compile(u"([а-яё]+([-–][а-яё]+)+|[а-яё][а-яё]+)")

def split(text):
  ''' memory fail on big size texts '''
  return [token[0] for token in ru.findall(text)]

'''
  Здесь возникает вопрос о возможном 
  междустрочном переносе слов. Например:
  
    Я пришел в МосГор-
    Транс.
    У них там - 
    Ренессанс.

  Распознавание и анализ подобных случаев
  кажется нам довольно нетривиальным.

'''
def split_big_file(source):
  result = []
  src = codecs.open(source, encoding='utf-8')
  for line in src:  
    words = split(line)
    result += words  
  src.close()
  return result

if __name__ == "__main__":
  text = u"кто-то любит рок-н-ролл, ха-ха-ха-ха! Кто-то любит т-образные волны\n"
  tokens = split(text)
  
  print text
  print "["+ u', '.join(tokens)+ "]"