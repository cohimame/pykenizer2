# -*- coding: utf-8 -*-
import StopWords
import PoemHTMLParser
import Normalizer
import Lemmatizer
import PosTagger
import Io

stopwords = StopWords.extract()

"""
На выбор три 
"""


def tokenize(poem_file):
  result = []
  poems  = PoemHTMLParser.extract_poems(poem_file)
  for poem in poems:
    npoem   = Normalizer.normalize(poem)
    tokens  = npoem.split()
    nonstop = [w for w in tokens if w not in stopwords]
    if len(nonstop)>4:
      p = ' '.join(nonstop)+'\n'
      result.append(p)
  return result

"""
  def lemmatize(poem_file):
    result = []
    poems  = PoemHTMLParser.extract_poems(poem_file)
    for poem in poems:
      npoem   = Normalizer.normalize(poem)
      lemmas  = Lemmatizer.lemmatize(npoem)
      nonstop = [w for w in lemmas if w not in stopwords]
      if nonstop:
        p = ' '.join(nonstop)+'\n'
        result.append(p)
    return result


  def tagging(poem_file):
    result = []
    poems  = PoemHTMLParser.extract_poems(poem_file)
    for poem in poems:
      npoem   = Normalizer.normalize(poem)
      tagged  = PosTagger.postag(npoem)
      #print(tagged)
      nonstop = [w for w in tagged if w.split('_')[0] not in stopwords]      
      if nonstop:
        p = ' '.join(nonstop)+'\n'
        result.append(p)
    return result
"""


if __name__ == "__main__":
  INPUT  = "test_input/corpora/A_Klin"
  OUTPUT_LEM = "test_output/lemmatized/A_Klin_lem"
  OUTPUT_TOK = "test_output/lemmatized/A_Klin_tok"
  OUTPUT_POS = "test_output/lemmatized/A_Klin_pos"

  

  #poems = Io.read(INPUT)

  #tokenized_poems  = tokenize(poems)
  #lemmatized_poems = lemmatize(poems)
  #postagged_poems  = tagging(poems)

  #Io.write(lemmatized_poems,OUTPUT_LEM)
  #Io.write(tokenized_poems,OUTPUT_TOK)
  #Io.write(postagged_poems,OUTPUT_POS)

