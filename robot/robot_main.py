import requests as httpReq
import time
from threading import Thread, Event
import json
from types import SimpleNamespace

import robot_worker as robotWorker
from logger import Logger


log = Logger("robot_main");

#------------------------------------------------

event = Event();

global action;
action = ["main-action", "value"];

#------------------------------------------------

def checkHubAction(ltime):
    action[0] = "";
    action[1] = str(ltime);
    URL = "http://localhost:3000/hub/action?lasttime=" + str(ltime);
    try:
       resp = httpReq.get(URL);
       if resp.status_code == 200:
          # log.info("resp=" + resp.text);
          actionJson = json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d));
          if actionJson.action:
             log.debug("actionJson=" + actionJson.action + ":" + actionJson.value);
             action[0] = actionJson.action;
             action[1] = actionJson.value;
       else:
          resp.raise_for_status();
    except Exception as ex:
        log.error(str(ex));

#------------------------------------------------

if __name__ == "__main__": 

   log.info("Start robot main");
   rthread = Thread(target=robotWorker.run, args=(event, action));
   rthread.start();

   # milli-seconds
   lastTime = round(time.time() * 1000);

   i = 1
   while True:
      try:
          log.info("main loop " + str(i));
          i = i + 1
          time.sleep(2);

          checkHubAction(lastTime);

          lastTime = round(time.time() * 1000);

      except KeyboardInterrupt:
          log.info("Stop on KeyboardInterrupt");
          event.set();
          break;
   #-----------------------------------------------

   rthread.join();
