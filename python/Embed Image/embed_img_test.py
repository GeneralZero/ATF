import re
import httplib

def get_html(url):
	data1 = None
	s_url =  re.findall(r'[http[s]?://]?([a-zA-Z0-9\.]+)/(.+)', url)
	print s_url
	s_url = s_url[0]
	conn = httplib.HTTPConnection(s_url[0])
	conn.request("GET", "/" + s_url[1])
	r1 = conn.getresponse()
	if r1.status == 200:
		data1 = r1.read()
	conn.close()
	return data1

def embed_js(html):
	arguments =  re.findall(r'<script.*[href=][\"\'](.*\.js.*)[\"\'].*>[</script>]?', html)
	print arguments
	for x in arguments:
		javascript = get_html('localhost' + x)
		if javascript:
			#print javascript
			html = re.sub(r'<script.*[href=][\"\'].*\.js.*[\"\'].*>[</script>]?', html, '<script>\n' + javascript +'\n</script>')
			print html
	return html

htmls = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Totoro</title>
		<link rel="stylesheet" type="text/css" href="/index.css"></link>
		<script href="/js/humane.min.js" ></script>
	</head>
	<body>
		<div id="Totoro">
			<div id="Text">
			</div>
		</div>
	</body>
</html>
'''

print embed_js(htmls)