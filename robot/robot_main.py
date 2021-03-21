import time
from threading import Thread, Event
import robot_worker as robotWorker

#------------------------------------------------

event = Event();

global action;
action = ["main-action"];

#------------------------------------------------

def checkHubAction(ltime):
    action[0] = "check-" + str(ltime);

#------------------------------------------------

if __name__ == "__main__": 

   rthread = Thread(target=robotWorker.run, args=(event, action));
   rthread.start();

   lastTime = round(time.time() * 1000);

   i = 1
   while True:
      try:
          print("main " + str(i) + ', ' + str(lastTime));
          i = i + 1
          time.sleep(2);

          #action[0] = "main-action-" + str(i);
          checkHubAction(lastTime);

          lastTime = round(time.time() * 1000);

      except KeyboardInterrupt:
          event.set();
          break;
   #-----------------------------------------------

   rthread.join();
