import os, re, sys, time, codecs, datetime, random, hashlib, getpass, binascii, cryptography
from datetime import date
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode


inter='''
   <Tsociety toolkit>
<made by themobilehacker>
          ___
         |   |
        _|___|_
       /#######\ 
      |-+-###-+-|
      |#########|
       \#\___/#/
        \#####/

1)Info tools
2)Password tools
3)Stress tools
4)file encrypter
0)Update toolkit
99)exit
>'''

def load_key():
	return open("pass.dat","rb").read()

def write_key():
	key=Fernet.generate_key()
	with open("pass.dat","wb") as keyfile:
		keyfile.write(key)

def encrypt(filename,key):
	f = Fernet(key)
	with open(filename,"rb") as file:	
		filedata = file.read()
		encrypted_data = f.encrypt(filedata)
		with open(filename,"wb") as file:
			file.write(encrypted_data)

def decrypt(filename, key):
	f = Fernet(key)
	with open(filename, "rb") as file:
		encrypted_data = file.read()
	decrypted_data = f.decrypt(encrypted_data)
	with open(filename, "wb") as file:
		file.write(decrypted_data)

def nmap():
	while True:
		interface = '''
1)OS scanning
2)host scanning
3)open website port scan
99)exit
>'''
		root = input('rooted? y/N>')
		if root=='y'or'Y':
			ip=input("ip address>")
			ch=input(interface)
			if ch=='1':
				os.system('sudo nmap -A %s'%ip)
			elif ch=='2':
				os.system('sudo nmap -sP %s'%ip)
			elif ch=='3':
				os.system('sudo nmap -p 80, 443 %s'%ip)
			elif ch=='99':
				print("exiting...")
				break
		elif root=='n'or'N':
			ip=input("ip address>")
			ch=input(interface)
			if ch=='1':
				os.system('nmap -A %s'%ip)
			elif ch=='2':
				os.system('nmap -sP %s'%ip)
			elif ch=='3':
				os.system('nmap -p 80, 443 %s'%ip)
			elif ch=='99':
				print("exiting...")
				break

def infotools():
	while True:
		infointer='''
1)nmap
99)exit
>'''
		ch=int(input(infointer))
		if ch==1:
			nmap()
		elif ch==99:
			break
def stresstools():
	stressinter='''
1)httpslowreq
2)hulk DoS tool
3)Fire Rain DoS tool
99)exit
>'''
	while True:
		c=int(input(stressinter))
		if c==1:
			web=input('input website>')
			os.system('python2 tools/httpslowreq.py %s'%web)
		elif c==2:
			dos()
		elif c==3:
			web=input('input website>')
			os.system('python2 tools/FR.py %s'%web)
		elif c==99:
			break



def entro():
	print("if none enter 'null'.")
	na=input('input filename>')
	f=open(na,"w+")
	v1={input('birthyear last two digits>'),input('name or person>'),input('name of person in relationship>'),input('pet name>'),input('closest relative>'),input('best friend>'),input('another important word>'),input('another important number>')}
	t = 0
	f.write('123456') 
	fa=open(na,'a')
	fa.write('''123456789
picture1
password
12345678
111111
123123
12345
1234567890
senha
senpai
senpi
1234567
qwerty
abc123
Million2
000000
1234
iloveyou
ilikeyou
iloveu
ilikeu
aaron431
aron431
password1
qqww1122
123
omgpop
123321
654321
qwertyuiop
qwerty123456
123456a
a123456
666666
123456seven
asdfghjkl
ashley
987654321
unkown
'unknown
zxcvbnm
112233
chatbooks
20100728
123123123
princess
jacket025
evite
123abc
123qwe
sunshine
121212
dragon
1q2w3e4r
5201314
159753
0123456789
pokemon
qwerty123
Bangbang123
johnbandtalent
monkey
1qaz2wsx
abcd1234
default
aaaaaa
soccer
123654
dick
blowjob
fuckyou
fucku
micheal
michealafton
killer
trustno1
jordan
gordon
hunter
buster
soccer
batman
andrew
fuckme
harley
2000
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2021
2022
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
george
asshole
asshat
computer
michelle
jessica
pepper
1111
zxcvbnm
555555
131313
freedom
7777777
puss
fuckmemaggie
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
nicole
chelsea
biteme
matthew
access
yankees
dallas
austiun
thunder
taylor
matrix
william
williamafton
corvette
hello
martin
heather
secret
fucker
merlin
diamond
1234qwer
gfhjkm
hammer
silver
2222222
anthony
justin
themobilehacker
biromantic2020
biromantic
asextual
test
bailey
patrick
internet
scooter
orange
111111
golfer
cookie
richard
samantha
bigdong
bigdoggo
guitar
jackson
whatever
whateverdawg
mickey
mickeymouse
chicken
sparky
snoopy
maverick
pheonix
camero
sexy
peanut
morgan
welcome
falcon
cowboy
ferrari
samsung
anderea
smokey
smokeythebear
smokeybear
steelers
america
noyhing
parker
4444
rebecca
qweqwe
69696969
jacks
asdasd
asdedasded
december
november
magic
apollo
skippy
parrot
parrotos
timcat
godzilla
brooklyn
bullshit
loveme
saturn
therock
rockdwayne
redwings
bigboy
pumpkin
williams
''')

