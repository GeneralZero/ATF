#Uses App directory of VLC Portable
#python
#VLC DVD and MEDIA COMMAND LINE CONVERTER iPod
import sys, os, subprocess
#Print Help
def Help():#HELP
    print "Help"
    print "[Source] [Destination] [Arguments]"
    print "Arguments"
    print "/? Help"
    print "/f Widescreen"
    print "/o Old iPods Non 640 (Resolution) Compatible"
    print "/d DVD"
    print "/y Automatically Overwrite a file if it already exists"
    print "/w Watch the source video while converting it"
    print "Format"
    print "For DVD support Use /d Arguments and for Source the title"
    os._exit(0)#Kill program instead of sys.exit which just ends this block and continues on. quit() gives errors in py2exe
if sys.argv[1]=="/?":
        Help()
if sys.argv[1]=='Help':
        Help()
path = os.path.dirname(sys.argv[0])
#DEFAULTS
try:
    a=sys.argv
except:
    print 'No Arguments Given'
    raw_input('No Command Line Arguments were given. Please Press ENTER to close')
    quit()
try:
    s=a[1]#Source
except:
    print 'No Source Destination Given'
    raw_input('Source Destination not given. Please Press ENTER to close')
    quit()
try:
    d=a[2]#Destination
except:
    print 'No Save Destination Given'
    raw_input('Save Destination not given. Please Press ENTER to close')
    quit()
widescreen='f'
old='f'# Default is New DVD unless arguments specify a need for old ipod compatible video
dvd='f'#DVD Var equals False
width='640'#Width and Height equal defaults of New iPod Fullscreen and unless needed arg present it doesn't change.
height='480'#Same^^
num='t'
overwrite='f'
watch=''
#DEFAULTS^^^
print s
print d  #Prints Source Destination Testing Purposes
try:# This Destects whether the source is a DVD title.
    temp=int(s)
except:
    num='f'
if num=='f':
    if not os.path.exists(str(s)):
        if not s[0]=='"':
            print 'Your source destination must be surrounded with qoutes.'
        if s[0]=='"':
            print "Your source destination doesn't exist."
        quit()
    if not os.path.exists(d):
        if not d[0]=='"':
            print 'Your save destination must be surrounded with qoutes.'
        '''
        if d[0]=='"':
            print "Your save destination doesn't exist."
        '''# Not needed for save destination becaouse it will be created only needed for source destination.
        quit()# End of wether the Source is a DVD Title
'''
if not s[0]== '"':#Block adds to Source "" if needed so if Source contains Spaces no errors will appear.
    s='"'+s
    if not s[-1]=='"':
        s=s+'"'
if not d[0]== '"':#Block adds to Destination "" if needed so if Destination contains Spaces no errors will appear.
    d='"'+d
    if not d[-1]=='"':
        d=d+'"'
'''
if os.path.exists(str(d)):#Detects wether the destination already exists
    temp=raw_input('The save destination you gave already exists do you want to overwrite it? Y/N')
    if temp[0]=='N':
        quit()#Program Quits
for i in a:#Goes through Arguments
    if i=="/f":#Widescreen
        widescreen='t'
        if not old=='t':#New iPod
            height=str('360')
            width=str('640')
        if old=='t':#Old iPod
            height=str('180')
            width=str('320')
    if i=="/o":#Old iPod
        old='t'
        if widescreen=='t':#Widescreen
            height=str('180')
            width=str('320')
        if not widescreen=='t':#Fullscreen
            height=str('240')
            width=str('320')
    if i=='/d':#DVD instead of File as Source
        dvd='t'
    if i=='/y':#Automatically Overwrite if destination exists
        overwrite='t'
    if i=='/w':#Watch while the Source is Converted. Slows down converting.... File by takes about 2 to 4 times longer. DVD and Network minimal length of time longer.
        watch='dst=display,'
if overwrite=='f':
    if os.path.exists(str(d)):#Detects wether the destination already exists
        temp=raw_input('The save destination you gave already exists do you want to overwrite it? Y/N')
        if temp[0]=='N':
            quit()#Program Quits        
drive='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in drive:#DVD Drive Destect Only Works for one drive. DVD Disk must be in.
    if os.path.exists(i+':\\VIDEO_TS'):
        dvddrive=i+':\\'
if dvd=='t':#DVD Ripping and Conversion #With Dimension Dection of VIDEO
    '''
    vlc='"'+path+'\App\\vlc\\vlc.exe" --intf dummy --dummy-quiet dvdsimple://'+dvddrive+'@'+s+' --file-logging --stop-time=2 vlc://quit'
    subprocess.Popen(vlc).wait()
    #python parse log VLC
    lines = [line.rstrip('\n') for line in file(r'C:\Windows\System32\vlc-log.txt')]
    global dim
    n=0
    for line in lines:
        n = n+1;
        if 'main debug: picture in ' in line:
            dim=n
    print dim
    '''
    VLC='"'+path+'\App\\vlc\\vlc.exe" --intf=dummy --dummy-quiet dvdsimple://'+dvddrive+'@'+s+' :sout=#transcode{vcodec=mp4v,vb=1024,height='+height+',width='+width+',scale=1,height='+height+',width='+width+',acodec=mp4a,ab=192,channels=2}:duplicate{'+watch+'dst=std{access=file,mux=mp4,dst="'+d+'.mp4"}} vlc://quit'#Were VLC is located and SOUT (Source OUT)
    print VLC
    subprocess.Popen(VLC).wait()#DVD
if dvd=='f':#File not DVD Ripping Conversion
    VLC='"'+path+'\App\\vlc\\vlc.exe" --intf dummy --dummy-quiet '+s+' :sout=#transcode{vcodec=mp4v,vb=1024,height='+height+',width='+width+',scale=1,height='+height+',width='+width+',acodec=mp4a,ab=192,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst='+d+'.mp4}} vlc://quit'#Were VLC is located and SOUT (Source OUT)'
    print VLC
    subprocess.Popen(VLC).wait()#File
#Cleans up VLC process...
print 'Cleaning up remnants... Garbage Collector'
    def GarbageCollector():
        subprocess.Popen('tskill vlc').wait()
    GarbageCollector()