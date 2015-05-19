# -*- coding: utf-8 -*-
import re
import string
from pprint import pprint

yo           = re.compile("[Ёё]")
oneletter    = re.compile("[-–][жтс]([^а-яё]|$)")
fewletter    = re.compile("[-–](то|либо|нибудь|таки|будто|ка|же)")
multihyphen  = re.compile("[а-яё]+([-–][а-яё]+){3,}")
lonelyHyphen = re.compile("([-–]+ | [-–]+ | -+ )")
endg         = re.compile("[a-z0-9@]+")


# collect weird russian punctuation in one place
pnkt = string.punctuation.replace("-",u"«»…“”")
dd = {ord(c):None for c in pnkt}

# translate() returns a copy of the string in which 
# all characters have been translated using table dd
def kill_punct(text):
  return text.translate(dd)


# remove all hyphens except interword ones
def clean_hyphen(text):
  fewlet    = lambda t: re.sub(fewletter,'',t)
  multihyph = lambda t: re.sub(multihyphen,'',t)
  hyphone   = lambda t: re.sub(oneletter,' ',t)
  engdig    = lambda t: re.sub(endg,'',t)
  lone      = lambda t: re.sub(lonelyHyphen,' ',t)
  return lone(
          engdig(
            hyphone(
              multihyph(
                fewlet(text)))))



# all normalization in one function
def normalize(text):
  strp  = lambda t: t.strip().lower()
  clyo  = lambda t: re.sub(yo,"е",t)
  clhyp = lambda t: clean_hyphen(t)

  return kill_punct(
            clhyp(
              clyo(
                strp(text))))

def test():
    test_text = "Кто-нибудь позвоните-ж кто- проблеме -------- 19999@htm Ёжи-сан зачем-либо, щекотно-с, кому-то-с\n Вам-то легко рассуждать-с"
    normalized = normalize(test_text)
    pprint ("normalizing standart example")
    print ("input: "  + test_text )    
    print( "output: " + normalized)
    print(normalized.split())

if __name__ == "__main__":
  test()

  
  
