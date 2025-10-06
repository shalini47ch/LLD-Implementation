#now the other way is to use a runnable interface
import threading
import time 
def my_task():
    for i in range(0,5):
        print(f"Runnable interface {threading.get_ident()} is running {i}")
        time.sleep(0.5)
#now the next step is the creation of threads
t1=threading.Thread(target=my_task)
t2=threading.Thread(target=my_task)
t1.start()
t2.start()

t1.join()
t2.join()