import time
from logger import Logger
import robot_cmd as robotCmd

log = Logger("robot_worker")

def run(event, action):
   log.info("Start robot worker");
   i = 1;
   while True:
      if event.is_set():
         break;
      if action[0]:
         # log.debug("worker loop " + str(i) + ": " + action[0] + "-" + action[1]);
         robotCmd.processAction(action[0], action[1]);
         action[0] = "";
      i = i + 1;
      time.sleep(4);

# ------------------------------------------------

def processAction(cmd, value):
   try:
      log.debug("cmd" + cmd);
   except Exception as ex:
      log.error("processAction - " + str(ex));
      