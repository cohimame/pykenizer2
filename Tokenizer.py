# -*- coding: utf-8 -*-
import StopWords
import PoemHTMLParser
import Normalizer
from Lemmatizer import FastYaLemmatizer

'''
  Токенизатор — инструмент для автоматического разделения текста на токены - 
  - цепочки символов, которые мы хотим считать минимальными линейными 
  единицами текста. 

  Задача данного токенизатора - подготовить корпус поэзии к подаче 
  на вход некоторым программам topic modeling.

  Токенизатор считает токеном последовательность символов русского
  алфавита, возможно, разделенную произвольным числом дефисов.
  Например: "когда-нибудь", "рок-н-ролл", "ха-ха-ха-ха".
 
  Так же токенизатор:
    1. "знает" структуру файлов корпуса поэзии
    2. рассматривает последовательности, длина которых строго больше единицы.
    3. делает lowercase
    4. берет на себя задачу по замене "ё" на "е".  
    5. устраняет стоп слова.
  
'''

stopwords = StopWords.collect_stopwords()

lemmatizer = FastYaLemmatizer()

def tokenize(poem_file):
  result = []
  poems  = PoemHTMLParser.extract_poems(poem_file)
  for poem in poems:
    npoem   = Normalizer.normalize(poem)
    lemmas   = lemmatizer.lemmatize(npoem)
    nonstop = [w for w in lemmas if w not in stopwords]
    if nonstop:
      p = u' '.join(nonstop)+u'\n'
      result.append(p)
  return result


if __name__ == "__main__":
  import Io
  INPUT  = "test_input/corpora/A_Klin"
  OUTPUT = "test_output/lemmatized/A_Klin"

  poems = Io.read(INPUT)

  lemmatized_poems = tokenize(poems)

  Io.write(lemmatized_poems,OUTPUT)

