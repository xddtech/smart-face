import requests as httpReq
import time
import json
from types import SimpleNamespace

from logger import Logger
from robot_cmd import CmdProcessor


log = Logger("robot_main");
cmdProcessor = CmdProcessor();

#------------------------------------------------

global action;
action = ["main-action", "value"];

checkActionSleepTimeSec = 1;
runCmdSleepTimeSec = 0.5;
mainLoopSleepTime = 0.25;

#------------------------------------------------

def checkRobotAction(lastTime):
    URL = "http://localhost:3000/robot/action";
    try:
       resp = httpReq.get(URL);
       if resp.status_code == 200:
          actionJson = json.loads(resp.text, object_hook=lambda d: SimpleNamespace(**d));
          #log.debug("actionJson=" + resp.text);
          if actionJson.action and len(actionJson.action) > 0:
             if (actionJson.time > lastTime):
                action[0] = actionJson.action;
                action[1] = actionJson.value;
                log.debug("Received new action: " + action[0] + "/" + action[1]);
                #cmdProcessor.setCmdAction(action[0], action[1]);
                #cmdProcessor.setCmdAction(actionJson.action, actionJson.value);
                cmdProcessor.setCmdAction(action[0], str(action[1]));
       else:
          resp.raise_for_status();
    except Exception as ex:
        log.error("checkRobotAction - " + str(ex));

#------------------------------------------------

if __name__ == "__main__": 

   log.info("Start robot main");
 
   # milli-seconds
   lastTime = round(time.time() * 1000);
   checkActionStartTime = lastTime;
   runCmdStartTime = lastTime;

   while True:
      try:
         currentTime = round(time.time() * 1000);
         checkActionTimeDiff = (currentTime - checkActionStartTime) / 1000; #seconds
         if checkActionTimeDiff > checkActionSleepTimeSec:
            checkRobotAction(lastTime);
            lastTime = round(time.time() * 1000);
            checkActionStartTime = currentTime;

         currentTime = round(time.time() * 1000);
         runCmdTimeDiff = (currentTime - runCmdStartTime) / 1000; #seconds
         if runCmdTimeDiff > runCmdSleepTimeSec:
            cmdProcessor.runCmd(runCmdTimeDiff);
            runCmdStartTime = currentTime;

         time.sleep(mainLoopSleepTime);

      except KeyboardInterrupt:
          log.info("Stop on KeyboardInterrupt");
          break;
   #-----------------------------------------------

