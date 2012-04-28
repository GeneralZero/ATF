from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=False,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print  parser.parse_args()