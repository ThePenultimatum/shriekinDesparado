#!/usr/bin/env python

import re
import nltk
import codecs

with codecs.open('movie_lines.txt','r') as fp:
	with codecs.open('A.txt','a') as a:
		with codecs.open('B.txt','a') as b:
			line = fp.readline()
			cnt = 1
			while line:
				line = re.sub('-','',line)
				line = re.sub('\\...','.',line)
				token = line.split()
				new = token[8:]
				out = " ".join(new)+"\n"
				out = re.sub('\\+\\+\\+\\$\\+\\+\\+','',out)
				if cnt%2 == 1:
					b.write(out)
				else:
					a.write(out)
				line = fp.readline()
				cnt += 1

cnt1 = 0
cnt2 = 0

with codecs.open('promptsAll.txt','r') as fp1:
	with codecs.open('p.txt','a') as a:
		line = fp1.readline()
		while line:
			if len(line.strip()) != 0:
				a.write(line)
			line = fp1.readline()
			cnt1 += 1

with codecs.open('responsesAll.txt','r') as fp2:
	with codecs.open('r.txt','a') as b:
		line = fp2.readline()
		while line:
			if len(line.strip()) != 0:
				b.write(line)
			line = fp2.readline()
			cnt2 += 1
