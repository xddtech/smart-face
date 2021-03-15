import time
import threading
import robot_worker as robotWorker


def checkHubAction(ltime):
   return '';

#------------------------------------------------

if __name__ == "__main__": 
   rthread = threading.Thread(target=robotWorker.run, args=());
   rthread.start();

   lasttime = round(time.time() * 1000);

   i = 1
   while True:
      print("main " + str(i) + ', ' + str(lasttime));
      i = i + 1
      time.sleep(2);

      #action = checkHubAction(lastime);

      lasttime = round(time.time() * 1000);

   #-----------------------------------------------

rthread.join();
