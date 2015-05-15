# -*- coding: utf-8 -*-
import StopWords
import PoemHTMLParser
import Normalizer
import Lemmatizer
import Io

stopwords = StopWords.collect_stopwords()


def tokenize(poem_file):
  result = []
  poems  = PoemHTMLParser.extract_poems(poem_file)
  for poem in poems:
    npoem   = Normalizer.normalize(poem)
    tokens  = npoem.split()
    nonstop = [w for w in tokens if w not in stopwords]
    if nonstop:
      p = ' '.join(nonstop)+'\n'
      result.append(p)
  return result


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


if __name__ == "__main__":
  INPUT  = "test_input/corpora/A_Klin"
  OUTPUT_LEM = "test_output/lemmatized/A_Klin_lem"
  OUTPUT_TOK = "test_output/lemmatized/A_Klin_tok"

  print (stopwords)

  poems = Io.read(INPUT)

  tokenized_poems  = tokenize(poems)
  lemmatized_poems = lemmatize(poems)

  Io.write(lemmatized_poems,OUTPUT_LEM)
  Io.write(tokenized_poems,OUTPUT_TOK)

