# usr/bin/python3
# © Ezz-Kun (2020)
# Start : Wednesday 22 Apr 2020,- 23:00:00 WIB
# Finish : Thursday Apr 23 2020,- 16:07:19 WIB
# Hanya Orang Bodoh Yang Rikod Tuul Ampas Kaya gini :)
import re,argparse
import requests as r
from sys import argv
from urllib.parse import unquote
from os import system,remove

class DeoB(object):
	def __init__(self):
		self.temp = 'i.js'
	def normal(self,file,out):
		opes = open(file).read()
		try:
			s = re.sub(r'document.write','console.log',unquote(re.search(r"eval\(unescape\('.*?'\)\)\;",opes).group(0).split('(')[2].split(')')[0])).strip("'")
		except AttributeError:
			exit('[*] error searching for text')
		with open(self.temp,'w') as so:
			so.write(s)
			so.close()
		print('[*] Wait A Few Seconds')
		print('[*] Difficulty : Normal\n')
		system('node %s > %s'%(self.temp,out))
		system('cat '+out)
		remove(self.temp)
		print('\n[*] Oke Deob File : '+file)
		print('[*] File Saved As : '+out)
	def Hard(self,file,out):
		ope = open(file).read()
		try:
			# Mencari function Utama
			ser = unquote(re.findall(r"eval\(unescape\('.*?'\)\)\;",ope)[0].split('(')[2].split(')')[0].strip("'"))
			# Mencari Var pertama
			yis = unquote(re.findall(r"eval\(unescape\('.*?'\)\)\;",ope)[1].split('+')[0].split('(')[2].split(')')[0].strip("'")).replace('document.write','console.log')
			# Mencari inti
			inet = re.sub(r"[ ']","",re.findall(r"eval\(unescape\('.*?'\)\)\;",ope)[1].split('+')[1])
			# Mencari Penutup
			pen = unquote(re.findall(r"eval\(unescape\('.*?'\)\)\;",ope)[1].split('+')[-1].split('(')[1].split(')')[0].strip("'"))
		except AttributeError:
			exit('[*] error searching for text')
		with open(self.temp,'w') as f:
			f.write(ser+yis+inet+pen)
			f.close()
		print('[*] Wait A Few Seconds')
		print('[*] Difficulty : Extended\n')
		system('node %s > %s'%(self.temp,out))
		system('cat '+out)
		remove(self.temp)
		print('\n[*] Oke Deob File : '+file)
		print('[*] File Saved As : '+out)

try:
	parser = argparse.ArgumentParser(description='A Simple Deobfuscated Html (c) Ezz-Kun \nSite : https://www.smartgb.com/free_encrypthtml.php',formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-u','--url',help='deobfuscate with url to file',metavar='')
	parser.add_argument('-f','--file',help='deobfuscate only via file',metavar='')
	parser.add_argument('-o','--outp',help='output file to saving',metavar='')
	parser.add_argument('-e','--extend',help='deobfuscate with extend security',action='store_true')
	parser.add_argument('-n','--normal',help='deobfuscate with normal security',action='store_true')
	group = parser.add_argument_group('Additional:')
	group.add_argument('-c','--contact',help='Contact Author',action='store_true')
	group.add_argument('-v','--version',help='Show This Script Version',action='store_true')
	args = parser.parse_args()
	if args.url and args.file and args.outp and args.normal:
		ses = r.get(args.url).content
		with open(args.file,'wb') as f:
			f.write(ses)
			f.close()
		home = DeoB()
		home.normal(args.file,args.outp)
	elif args.file and args.outp and args.normal:
		home = DeoB()
		home.normal(args.file,args.outp)
	elif args.file and args.outp and args.extend:
		home = DeoB()
		home.Hard(args.file,args.outp)
	elif args.url and args.file and args.outp and args.extend:
		ses = r.get(args.url).content
		with open(args.file,'wb') as f:
			f.write(ses)
			f.close()
		home = DeoB()
		home.extend(args.file,args.outp)
	elif args.contact:
		system('xdg-open https://instagram.com/aditiaze_07/')
	elif args.version:
		print('Version : 2.1 (Fix) ')
	else:
		print('''Usage : python %s [options] [files]
Try   : python %s -h / --help for more info
Error : Missing Arguments Files or Url And Mode'''%(argv[0],argv[0]))
except EOFError:
	pass
