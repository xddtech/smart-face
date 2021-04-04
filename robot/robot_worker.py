import time
from logger import Logger

log = Logger("robot_worker")

def run(event, action):
   log.info("Start robot worker");
   i = 1;
   while True:
      if event.is_set():
         break;
      if action[0]:
         log.info("worker loop " + str(i) + ": " + action[0] + "-" + action[1]);
      i = i + 1;
      time.sleep(4);
      