#
def buildConnectionString(params):
	"""build a connection string from a dictionary of parameters"""
	return ";".join(["%s=%s" % (k,v) for k,v in params.items()])


if __name__ == "__main__":
	myParams = {"server":"mpilgrim",
				"database":"master",
				"uid":"sa",
				"pwd":"secret"
				}
	myParams.add("test":"tt")			
# print("%s=%s" % (k,v) for k,v in params.items())
	print (buildConnectionString(myParams))
	
	print (buildConnectionString(myParams))

