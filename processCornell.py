

# this file is for processing the cornell movie lines corpus

lines = open("movie_lines.txt").readlines()
convos = open("movie_conversations.txt").readlines()
splitter = " +++$+++ "
lineparts = map(lambda l: l.split(splitter), lines)
convoparts = map(lambda c: c.split(splitter), convos)

(linenums, linewords) = ([l[0] for l in lineparts], [l[-1].rstrip() for l in lineparts])
convosSeparate = [c[-1].rstrip() for c in convoparts]

linesByNum = dict()
pairs = dict()

for (lineNum, line) in zip(linenums, linewords):
	print lineNum, line
	linesByNum[lineNum] = line

for c in convosSeparate:
	linesInConvo = (c[2:-2]).split("', '")
	print linesInConvo
	for i, line in enumerate(linesInConvo[0:-1]):
		print i, line
		pairs[linesByNum[line]] = linesByNum[linesInConvo[i+1]]

