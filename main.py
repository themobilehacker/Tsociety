import os,re,sys,base64,time,codecs,datetime,random,hashlib,getpass,binascii,cryptography
from datetime import date
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode
f=Fernet
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
5)repositories
0)Update toolkit (still in developent)
99)exit
>'''
intr='''---------------------------
--Tsociety file encrypter--
1)encrypt
2)decrypt
99)exit
---------------------------
>'''
def key():
    print('')
    key=input('password>')
    keyc=len(key)
    if keyc<=7:
        print('password must have at least 8 characters')
        sys.exit()
    elif keyc>=33:
        print('password must be less than 33 characters')
        sys.exit()
    key=hashlib.md5(str(key).encode())
    key=key.hexdigest()
    print(str(key))
    key=base64.urlsafe_b64encode(bytes(str(key),'utf-8'))
    return(key)
def enc(key):
    print('')
    fi=input('filename>')
    print('')
    print('   ***reading file data...***')
    os.system('zip enc -r %s'%fi)
    fd=open('enc.zip','rb').read()
    time.sleep(0.3)
    print('')
    print('***initializing Fernet key...***')
    time.sleep(0.4)
    print('')
    os.system('rm -rf %s'%fi)
    print('   ***encrypting file data***')
    print('')
    en=f(key).encrypt(fd)
    open(fi+'.enc','wb').write(en)
    print('      ***file encrypted***')
    os.system('rm -rf enc.zip')
def dec(key):
    print('')
    fi=input('filename>')
    print('')
    print('   ***reading file data...***')
    fd=open(fi,'rb').read()
    time.sleep(0.2)
    print('')
    print('***initializing Fernet key...***')
    time.sleep(0.35)
    print('')
    print('    ***decrypting data...***')
    print('')
    de=f(key).decrypt(fd)
    open(fi.replace('.enc','.zip'),'wb').write(de)
    os.system('unzip %s'%fi.replace('.enc',''))
    print('      ***file decrypted***')
    os.system('rm -rf %s'%fi.replace('.enc','.zip'))
    os.system('rm -rf %s'%fi)
    print('')
#nmap
def nmap():
	while True:
		interface = ''' NMAP
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
#banchmark
def benchmarkc():
	num1 = 212910
	num2 = 8323740
	num3 = 45334330
	num4 = 624345960
	num5 = 5234356660
	num6 = 68173467770
	num7 = 605341278530
	num8 = 1835932389260
	num9 = 19384533190360
	num10 = 10287502900380
	num11 = 213453142239940
	num12 = 8325321435548950
	num13 = 45333576567327860
	num14 = 624345697274636770
	num15 = 5234359360746805920
	num16 = 68173462569364844640
	num17 = 605341275638923843560
	num18 = 1835932384626357983480
	num19 = 19384533195685693672300
	num20 = 102875029028472043231240
	randomnum1 = num13
	randomnum2 = num5
	randomnum3 = num3
	randomnum4 = num2
	randomnum5 = num9
	randomnum6 = num2
	randomnum7 = num5
	randomnum8 = num3
	randomnum9 = num9
	mul1 = num3 + num7 * num18 + randomnum2 + num10
	mul2 = mul1 * num3 * num14 + randomnum4 + mul1 + num17
	mul3 = mul2 * mul1 * num5 + num4 - num19 - num8 / mul2
	mul4 = mul2 * mul2 * num19 - randomnum9 / mul3 * mul2 - num20 + mul1
	equation1 = num1 * randomnum2
	equation2 = equation1 + num2 / randomnum2
	equation3 = equation1 + equation2
	equation4 = equation3 - equation1 * num3
	equation5 = equation2 + equation1 / num1 + num3 * randomnum2 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation2 = equation1 + num2 / randomnum2 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation3 = equation1 + equation2 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation4 = equation3 - equation1 * num3 + num3 * num10 / randomnum4 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation5 = equation2 + equation1 / num1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation6 = equation5 * num7 + equation4 / equation1 + num3 +randomnum2 * randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 * mul1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation7 = equation4 + num10 * num9 / num8 * num10 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation8 = equation5 * num7 + equation4 / equation1 + num3 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + mul1 * num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation9 = equation4 + num10 * num9 / num8 * num10 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation10 = equation2 + equation6 / num1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation11 = equation5 * num7 + equation4 / equation1 + num3 +randomnum2 * randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * mul2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation12 = equation4 + num10 * num9 / num8 * num10 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation13 = equation5 * num7 + equation4 / equation1 + num3 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * equation2 / num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation14 = equation4 + num10 * num9 / num8 * num10 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation15 = equation2 + equation14 / num1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation16 = equation5 * num7 + equation14 / equation9 + num3 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation17 = equation11 + equation1 / num1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation18 = equation5 * num7 + equation17 / equation1 + num3 +randomnum3 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation19 = equation13 + num10 * num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation20 = equation5 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * mul3 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20
	equation21 = equation11 + equation1 / num1 * num7 + equation19 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 
	equation22 = equation5 * num7 + equation12 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation23 = equation13 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation24 = equation5 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 *  num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 
	equation25 = equation11 + equation1 / num1 * num7 + equation19 / equation24 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + mul4 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 
	equation26 = equation5 * num7 + equation12 / equation25 + num3 +randomnum2 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation27 = equation13 + num10 * num9 / num8 * num10 * num7 + equation19 / equation26 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num10 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num17 / num3 * num16 + num13 * num12 / num19 * num14 + equation23 * num12 / num19 
	equation27 = equation13 + num10 * num9 / num8 * num10 * num7 + equation26 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation28 = equation5 * num7 + equation19 / equation27 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 
	equation29 = equation11 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 
	equation30 = equation5 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation31 = equation13 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation32 = equation5 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation31 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 
	equation33 = equation11 + equation32 / num1 * num7 + equation19 / equation28 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 
	equation34 = equation33 * num7 + equation32 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation35 = equation34 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 +num20*num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num10 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + equation23 * num12 / num19 
	equation36 = equation35 + num16 * num9 / num8 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation28 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation21 * num1 / num9 
	equation37 = equation36 * num7 + equation14 / equation9 + num3 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation38 = equation37 + equation1 / num1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation39 = equation38 * num7 + equation17 / equation1 + num3 +randomnum3 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation40 = equation39 + num10 * num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation41 = equation40 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * mul3 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 
	equation42 = equation41 + equation1 / num1 * num7 + equation19 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18* mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 
	equation43 = equation42 * num7 + equation12 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation44 = equation43 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation45 = equation44 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17*num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 *  num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 
	equation46 = equation45 + equation1 / num1 * num7 + equation19 / equation24 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + mul4 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 
	equation47 = equation46 * num7 + equation12 / equation25 + num3 +randomnum2 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 *num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation48 = equation47 + num10 * num9 / num8 * num10 * num7 + equation19 / equation26 + num20 * num4+num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num10 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num17 / num3 * num16 + num13 * num12 / num19 * num14 + equation23 * num12 / num19 
	equation49 = equation48 + num10 * num9 / num8 * num10 * num7 + equation26 / num1 + equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation50 = equation49 * num7 + equation19 / equation27 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 
	equation51 = equation50 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 
	equation52 = equation51 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation53 = equation52 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation54 = equation53 * num7 + equation19 / equation18 + num3 * mul1 + equation19 / equation31 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 
	equation55 = equation54 + equation32 / num1 * num7 + equation19 / equation28 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 
	equation56 = equation55 * num7 + equation32 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 /num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation57 = equation56 + num10 * num9 / num8 * num10 * num7 + + equation56 * equation56 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation28 + num3 * num10 / num7 * num4 + num7 * num10 / num19
	equation58 = equation57 + num16 * num9 / num8 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation57 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation50 / equation21 * num1 / num9 
	equation59 = equation58 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * mul3 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 
	equation60 = equation59 + equation1 / num1 * num7 + equation19 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18* mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 
	equation61 = equation60 * num7 + equation12 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation62 = equation61 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation63 = equation62 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17*num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 *  num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation64 = equation63 + equation1 / num1 * num7 + equation19 / equation24 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + mul4 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation65 = equation64 * num7 + equation12 / equation25 + num3 +randomnum2 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 *num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation66 = equation65 + num10 * num9 / num8 * num10 * equation33 / equation34 * num7 + equation19 / equation26 + num20 * num4+num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num10 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num17 / num3 * num16 + num13 * num12 / num19 * num14 + equation23 * num12 / num19 
	equation67 = equation66 + num10 * num19 / num18 * num10 * num7 + equation26 / num1 + equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation68 = equation67 * num7 + equation19 / equation27 + num3 * num7 + equation19 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation69 = equation68 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation70 = equation69 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation71 = equation70 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation72 = equation71 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation31 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation73 = equation72 + equation72 / num1 * num7 + equation19 / equation28 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation74 = equation73 * num7 + equation32 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 /num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation75 = equation74 + num10 * num9 / num8 * num10 * num7 + + equation56 * equation56 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 
	equation76 = equation75 + num16 * num9 / num8 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation57 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation50 / equation21 * num1 / num9 
	equation77 = equation76 * equation2 * equation3 / equation4 / equation5 * equation76 + equation8 * equation7 + equation9 - equation10 * equation11 - equation13 * equation12 / equation14 * equation13 / equation17 * equation15 * equation14 / equation16 * equation18 * equation19 * equation20 * equation22 / equation21 * equation24 * equation28 / equation30 * equation31 / equation35 * equation32 * equation33 / equation34 + num2 + equation36 + num15 * num12 / num19 * num14 + equation21 * num1 / num9 * num12 / num19 * num14 + num17 * num12 / num9 * num12 / num19 * num14 + num17 * num12 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num1 * mul2 / num7 * num4 + num7 * num10 / num7 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation78 = equation77 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation79 = equation78 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation80 = equation79 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation81 = equation80 * num7 + equation19 / equation18 + num3 * num7 + equation69 / equation31 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation82 = equation81 + equation72 / num1 * num7 + equation19 / equation28 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation83 = equation82 * num7 + equation32 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 /num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation84 = equation83 + num10 * num9 / num8 * num10 * num7 + + equation56 * equation56 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 
	equation85 = equation84 + num16 * num9 / num8 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation57 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation50 / equation21 * num1 / num9 
	equation86 = equation85 * equation2 * equation3 / equation4 / equation5 * equation76 + equation8 * equation7 + equation9 - equation10 * equation11 - equation13 * equation12 / equation14 * equation13 / equation17 * equation15 * equation14 / equation16 * equation18 * equation19 * equation20 * equation22 / equation21 * equation24 * equation28 / equation30 * equation31 / equation35 * equation32 * equation33 / equation34 + num2 + equation36 + num15 * num12 / num19 * num14 + equation21 * num1 / num9 * num12 / num19 * num14 + num17 * num12 / num9 * num12 / num19 * num14 + num17 * num12 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num1 * mul2 / num7 * num4 + num7 * num10 / num7 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation87 = equation86 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation88 = equation87 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation89 = equation88 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation90 = equation89 * num7 + equation19 / equation18 + num3 * num7 + equation19 / equation31 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation91 = equation90 + equation72 / num1 * num7 + equation19 / equation8 + num3 * num17 + equation10 / mul1 *equation18 + num3 * num10 / num7 * num14 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation92 = equation91 * num7 + equation32 / equation1 + num3 +randomnum2 / randomnum1 + num3 * num10 * mul2 /num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation93 = equation92 + num10 * num9 * equation33 * equation33 / equation34 / equation34 / num8 * num10 * num7 + + equation56 * equation86 / equation18 + num20 * num7 + equation22 / equation18 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 
	equation94 = equation93 + num16 * num9 * equation33 / equation34 / num8 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation57 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation50 / equation21 * num1 / num9 
	equation95 = equation94 + num16 * num9 / num8 * equation33 / equation34 * equation33 / equation34 * num10 * num7 + equation32 / equation18 + num20 * num7 + equation35 / equation57 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation50 / equation21 * num1 / num9 
	equation96 = equation95 * equation2 * equation3 / equation4 / equation5 * equation76 + equation8 * equation7 + equation9 - equation10 * equation11 - equation13 * equation12 / equation14 * equation13 / equation17 * equation15 * equation14 / equation16 * equation18 * equation19 * equation20 * equation22 / equation21 * equation24 * equation28 / equation30 * equation31 / equation35 * equation32 * equation33 / equation34 + num2 + equation36 + num15 * num12 / num19 * num14 + equation21 * num1 / num9 * num12 / num19 * num14 + num17 * num12 / num9 * num12 / num19 * num14 + num17 * num12 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num1 * mul2 / num7 * num4 + num7 * num10 / num7 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation97 = equation96 + equation1 / num1 * num7 + equation28 / equation18 + num3 * num17 + equation19 / equation18 + num3 * num10 *mul3 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num7 * num10 / equation19 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation98 = equation97 * num7 + equation12 / equation29 + num3 +randomnum4 / randomnum1+ num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation99 = equation98 + num10 * num9 / num8 * num10 * num7 + equation19 / equation18 + num20 * num7 + equation22 / equation30 + num3 * num10 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * num10 / num7 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num16 * num2 * num10 / num7 * num4 + num7 * equation20 / num17 * num20 + num18 * num10 / num7 * num15 + num17 * num10 / num3 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num9 
	equation100 = equation1 * equation2 * equation3 / equation4 / equation93 * equation76 + equation8 * equation7 + equation89 - equation10 * equation11 - equation13 * equation12 / equation14 * equation13 / equation17 * equation15 * equation14 / equation16 * equation18 * equation19 * equation20 * equation22 / equation21 * equation24 * equation28 / equation30 * equation31 / equation35 * equation32 * equation33 / equation34 + num2 * equation98 / equation99 + equation36 + num15 * num12 / num19 * num14 + equation21 * num1 / num9 * num12 / num19 * num14 + num17 * num12 / num9 * num12 / num19 * num14 + num17 * num12 / num9 + num3 * equation96 / equation94 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 * equation99 / equation94 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 * equation33 / equation34 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 * equation33 / equation34 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 * equation33 / equation34 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 * equation83 / equation4 / num13 * num16 + num13 * num12 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 * equation33 / equation34 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num1 * mul2 / num7 * num4 + num7 * num10 / num7 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 + num3 * num10 * mul2 / num7 * num4 + num7 * num10 / num17 * num2 + num18 * mul1 * num10 / num17 * num15 + num17 * num10 / num13 * num16 + num13 * num12 / num19 * num14 + num17 * num12 / num6 * num2 * num1 / num7 * num4 + num7 * num10 / num17 * num20 + num18 * num10 / num7 * num5 + num7 * num10 / num3 * num16 + num15 * num12 / num19 * num14 + equation2 * num1 / num9 
	equation201 = num1 * randomnum2 + equation100 * equation90 / equation89

