import threading
from time import sleep, time
  
def loop(i, event):
    while not event.isSet():
      cntr = 0
      while cntr < 1000000:
        cntr += 1      
        store='handle some data etc.'
 
event = threading.Event()

print 'starting'
 
th1 = threading.Thread(target=loop, args=(1, event))
th1.start()
th2 = threading.Thread(target=loop, args=(2, event))
th2.start()
th3 = threading.Thread(target=loop, args=(3, event))
th3.start()
th4 = threading.Thread(target=loop, args=(4, event))
th4.start()

#th11 = threading.Thread(target=loop, args=(1, event))
#th11.start()
#th12 = threading.Thread(target=loop, args=(2, event))
#th12.start()
#th13 = threading.Thread(target=loop, args=(3, event))
#th13.start()
#th14 = threading.Thread(target=loop, args=(4, event))
#th14.start() 

print 'running...'

sleep(1000)

print 'stop...'

event.set()
 
th1.join()
th2.join()
th3.join()
th4.join()

print 'end'