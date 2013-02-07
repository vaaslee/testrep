# -*- coding: utf-8 -*-
import os
#
#
def echo(word):
	word=str(word)
	print word
#
com=raw_input()
com=com.split(">")
print com
print com[0]
print com[1]
if com[0]=="echo":
	echo(com[1])
else:
	print "Command error!"