def benchamrkc2():
	benchmarkc()
	benchmarkc()
def benchmarkc4():
	benchamrkc2()
	benchamrkc2()
def benchmarkc8():
	benchmarkc4()
	benchmarkc4()
def benchmarkc16():
	benchmarkc8()
	benchmarkc8()
def benchmarkc32():
	benchmarkc16()
	benchmarkc16()
def benchmarkc64():
	benchmarkc32()
	benchmarkc32()
def benchmarkc128():
	benchmarkc64()
	benchmarkc64()
def benchmarkc256():
	benchmarkc128()
	benchmarkc128()
def benchmarkc512():
	benchmarkc256()
	benchmarkc256()
def benchmarkc1024():
	benchmarkc512()
	benchmarkc512()
def benchmarkc2048():
	benchmarkc1024()
	benchmarkc1024()
def benchmarkc4096():
	benchmarkc2048()
	benchmarkc2048()
def benchmarkc8192():
	benchmarkc2048()
	benchmarkc2048()
def benchmarkc16000():
	benchmarkc8192()
	benchmarkc8192()
	
def benchmark():
	print("starting benchmark...")
	starttime1 = time.time()
	benchmarkc16000()
	benchmarkc16000()
	benchmarkc16000()
	endtime1 = time.time()
	starttime2 = time.time()
	key = load_key()
	encrypt("b.dat", key)
	encrypt("b.dat", key)
	encrypt("b.dat", key)
	encrypt("b.dat", key)
	encrypt("b.dat", key)
	decrypt("b.dat", key)
	decrypt("b.dat", key)
	encrypt("b.dat", key)
	decrypt("b.dat", key)
	decrypt("b.dat", key)
	decrypt("b.dat", key)
	decrypt("b.dat", key)
	endtime2 = time.time()
	time1 = endtime1 - starttime1
	time2 = endtime2 - starttime2
	totaltime = time1 + time2 
	if totaltime <= 1.9:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 450
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 2.2:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 2.4:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 2.6:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 2.8:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 3:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 3.2:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 3.4:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 3.6:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 3.8:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 4:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 6.2:
		scoretime = totaltime - 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	elif totaltime <= 8.4:
		scoretime = totaltime + 0.1
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
	else:
		scoretime = totaltime - 0.5
		total = 85000 - scoretime * 400
		print("benchmark has finished")
		print("the score is: %1.0f" % total)
		print("time taken: %0.4f" % totaltime)
