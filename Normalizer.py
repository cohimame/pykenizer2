# -*- coding: utf-8 -*-
import re

yo = re.compile(u"[Ёё]")
oneletter = re.compile(u"[-–][жтс]([^а-яё]|$)")
fewletter = re.compile(u"[-–](то|либо|нибудь|таки|будто|ка|же)")
multihyphen = re.compile(u"[а-яё]+([-–][а-яё]+){3,}")

def clean_hyphen(text):
  fewlet = lambda t: re.sub(fewletter,'',t)
  multihyph = lambda t: re.sub(multihyphen,'',t)
  hyphone = lambda t: re.sub(oneletter,' ',t)
  return hyphone(multihyph(fewlet(text)))

def normalize(text):
  strp  = lambda t: t.strip().lower()
  clyo  = lambda t: re.sub(yo,u"е",t)
  clhyp = lambda t: clean_hyphen(t)

  return clhyp(clyo(strp(text)))

def test():
    test_text =  u"Кто-нибудь позвоните-ж Ёжи-сан зачем-либо, щекотно-с, кому-то-с\n Вам-то легко рассуждать-с"
    normalized = normalize(test_text)
    print "normalizing standart example"
    print "input: "  + test_text     
    print "output: " + normalized

if __name__ == "__main__":
  test()
  