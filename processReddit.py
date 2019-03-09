import json
import os
#from anytree import AnyNode
from string import printable          

allFS = os.listdir(".") 

fs = ["anotherSplitAFcd"]
abcs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#treeSoFar = AnyNode(id="root")
#parentIds = set()
#ids = set()
promptsById = dict()
#idsDoneAsResponses = dict()

def getRelevantVals(lineJson, fields):
	return [lineJson[i] for i in fields]

def takeIdsAndText(fs, columns):
    i = 0
    for f in fs:
		o = open(f)
		print i
		print f
		ls = o.readlines()
		# relevant columns: body, id, link_id, parent_id
		# in recent data, parentId is null for 

		res = []
		prompts = []
		responses = []
		responsesByParentId = dict()
		for l in ls:
			lineJson = json.loads(l)
			firstBody = str(filter(lambda c: c in printable, lineJson['body']))
			body = firstBody.replace("\n", " ")
			tmp = firstBody.split(" ")
			idval = str(filter(lambda c: c in printable, lineJson['id']))
			pid = str(filter(lambda c: c in printable, lineJson['parent_id'][3:]))
			if ((len(body) > 0) and (body[0] in abcs) and ("[removed]" not in body) and (body != "") and (not body.isspace())):
				if (len(tmp) > 40):
					body = " ".join(tmp[:40])

				promptsById[idval] = body
				if (pid != "null"):
					responsesByParentId[pid] = body
			#author = lineJson['author']
			#parentIds.add(lineJson['parent_id'][3:])
			#ids.add(lineJson['id'])
			#resLine = filter(lambda c: c in printable ,",".join(getRelevantVals(lineJson, columns)))
			#res.append(resLine)
		#text = "\n".join(res) #filter(lambda c: c in printable, "\n".join(res))
		#o.close()
		#newO = open(("new2_" + f), 'w')
		#newO.write(text)
		#newO.close()
		#allIds = promptsById.keys()
		for k, v in responsesByParentId.iteritems():
			if k in promptsById:
				prompts.append(promptsById[k])
				responses.append(v)
				#idsDoneAsResponses.append(k)
		oprompts = open("prompts.txt", 'a')
		oprompts.write("\n".join(prompts))
		oprompts.close()
		oresponses = open("responses.txt", 'a')
		oresponses.write("\n".join(responses))
		oresponses.close()
		i += 1

takeIdsAndText(allFS, ['parent_id','id','author','body'])
