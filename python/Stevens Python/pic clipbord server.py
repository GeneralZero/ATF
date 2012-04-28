import urllib2
class ToServer(object):
	def __init__(self):
		self.opener = urllib2.build_opener(urllib2.HTTPHandler)
		self.request = urllib2.Request('http://example.org', data='your_put_data')
		self.request.add_header('Content-Type', 'your/contenttype')
	def putToServer(self):
		self.request.get_method = lambda: 'PUT'
		self.url = opener.open(self.request)

	def getFromServer(self):
		
