

def saveFile(text, filename):
	with open(filename, 'a') as f:
		f.write(text)
	return

def process(lines):
	currLine = 0
	lastLine = len(lines)-1
	prompts = []
	responses = []
	lenOfLines = len(lines)
	while (currLine <= lastLine):
		convo = getCurrConvo(currLine, lines, lenOfLines)
		#print convo
		filteredConvo = filterRepeatedLines(convo)
		coalescedConvo = coalesceConvo(filteredConvo)
		#print "**********"
		#print filteredConvo
		#print "**********"
		#print coalescedConvo
		(newPrompts, newResponses) = getPromptsAndResponses(coalescedConvo)
		#print newPrompts
		#print newResponses
		#print "**********"
		prompts += newPrompts
		responses += newResponses
		currLine += len(convo)
	return (prompts, responses)		

def getCurrConvo(currLineInd, lines, lenOfLines):
	currLine = lines[currLineInd]
	currSender = lines[currLineInd][0]
	nextLineInd = currLineInd + 1
	lastSender  = ""
	# maybe check here if currReceiver is empty string, because if not then it's not the start of a convo
	while (nextLineInd < lenOfLines):
		nextLine = lines[nextLineInd]
		(s, r) = (nextLine[0], nextLine[1])
		if (currSender not in [s, r]):
			return lines[currLineInd:nextLineInd]
		else:
			nextLineInd += 1
	return lines[currLineInd:]

def filterRepeatedLines(convo):
	currLine = convo[0]
	res = []
	res.append(currLine)
	for l in convo[1:]:
		if (currLine[2] != l[2]):
			res.append(l)
		currLine = l
	return res

def coalesceConvo(convo):
	# this needs to be run after filterRepeatedLines(convo) because otherwise
	# it will combine identical / repeated lines
	currLine = convo[0]
	res = []
	res.append(currLine)
	for l in convo[1:]:
		if ((l[0] == currLine[0]) and (l[1] == currLine[1])):
			res[len(res)-1][2] += (" " + l[2])
		else:
			res.append(l)
			currLine = l
	return res

def getPromptsAndResponses(convo):
	lenOfConvo = len(convo)
	ps = []
	rs = []
	ps.append((convo[0])[2]) # sender, receiver, text
	for (i, l) in enumerate(convo[1:]):
		rs.append(l[2])
		if (i < lenOfConvo):
			ps.append(l[2])
        #print "************************"
        #print ps
        #print rs
        #print "************************" 
	return (ps, rs)

fs196 = ["partial196aa",
      "partial196ab",
      "partial196ac",
      "partial196ad",
      "partial196ae",
      "partial196af",
      "partial196ag",
      "partial196ah",
      "partial196ai",
      "partial196aj"]

fs301 = ["partial301aa",
         "partial301ab",
         "partial301ac",
         "partial301ad",
         "partial301ae",
         "partial301af",
         "partial301ag",
         "partial301ah",
         "partial301ai",
         "partial301aj",
         "partial301ak",
         "partial301al",
         "partial301am",
         "partial301an",
         "partial301ao",
         "partial301ap",
         "partial301aq",
         "partial301ar"]

for f in fs196:
	print f
	o = open(f)
	print "reading lines"
	ls = (o.readlines())
	if ("dialogueID" in ls[0]):
		print "removing first line in ", f
		ls = ls[1:]
	print "mapping lines now"
	op = map(lambda l: (((l.replace("\n","")).replace("\"","")).split(","))[3:], ls)
	print "processing lines now"
	(p,r) = process(op)
	print "saving files now"
	saveFile("\n".join(p), "prompts.txt")
	saveFile("\n".join(r), "responses.txt")        

(fn1, fn2, fn3) = ("dialogueText_196.csv", "dialogueText_301.csv", "dialogueText.csv")

(of1, of2, of3) = (open(fn1), open(fn2), open(fn3))

#(ls1, ls2, ls3) = ((of1.readlines())[1:], (of2.readlines())[1:], (of3.readlines())[1:])
ls1 = ((of1.readlines())[1:])#.replace("\n","").replace("\"","")
ls2 = ((of2.readlines())[1:])#.replace("\n","").replace("\"","")
ls3 = ((of3.readlines())[1:])#.replace("\n","").replace("\"","")

# 6 columns: _, _, _, fromUser, toUser, message

print "processing 1st file lines"
onlyParts1 = map(lambda l: (((l.replace("\n","")).replace("\"","")).split(","))[3:], ls1)


#for (p, r) in (process(onlyParts1), process(onlyParts2), process(onlyParts3)):
#	saveFile(p, "prompts.txt")
#	saveFile(r, "responses.txt")
print "processing 1st file"
(p, r) = process(onlyParts1)
#print p
#print r
print "saving 1st file"
saveFile("\n".join(p), "prompts.txt")
saveFile("\n".join(r), "responses.txt")


print "processing 2nd file lines"
onlyParts2 = map(lambda l: (((l.replace("\n","")).replace("\"","")).split(","))[3:], ls2)
print "processing 2nd file"
(p, r) = process(onlyParts2)
print "saving 2nd file"
saveFile(p, "prompts.txt")
saveFile(r, "responses.txt")


print "processing 3rd file lines"
onlyParts3 = map(lambda l: (((l.replace("\n","")).replace("\"","")).split(","))[3:], ls3)
print "processing 3rd file"
(p, r) = process(onlyParts3)
print "saving 3rd file"
saveFile(p, "prompts.txt")
saveFile(r, "responses.txt")
