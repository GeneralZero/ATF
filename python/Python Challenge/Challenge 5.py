import pickle, urllib

loaded = pickle.load(urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for a,b in enumerate(loaded):
	print ''.join(map(lambda pair: pair[0]*pair[1], b))
