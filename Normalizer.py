# -*- coding: utf-8 -*-
import re
import string

yo = re.compile("[Ёё]")
oneletter = re.compile("[-–][жтс]([^а-яё]|$)")
fewletter = re.compile("[-–](то|либо|нибудь|таки|будто|ка|же)")
multihyphen = re.compile("[а-яё]+([-–][а-яё]+){3,}")

def kill_punct(text):
  pnkt = string.punctuation.replace("-","")
  dd = {ord(c):None for c in pnkt}
  result = text.translate(dd)
  return result 

def clean_hyphen(text):
  fewlet = lambda t: re.sub(fewletter,'',t)
  multihyph = lambda t: re.sub(multihyphen,'',t)
  hyphone = lambda t: re.sub(oneletter,' ',t)
  return hyphone(multihyph(fewlet(text)))

def normalize(text):
  strp  = lambda t: t.strip().lower()
  clyo  = lambda t: re.sub(yo,"е",t)
  clhyp = lambda t: clean_hyphen(t)

  return kill_punct(
            clhyp(
              clyo(
                strp(text))))

def test():
    test_text = "Кто-нибудь позвоните-ж Ёжи-сан зачем-либо, щекотно-с, кому-то-с\n Вам-то легко рассуждать-с"
    normalized = normalize(test_text)
    print ("normalizing standart example")
    print ("input: "  + test_text )    
    print( "output: " + normalized)
    print(normalized.split())

if __name__ == "__main__":
  test()

  
  
