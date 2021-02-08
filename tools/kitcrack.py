import sys,time,optparse,hashlib
author="""
      <Tsociety>
<Kit Password Cracker>
         ___
        |   |
       _|___|_
      /#######\ 
     |-+-###-+-|
     |#########|
      \#\___/#/
       \#####/
"""
Version="%prog 0.7"
usage = "usage: %prog [options] "
print(author)

class kit_crack_engine:
 def __init__(self):
  self.starttime = time.time()
  self.extract_input_data()
  self.openandgetup()
  self.start_cracking_engine()
  self.closetime = time.time()
  self.close_all_process()
  
 def encrypt(self, string):
  if self.salt=="md5":
   return hashlib.md5(string).hexdigest()
  if self.salt=="sha1":
   return hashlib.sha1(string).hexdigest()
  if self.salt=="sha224":
   return hashlib.sha224(string).hexdigest()
  if self.salt=="sha256":
   return hashlib.sha256(string).hexdigest()
  if self.salt=="sha384":
   return hashlib.sha384(string).hexdigest()
  if self.salt=="sha512":
   return hashlib.sha512(string).hexdigest()

 def start_cracking_engine(self):
  self.got_hash = []
  for i in self.words:
   if self.encrypt(i.strip("\n")) in self.hashlist:
    print "[+] Hash Cracked! {} = {}".format(i.strip('\n'), self.encrypt(i.strip("\n")))
    self.result.write(" {} : {}\n".format(i.strip('\n'), self.encrypt(i.strip("\n"))))
    self.got_hash.append(i.strip("\n"))
    if len(self.got_hash)==len(self.hashlist):
     break
   self.pwdtries = self.pwdtries + 1
  return

 def extract_input_data(self):
  self.starttime=time.time()
  self.pwdtries=0

  parser = optparse.OptionParser(usage, version=Version)
  parser.add_option("-f", "--file", action="store", type="string", dest="filename",help="Please Specify Path of Hash File", default=None)
  parser.add_option("-d", "--dict", action="store", type="string", dest="dictionery", help="Please Specify Path of Password Dictionery.", default=None)
  parser.add_option("-o", "--output", action="store", type="string", dest="output", help="Please Specify Path for Saving Cracked hash", default='cracked_hash.txt')
  parser.add_option("-s", "--salt", action="store", type="string", dest="salt", help="Please Provide Hash Salt. ex: md5, sha1, sha256, sha512", default=None)
  (option, args)=parser.parse_args()

  print "Extracting input data..."
  self.filename=option.filename
  self.dictionery=option.dictionery
  self.output=option.output
  self.salt=option.salt
  
  if not self.salt:
   print "Please provide Hash Salts"
   sys.exit(0)
  if self.salt not in hashlib.algorithms:
   print "Please provide an actual Hash Salt. \n\t\tEx : {}".format(hashlib.algorithms)
   sys.exit(0)

  if not self.filename:
   print "Please Provide Hash File."
   sys.exit(0)
  
  if not self.dictionery:
   print "Please Provide Password Source."
   sys.exit(0)
  if not self.output:
   print "Please Provide Output Path."
   sys.exit(0)
  return

 def openandgetup(self):
  hashlist = open(self.filename,'r')
  wordlist = open(self.dictionery,'r')  
  self.hashlist = [i.strip('\n') for i in hashlist.xreadlines()] 
  self.words = wordlist.xreadlines()
  self.result = open(self.output,'a')
  return

 def close_all_process(self):
  self.result.close()
  self.time_management()
  return
  
 def time_management(self):
  print "Time Taken:",self.closetime-self.starttime
  print "Tries:",self.pwdtries
  print "Speed:",self.pwdtries/(self.closetime-self.starttime)
  return

if __name__=="__main__":
 kit_crack_engine()