#info
def infotools():
	while True:
		infointer='''
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

1)nmap
99)exit
>'''
		ch=int(input(infointer))
		if ch==1:
			nmap()
		elif ch==99:
			break
#stress
def stresstools():
	stressinter='''
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

1)httpslowreq
2)hulk DoS tool
3)Fire Rain DoS tool
4)benchmark
99)exit
>'''
	while True:
		c=int(input(stressinter))
		if c==1:
			web=input('input website>')
			os.system('python tools/httpslowreq.py %s'%web)
		elif c==2:
			dos()
		elif c==3:
			web=input('input website>')
			os.system('python2 tools/FR.py %s'%web)
		elif c==4:
			benchmark()
		elif c==99:
			break


def entro():
	na=input('input filename>')
	f=open(na,"w+")
	v1=[input('birthyear last two digits>'),input('name of person>'),input('name of important person>'),input('favourite character or idol>'),input('favourite sports team or game>'),input('name of favourite animal>'),input('another important word>'),input('another important number>')]
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
	don=255
	n1=0
	while True:
		n2=0
		n3=0
		if n1<=7:
			n2=0
			n3=0
			while True:
				if n2<=7:
					n3=0
					while True:
						if n3<=7:
							n4=0
							while True:
								if n4<=7:
									fa.write(v1[n1]+v1[n2])
									fa.write('''
''')
									fa.write(v1[n1]+v1[n2]+v1[n3])
									fa.write('''
''')
									fa.write(v1[n1]+v1[n2]+v1[n3]+v1[n4])
									fa.write('''
''')
									os.system('clear')
									print('''
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
''')
									don+=3
									do=don/12543*100
									print('wordlist is %0.1f percent completed'%do)
									print('%1.0f words completed'%don)
									n4+=1
								else:
									break
							n3+=1
						else:
							break
					n2+=1
				else:
					break
			n1+=1
		else:
			fa.close()
			break


