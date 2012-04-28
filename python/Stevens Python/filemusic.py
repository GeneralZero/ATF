import os 
import shutil
import sys
from UserDict import UserDict

def stripnulls(data):
    "strip whitespace and nulls"
    return data.replace("\00", "").strip()

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

class MP3FileInfo(FileInfo):
    "store ID3v1.0 MP3 tags"
    tagDataMap = {"title"   : (  3,  33, stripnulls),
                  "artist"  : ( 33,  63, stripnulls),
                  "album"   : ( 63,  93, stripnulls),
                  "year"    : ( 93,  97, stripnulls),
                  "comment" : ( 97, 126, stripnulls),
                  "genre"   : (127, 128, ord)}

    def __parse(self, filename):
        "parse ID3v1.0 tags from MP3 file"
        self.clear()
        try:                               
            fsock = open(filename, "rb", 0)
            try:                           
                fsock.seek(-128, 2)        
                tagdata = fsock.read(128)  
            finally:                       
                fsock.close()              
            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])               
        except IOError:                    
            pass                           

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)
        FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):                                        
    "get list of file info objects for files of particular extensions"
    fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]           
    fileList = [os.path.join(directory, f) 
               for f in fileList
                if os.path.splitext(f)[1] in fileExtList] 
    def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):      
        "get file info class from filename extension"                             
        subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]       
        return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
    return [getFileInfoClass(f)(f) for f in fileList]                             

if __name__ == "__main__":
	animename = ""
	filenumber = 0
	ext = ".mp3"
	com = ''
	infol = "C:\Downloads\Coldplay\Viva La Vida"
	outfol = "C:\Downloads\Coldplay\Viva La Vida\1"

	def ensure_dir(f):
		if not os.path.exists(f):
			os.makedirs(f)
			
	def movedirs(inf,outf):
		os.system("copy -f -r " + inf + " " + outf)
		os.system("del -f -r " + inf)

	for info in listDirectory("C:\Downloads\Coldplay\Viva La Vida", [".mp3"]):
		print info.items()[4][1]
		print info.items()[3][1]
		print info.items()[2][1][info.items()[2][1].find(infol[-3:])+4:]
		print (infol + '\\' + info.items()[2][1][info.items()[2][1].find(infol[-3:])+4:])
		#ensure_dir((outfol + info.items()[3][1] + ext))
		src = (infol + '\\' + info.items()[2][1][info.items()[2][1].find(infol[-3:])+4:])
		com =("copy \'" + src + "\' \'" + outfol[:-1] + '\\' + info.items()[3][1]+ ext + "\'")
		print com
		os.system(com)
		#ensure_dir("/mnt/server/Music/" + files[:placenumber])
		movedirs(infol + info.items()[2][1][info.items()[2][1].find(infol[-3:])+4:],outfol + '\\' + info.items()[3][1]+ ext)