
from logger import Logger

log = Logger("robot_cmd_doer")

def isValid(cmd, value):
   if len(cmd) < 1:
      return False;
   return True;
   
# ------------------------------------------

def doCommand(cmd, value):
   log.info("do command-" + cmd + ": " + str(value));