def kitpasscrack():   
	hashf=input('hash file>')
	hashsalt=input('hash salt>')
	dic=input('password list file>')
	os.system('python2 tools/kitcrack.py -f %s'%hashf+' -s %s'%hashsalt+' -d %s'%dic)
def passtools():
	passinter='''
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

1)crunch
2)Entrophic password generator
3)Kit password cracker
4)hash encoder
5)Hasher
99)exit
>''' 
	while True:
		i=int(input(passinter))
		if i==1:
			sleng=input('shortest length>')
			lleng=input('longest length>')
			pc=input('possible characters>')
			filen=input('output filename>')
			spec=input('specifications>')
			os.system('crunch %s'%sleng+' %s'%lleng+' %s'%spec+' %s'%pc+' -o %s'%filen)
		elif i==2:
			entro()
		elif i==3:
			kitpasscrack()
		elif i==4:
			Escolha()
		elif i==5:
			os.system('python3 hash.py')
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
	mystring=input("\033[32mPLACE THE TEXT YOU WANT TO REVERSE\033[1;m: ")
	print("")
	print(' '.join(mystring.split()[::-1]))
	print("")
	Again("\n\033[1;36mWANTS TO MAKE ANOTHER REVERSE (y/n) ?:\033[1;m ", WordsReverseEncode)