def kitpasscrack():
	hashf=input('hash file>')
	hashsalt=input('hash salt>')
	dic=input('password list file>')
	os.system('python2 tools/kitcrack.py -f %s'%hashf+' -s %s'%hashsalt+' -d %s'%dic)
def passtools():
	passinter='''
1)crunch
2)Entrophic password generator(still developing)
3)Kit password cracker
4)hash encoder
99)exit
>'''
	while True:
		i=int(input(passinter))
		if i==1:
			sleng=input('shortest length>')
			lleng=input('longest length>')
			pc=input('possible characters>')
			filen=input('output filename>')
			os.system('crunch %s'%sleng+' %s'%lleng+' %s'%pc+' -o %s'%filen)
		elif i==2:
			entro()
		elif i==3:
			kitpasscrack()
		elif i==4:
			Escolha()
		elif i==99:
			break
def Apresentacao():
	os.system('clear')
	

def Again(frase, call):
	opcao1 = input(frase)
	if opcao1 == "y":
		call()
	elif opcao1 == "n":
		Escolha()
	else:
		Again(frase,call)


def Escolha():
	Apresentacao()
	print("""
	[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

	\033[31mA\033[1;m) \033[31mENCODE\033[1;m - \033[32mMD5\033[1;m
	\033[31mB\033[1;m) \033[31mENCODE\033[1;m - \033[32mSHA1\033[1;m
	\033[31mC\033[1;m) \033[31mENCODE\033[1;m - \033[32mSHA224\033[1;m
	\033[31mD\033[1;m) \033[31mENCODE\033[1;m - \033[32mSHA256\033[1;m
	\033[31mE\033[1;m) \033[31mENCODE\033[1;m - \033[32mSHA384\033[1;m
	\033[31mF\033[1;m) \033[31mENCODE\033[1;m - \033[32mSHA512\033[1;m
	\033[31mG\033[1;m) \033[31mENCODE/DECODE\033[1;m - \033[32mBASE64\033[1;m
	\033[31mH\033[1;m) \033[31mENCODE/DECODE\033[1;m - \033[32mBINARY\033[1;m
	\033[31mI\033[1;m) \033[31mENCODE/DECODE\033[1;m - \033[32mHEXADECIMAL\033[1;m
	\033[31mJ\033[1;m) \033[31mENCODE/DECODE\033[1;m - \033[32mCIPHER OF CESAR\033[1;m
	\033[31mK\033[1;m) \033[31mREVERSE\033[1;m - \033[32mTEXT\033[1;m
	\033[31mL\033[1;m) \033[31mREVERSE\033[1;m - \033[32mWORDS\033[1;m

	\033[31mq\033[1;m) EXIT
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "A" or opcao1 == "a":
		Md5()
	elif opcao1 == "B" or opcao1 == "b":
		Sha1()
	elif opcao1 == "C" or opcao1 == "c":
		Sha224()
	elif opcao1 == "D" or opcao1 == "d":
		Sha256()
	elif opcao1 == "E" or opcao1 == "e":
		Sha384()
	elif opcao1 == "F" or opcao1 == "f":
		Sha512()
	elif opcao1 == "G" or opcao1 == "g":
		Base64()
	elif opcao1 == "H" or opcao1 == "h":
		Binario()
	elif opcao1 == "I" or opcao1 == "i":
		Hexadecimal()
	elif opcao1 == "J" or opcao1 == "j":
		CifraDeCesar()
	elif opcao1 == "K" or opcao1 == "k":
		TextReverse()
	elif opcao1 == "L" or opcao1 == "l":
		WordsReverse()
	elif opcao1 == "Q" or opcao1 == "q":
			print("exiting...")
	else: 
		Escolha()

def Md5():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN MD5\033[1;m: ")
	hash_object = hashlib.md5(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN MD5 (y/n) ?:\033[1;m ", Md5)

def Sha1():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN SHA1\033[1;m: ")
	hash_object = hashlib.sha1(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN SHA1 (y/n) ?:\033[1;m ", Sha1)

def Sha224():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN SHA224\033[1;m: ")
	hash_object = hashlib.sha224(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN SHA224 (y/n) ?:\033[1;m ", Sha224)

def Sha256():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN SHA256\033[1;m: ")
	hash_object = hashlib.sha256(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN SHA256 (y/n) ?:\033[1;m ", Sha256)

def Sha384():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN SHA384\033[1;m: ")
	hash_object = hashlib.sha384(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN SHA384 (y/n) ?:\033[1;m ", Sha384)

def Sha512():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO ENCRYPT IN SHA512\033[1;m: ")
	hash_object = hashlib.sha512(mystring.encode())
	print("")
	print(hash_object.hexdigest())
	print("")
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN SHA512 (y/n) ?:\033[1;m ", Sha512)

def Base64Encode():
	Apresentacao()
	mystring = str(input("\033[32mPLACE THE TEXT YOU WANT TO TRANSFORM IN BASE64\033[1;m: ")) 
	print("")
	encode = b64encode(mystring.encode('utf-8')) 
	decode = encode.decode('utf-8')
	print(decode)
	print("") 
	Again("\n\033[1;36mWOULD YOU LIKE TO TRANSFORM ANOTHER TEXT IN BASE64 (y/n) ?:\033[1;m ", Base64Encode)

def Base64Decode():
	Apresentacao()
	mystring = str(input("\033[32mPLACE THE TEXT YOU WANT TO UNCOVER IN BASE64\033[1;m: ")) 
	print("")
	try:
		decode = b64decode(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n[\033[1;91m!\033[1;m] INCORRECT PADDING")
		sleep(3)
		Base64Decode()
	Again("\n\033[1;36mWISHES TO UNCOVER ANOTHER TEXT IN BASE64 (y/n) ?:\033[1;m ", Base64Decode)

def Base64():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - BASE64
\033[31m2\033[1;m) DECODE - BASE64
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		Base64Encode()
	elif opcao1 == "2":
		Base64Decode()
	else:
		Base64()


def BinarioEncode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		mystring = input("\033[32mPLACE THE TEXT YOU WANT TO TRANSFORM IN BINARY\033[1;m: ")
		print("")
		bits = bin(int(binascii.hexlify(mystring.encode(encoding, errors)), 16))[2:]
		print(bits.zfill(8 * ((len(bits) + 7) // 8)))
		print("")
	except:
		print("\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		BinarioEncode()
	Again("\n\033[1;36mWOULD YOU LIKE TO TRANSFORM ANOTHER TEXT IN BINARY (y/n) ?:\033[1;m ", BinarioEncode)

def BinarioDecode(encoding='utf-8', errors='surrogatepass'):
	Apresentacao()
	try:
		binario = input("\033[32mPLACE THE SEQUENCE OF NUMBERS YOU DESIRE TO UNCOVER IN BINARY\033[1;m: ")
		binario = binario.replace(" ", "")
		n = int(binario, 2)
		print("")
		print(int2bytes(n).decode(encoding, errors))
		print("")
	except:
		print("\n\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		BinarioDecode()
	Again("\n\033[1;36mWISHES TO UNCOVER ANOTHER SEQUENCE IN BINARY (y/n) ?:\033[1;m ", BinarioDecode)

def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


def Binario():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - BINARY
\033[31m2\033[1;m) DECODE - BINARY
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		BinarioEncode()
	elif opcao1 == "2":
		BinarioDecode()
	else:
		Binario()


def HexaEncode():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO TRANSFORM IN HEXADECIMAL\033[1;m: ")
	print("")
	encode = binascii.hexlify(bytes(mystring, "utf-8"))
	encode = str(encode).strip("b")
	encode = encode.strip("'")
	encode = re.sub(r'(..)', r'\1 ', encode).strip()
	print(encode)
	print("")
	Again("\n\033[1;36mWANT TO TRANSFORM ANOTHER TEXT IN HEXADECIMAL (y/n) ?:\033[1;m ", HexaEncode)

def HexaDecode():
	Apresentacao()
	try:
		mystring = input("\033[32mPLACE THE SEQUENCE OF CHARACTERS YOU DESIRE TO UNCOVER IN HEXADECIMAL\033[1;m: ")
		print("")
		decode = bytes.fromhex(mystring).decode('utf-8')
		print(decode)
		print("")
	except:
		print("\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		HexaDecode()
	Again("\n\033[1;36mWISHES TO UNCOVER ANOTHER SEQUENCE IN HEXADECIMAL (y/n) ?:\033[1;m ", HexaDecode)

def Hexadecimal():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - HEXADECIMAL
\033[31m2\033[1;m) DECODE - HEXADECIMAL
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		HexaEncode()
	elif opcao1 == "2":
		HexaDecode()
	else:
		Hexadecimal()


def TextReverseEncode():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO REVERSE\033[1;m: ")
	print("")
	print(mystring[::-1])
	print("")
	Again("\n\033[1;36mWANTS TO MAKE ANOTHER REVERSE (y/n) ?:\033[1;m ", TextReverseEncode)


def TextReverseDecode():
	Apresentacao()
	mystring = input("\033[32mPLACE TEXT YOU WANT TO UNCOVER THE REVERSE\033[1;m: ")
	print("")
	print(mystring[::-1])
	print("")
	Again("\n\033[1;36mWANT TO UNCOVER ANOTHER REVERSE (y/n) ?:\033[1;m ", TextReverseDecode)

def TextReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - REVERSE-TEXT
\033[31m2\033[1;m) DECODE - REVERSE-TEXT
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		TextReverseEncode()
	elif opcao1 == "2":
		TextReverseDecode()
	else:
		TextReverse()


def WordsReverseEncode():
	Apresentacao()
	mystring = input("\033[32mPLACE THE TEXT YOU WANT TO REVERSE\033[1;m: ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\n\033[1;36mWANTS TO MAKE ANOTHER REVERSE (y/n) ?:\033[1;m ", WordsReverseEncode)

def WordsReverseDecode():
	Apresentacao()
	mystring = input("\033[32mPLACE TEXT YOU WANT TO UNCOVER THE REVERSE\033[1;m: ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\n\033[1;36mWANT TO UNCOVER ANOTHER REVERSE (y/n) ?:\033[1;m ", WordsReverseDecode)

def WordsReverse():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - REVERSE-WORDS
\033[31m2\033[1;m) DECODE - REVERSE-WORDS
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		WordsReverseEncode()
	elif opcao1 == "2":
		WordsReverseDecode()
	else:
		WordsReverse()


def CifraDeCesar():
	Apresentacao()
	print("""
[\033[1;32m*\033[1;m] CHOOSE ONE OF THE OPTIONS BELOW TO CONTINUE:

\033[31m1\033[1;m) ENCODE - CIPHER OF CESAR
\033[31m2\033[1;m) DECODE - CIPHER OF CESAR
""")
	opcao1 = input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		ChamarBloco1()
	elif opcao1 == "2":
		ChamarBloco2()
	else:
		CifraDeCesar()


def cifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) + chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado


def decifrar(palavras, chave):
	abc = "abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma = abc.find(letra) - chave
		modulo = int(soma) % len(abc)
		text_cifrado = text_cifrado + str(abc[modulo])

	return text_cifrado

def ChamarBloco1():
	Apresentacao()
	try:
		c = str(input('\n\033[32mTEXT FOR CIPHER\033[1;m: ')).lower()
		n = int(input('\033[32mNUMERICAL KEY\033[1;m: '))
		print("\033[32mRESULT\033[1;m:", cifrar(c, n))
		print("")
	except:
		print("\n\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		ChamarBloco1()
	Again("\n\033[1;36mDESIRE TO DO ANOTHER ENCODE IN CIPHER OF CESAR (y/n) ?:\033[1;m ", ChamarBloco1)


def ChamarBloco2():
	Apresentacao()
	try:
		cc = str(input('\n\033[32mTEXT TO BE DECODE\033[1;m: ')).lower()
		cn = int(input('\033[32mNUMERICAL KEY\033[1;m: '))
		print("\033[32mRESULT\033[1;m:", decifrar(cc, cn))
		print("")
	except:
		print("\n\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		ChamarBloco2()
	Again("\n\033[1;36mDESIRE TO DO ANOTHER DECODE IN CIPHER OF CESAR (y/n) ?:\033[1;m ", ChamarBloco2)

def dos():
	url = input('input url to DOS>')
	os.system('python2 tools/DOS.py %s'%url)

while True:
	c=int(input(inter))
	if c==1:
		infotools()
	elif c==2:
		passtools()
	elif c==3:
		stresstools()
	elif c==4:
		eninter='''
1)encrypt
2)decrypt
99)exit
>'''
		while True:
			en=int(input(eninter))
			if en==1:
				filename=input('name of file to encrypt>')
				key=load_key()
				encrypt(filename,key)
				print('done')
			elif en==2:
				filename=input('name of file to decrypt>')
				key=load_key()
				decrypt(filename,key)
			elif en==3:
				break
	elif c==99:
		break
		sys.exit()
	else:
		print('please input a number shown')