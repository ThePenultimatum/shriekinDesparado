import json
import os
#from anytree import AnyNode
from string import printable          

allFS = os.listdir(".") 

fs = ["anotherSplitAFcd"]
abcs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

promptsById = dict()

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
			firstBody = str(filter(lambda c: c in printable, lineJson['body'])).strip()
			body = firstBody.split('\n')[0]
			tmp = body.split(" ")
			idval = str(filter(lambda c: c in printable, lineJson['id']))
			pid = str(filter(lambda c: c in printable, lineJson['parent_id'][3:]))
			if ((len(body) > 0) and (body[0] in abcs) and ("[removed]" not in body) and (body not in ["", " ", "\n", "\b", "\t", "\r\n"]) and (not body.isspace())):
				if (len(tmp) > 40):
					body = " ".join(tmp[:40])
				elif ("\n" in body):
					body = (body.split("\n"))[0]

				promptsById[idval] = body
				if (pid != "null"):
					responsesByParentId[pid] = body

		#iterating through responses because responses are what define a response - prompt pair. there could be more prompts overall than responses
		# so we only want to count the pairs
		for k, v in responsesByParentId.iteritems():
			if k in promptsById:
				pb = promptsById[k]
				if (len(pb) > 1) and (len(v) > 1): # and (not (pb.isspace() or v.isspace()))):
					prompts.append(pb)
					responses.append(v)
		oprompts = open("prompts.txt", 'a')
		oprompts.write("\n".join(prompts))
		oprompts.close()
		oresponses = open("responses.txt", 'a')
		oresponses.write("\n".join(responses))
		oresponses.close()
		i += 1

takeIdsAndText(allFS, ['parent_id','id','author','body'])