def WordsReverseDecode():
	Apresentacao()
	mystring=input("\033[32mPLACE TEXT YOU WANT TO UNCOVER THE REVERSE\033[1;m: ")
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
	opcao1=input("\n\033[1;36m⟫⟫⟫\033[1;m ")
	if opcao1 == "1":
		ChamarBloco1()
	elif opcao1 == "2":
		ChamarBloco2()
	else:
		CifraDeCesar()


def cifrar(palavras, chave):
	abc="abcdefghijklmnopqrstuvwxyz "
	text_cifrado = ''

	for letra in palavras:
		soma=abc.find(letra)+chave
		modulo=int(soma)%len(abc)
		text_cifrado=text_cifrado+str(abc[modulo])

	return text_cifrado


def decifrar(palavras, chave):
	abc="abcdefghijklmnopqrstuvwxyz "
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
		cc=str(input('\n\033[32mTEXT TO BE DECODE\033[1;m: ')).lower()
		cn=int(input('\033[32mNUMERICAL KEY\033[1;m: '))
		print("\033[32mRESULT\033[1;m:", decifrar(cc, cn))
		print("")
	except:
		print("\n\n[\033[1;91m!\033[1;m] VALUE ERROR")
		sleep(3)
		ChamarBloco2()
	Again("\n\033[1;36mDESIRE TO DO ANOTHER DECODE IN CIPHER OF CESAR (y/n) ?:\033[1;m ", ChamarBloco2)

