import json

# Read a json file
# ==================
with open('a.json','r') as rfile:  #rfile = open('a.json','r') is less recommeneded because file has to be manually closed
    data_loaded = json.load(rfile)

print "The json read:",data_loaded

print data_loaded['a string']
print data_loaded['a list'][0]
print data_loaded['another dict']['foo']
print data_loaded['another dict']['key'][1]

with open('out.json','w') as outfile:
    json.dump(data_loaded,outfile)

print ('aaa')
print ("bbb")

