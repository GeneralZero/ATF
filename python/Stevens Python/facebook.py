#!/usr/bin/python
#
#   InFB - Information Facebook
#   Usage: infb.py user@domain.tld password
#   http://ruel.me
#
#   Copyright (c) 2010, Ruel Pagayon - ruel@ruel.me
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#       * Redistributions of source code must retain the above copyright
#         notice, this list of conditions and the following disclaimer.
#       * Redistributions in binary form must reproduce the above copyright
#         notice, this list of conditions and the following disclaimer in the
#         documentation and/or other materials provided with the distribution.
#       * Neither the name of ruel.me nor the names of its contributors
#         may be used to endorse or promote products derived from this
#         code without specific prior written permission.
#
#   THIS CODE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#   ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#   WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL RUEL PAGAYON BE LIABLE FOR ANY
#   DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#   (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#   ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#   CODE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
import sys, re, urllib, urllib2, cookielib
 
def main():
    if len(sys.argv) != 3:
        usage()
    user = sys.argv[1]
    passw = sys.argv[2]
 
    # Set needed modules
    CHandler = urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    browser = urllib2.build_opener(CHandler)
    browser.addheaders = [('User-agent', 'InFB - ruel@ruel.me - http://ruel.me')]
    urllib2.install_opener(browser)
    data = urllib.urlencode({
        'charset_test'  : urllib.unquote_plus('%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84'),
        'locale'        : 'en_US',
        'email'         : user,
        'pass'          : passw,
        'charset_test'  : urllib.unquote_plus('%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84'),
        'lsd'           : 'lcUCH'
    })
 
    # Initialize the cookies
    print 'Initializing..'
    res = browser.open('https://login.facebook.com/login.php?login_attempt=1')
    res.close()
 
    # Login
    print 'Logging in to account ' + user
    res = browser.open('https://login.facebook.com/login.php?login_attempt=1', data)
    rcode = res.code
    if not re.search('home\.php$', res.url):
        print 'Login Failed'
        exit(2)
    res.close()
 
    # Get Emails and Phone Numbers
    print "Getting Info..\n"
    flog = open(user + '.html', 'a')
    flog.write("<html>\n\t<head>\n\t\t<title>InFB - " + user + "</title>\n\t\t<link href=\"infb.css\" rel=\"stylesheet\" type=\"text/css\" />\n\t</head>\n\t<body>\n\t\t<div class=\"rby\">\n\t\t\t<table class=\"flist\">\n\t\t\t\t")
    page = 0
    while True:
        res = browser.open('http://m.facebook.com/friends.php?a&f=' + str(page))
        parp = res.read()
        m = re.findall('"\/friends\.php\?id=([0-9]+)&', parp)
        res.close()
        for i in m:
            prof = 'http://m.facebook.com/profile.php?id=' + i + '&v=info'
            res = browser.open(prof)
            cont = res.read()
            res.close()
            prof = prof.replace('m.', 'www.')
            ms = re.search('<div id="body"><div><div>(.*?)<\/div>', cont)
            if ms:
                name = ms.group(1)
            else:
                continue
            ms = re.search('href="tel:(.*?)"', cont)
            if ms:
                tel = ms.group(1)
            else:
                tel = ''
            ms = re.search('Emails?:<\/div><\/td><td valign="top"><div>(.*?)<\/div>', cont)
            if ms:
                email = re.sub('<br \/>', ', ', ms.group(1)).replace('&#64;', '@')
            else:
                continue
            print name + ' : ' + email + ' ' + tel
            flog.write("<tr class=\"lbreak\">\n\t\t\t\t\t<td class=\"num\">" + i + "</td><td class=\"fname\"><a href=\"" + prof + "\" title=\"" + name + "\">" + name + "</a></td><td class=\"fmail\">" + email + "</td></td><td class=\"cnum\">" + tel + "</td>\n\t\t\t\t\t</tr>\n\t\t\t\t")
        if re.search('Next', parp):
            page += 10
        else:
            break
    flog.write("\n\t\t\t</table>\n\t\t</div>\n\t</body>\n</html>")
    flog.close()
 
def usage():
    print 'Usage: ' + sys.argv[0] + ' user@domain.tld password'
    sys.exit(1)
 
if __name__ == '__main__':
    main()