def dos():
	url=input('input url to DOS>')
	os.system('python2 tools/DOS.py %s'%url)

def repotools():
	while True:
		repointer='''
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
1)M1
99)exit
>'''
		typeinterm1='''
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
1)Android
2)Windows
3)Unix
4)Mac
99)exit
>'''
		andinter='''
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
1)Elite
2)Facebook
3)Mobelejen
4)Malum
5)Mobile_Legends_Adventure
6)Skygofree_pe
99)exit
>'''
		wininter='''
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
1)AntiExe
2)404
3)capslock
4)CMD
5)kuis
6)Matthieu
7)PCT
8)regeater
9)RIP
10)sleepy
11)ugly
99)exit
>'''
		unixinter='''
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
1)CitaM
2)trash
99)exit
>'''
		macinter='''
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
1)JacksBot
2)install
3)nothing
4)OceanLotus
5)trinoids
99)exit
>'''
		r=int(input(repointer))
		if r==1:
			while True:
				m=int(input(typeinterm1))
				if m==1:
					while True:
						andr=int(input(andinter))
						if andr==1:
							os.system('cp tools/M1/Android/elite.apk Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==2:
							os.system('cp tools/M1/Android/Facebook.apk Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==3:
							os.system('cp tools/M1/Android/Mobelejen.apk Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==4:
							os.system('cp tools/M1/Android/Malum.apk Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==5:
							os.system('cp tools/M1/Android/Mobile_Legends_Adventure.apk Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==6:
							os.system('cp tools/M1/Android/Skygofree_pe.jar Android/')
							print('')
							print('File copied into the Android directory')
						elif andr==99:
							break
						else:
							print('input not accepted')
				elif m==2:
					while True:
						windr=int(input(wininter))
						if windr==1:
							os.system('cp tools/M1/Win/AntiExe.A.zip Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==2:
							os.system('cp tools/M1/Win/404.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==3:
							os.system('cp tools/M1/Win/capslock.vbs Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==4:
							os.system('cp tools/M1/Win/CMD.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==5:
							os.system('cp tools/M1/Win/kuis.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==6:
							os.system('cp tools/M1/Win/Matthieu.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==7:
							os.system('cp tools/M1/Win/PCT.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==8:
							os.system('cp tools/M1/Win/regeater.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==9:
							os.system('cp tools/M1/Win/RIP.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==10:
							os.system('cp tools/M1/Win/sleepy.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==11:
							os.system('cp tools/M1/Win/ugly.bat Win/')
							print('')
							print('File copied into the Win directory')
						elif windr==99:
							break
						else:
							print('input not accepted')
				elif m==3:
					while True:
						unixr=int(input(unixinter))
						if unixr==1:
							os.system('cp tools/M1/Unix/CitaM Unix/')
							print('')
							print('File copied into the Unix directory')
						elif unixr==2:
							os.system('cp tools/M1/Unix/trash.sh Unix/')
							print('')
							print('File copied into the Unix directory')
						elif unixr==99:
							break
						else:
							print('')
							print('input not accepted')
				elif m==4:
					while True:
						macr=int(input(macinter))
						if macr==1:
							os.system('cp tools/M1/Mac/JacksBot.zip Mac/')
							print('')
							print('File copied into the Mac directory')
						elif macr==2:
							os.system('cp tools/M1/Mac/install Mac/')
							print('')
							print('File copied into the Mac directory')
						elif macr==3:
							os.system('cp tools/M1/Mac/nothing.app Mac/')
							print('')
							print('File copied into the Mac directory')
						elif macr==4:
							os.system('cp tools/M1/Mac/OceanLotus.zip Mac/')
							print('')
							print('File copied into the Mac directory')
						elif macr==5:
							os.system('cp tools/M1/Mac/trinoids.app Mac/')
							print('')
							print('File copied into the Mac directory')
						elif macr==99:
							break
						else:
							print('')
							print('input not accepted')
				elif m==99:
					break
				else:
					print('')
					print('input not accepted')
		elif r==99:
			break



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

1)encrypt
2)decrypt
99)exit
>'''
		while True:
			en=int(input(eninter))
			if en==1:
				enc(key())
			elif en==2:
				dec(key())
			elif c==99:
				break
			else:
				print('please input a number shown')
	elif c==5:
		repotools()
	elif c==99:
		break
	else:
		print('please input a prober number')
