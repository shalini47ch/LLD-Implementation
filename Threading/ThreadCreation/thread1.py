import threading 
import time 

#this thread creation is based on extending  the thread class
# the other ways are implementing the runnable interfaces or using callable

class MyThread(threading.Thread):
    def run(self):
        for i in range(0,5):
            print(f"Thread {threading.get_ident()} is running {i}")
            time.sleep(1.5)

#now the next step is to create and execute threads
t1=MyThread()
t2=MyThread() #here we have created two threads
t1.start()
t2.start()
#here the main thread pauses till t1 completes and once t1 completes then main thread pauses for t2 to complete
t1.join()
t2.join()

    