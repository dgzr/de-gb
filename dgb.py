"""
Deobfuscated smartgb.com (free online html encrypt)
© 2021.04.02 ,- dtz-aditia
"""
import re
import os
import codecs
import logging
import argparse
import subprocess
import urllib.parse

class SmartGb(object):
	def __init__(self,file,out):
		if os.path.exists(out):
			logging.warning(f" output file -> {out} has already!")
			exit(1)
		else:
			self.out = out
		if file.endswith(".html"):
			if os.path.exists(file):
				self.target = open(file).read()
				if self.target.startswith("<html>"):
					self.__main__(self.target)
				else:
					logging.warning(f" + invalid file input! -> {file}")
			else:
				logging.warning(f" + cannot find file! -> {file}")
		else:
			logging.warning(" + file must be *.html! -> {file}")

	def __qriter__(self, **kwargs):
		try:
			if kwargs.get('name'):
				names = kwargs.get('name')
				if kwargs.get('content'):
					content = kwargs.get('content')
					if not isinstance(content, bytes):
						content = content.encode("utf-8")
				else:
					raise AssertionError(' Content is null!')
			else:
				names = 'out.js'
			with open(names,'wb') as f:
				f.write(
					content + b"\n")
			return " + file saved as -> {}".format(names)
		except EOFError:
			return False

	def __main__(self, target):
		try:
			if(res := re.search(r"eval\(unescape\('(?P<func>[^>]+?)'\)\)\;\neval\(unescape\('(?P<t>[^>]+?)'\)\s\+\s'(?P<str>[^>]+)\'\s\+\sunescape\('(?P<n>[^>]+)'\)\)",target)):
				logging.warning(
					f" Extended security detected !")
				q = res.groupdict()
				self.__qriter__(
					name="tmp.js",
					content=urllib.parse.unquote(
						q["func"]) + urllib.parse.unquote(
							q["t"]).replace("document.write","console.log") + q["str"] + urllib.parse.unquote(
								q["n"]))
				output = subprocess.Popen([
					"node","tmp.js"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
				os.remove("tmp.js")
				if(saved := self.__qriter__(
						name=self.out, content=output[0])):
					subprocess.call(["cat",self.out])
					logging.warning(saved)
				else:
					pass
			elif(res := re.search(r"eval\(unescape\('(?P<t>[^>]+?)'\)",target)):
				logging.warning(
					f" Normal security detected !")
				q = res.groupdict()
				if(saved := self.__qriter__(name=self.out,
						content=codecs.escape_decode(
							urllib.parse.unquote(
								q["t"]).removeprefix(
									"document.write('").removesuffix(
										"');"))[0])):
					subprocess.call(["cat",self.out])
					logging.warning(saved)
				else:
					pass
			else:
				logging.warning(
					f" invalid file input!")
		except Exception as e:
			logging.warning(
				str(e))

if __name__=="__main__":
	try:
		parser = argparse.ArgumentParser(
			formatter_class=argparse.RawTextHelpFormatter,description=" deobfuscate smartgb (html obfuscate)\n update 2021.04 © dtz-aditia")
		parser.add_argument("-f","--file",help="filename")
		parser.add_argument("-o","--out",help="output file")
		parser.add_argument("-v","--version",help="version tool",action="store_true")
		args = parser.parse_args()
		if args.file and args.out:
			SmartGb(
				args.file, args.out)
		elif args.version:
			logging.warning(" v2.2 2021.04")
		else:
			parser.print_help()
	except Exception as e:
		logging.warning(str(e))
