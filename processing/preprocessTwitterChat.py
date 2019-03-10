#!/usr/bin/env python

import codecs
import numpy
import re

with codecs.open('TwitterLowerAsciiCorpus.txt','r') as f1:
	with codecs.open('Line1.txt','w') as w1:
		with codecs.open('Line2.txt','w') as w2:
			line = f1.readline()
			cnt = 1
			flag = 0
			while line:
				if len(line.strip()) == 0:
					if flag == 1:
						w2.write("\n")
						flag = 0
				else:
					if flag == 0:
						w1.write(line)
						flag = 1
					else:
						w1.write(line)
						w2.write(line)
				cnt = cnt + 1
				line = f1.readline()


with codecs.open('Line1.txt','r') as f1:
	with codecs.open('Line2.txt','r') as f2:
		with codecs.open('Result1.txt','w') as r1:
			with codecs.open('Result2.txt','w') as r2:
				line1 = f1.readline()
				line2 = f2.readline()
				while line1:
					if len(line2.strip()) != 0:
						re.sub('[^a-zA-Z0-9-_*()?!,.]', '', line1)
						re.sub('[^a-zA-Z0-9-_*()?!,.]', '', line2)
						r1.write(line1)
						r2.write(line2)
					line1 = f1.readline()
					line2 = f2.readline()