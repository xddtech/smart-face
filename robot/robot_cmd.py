from logger import Logger

log = Logger("robot_cmd")

def processAction(cmd, value):
   try:
      log.debug("cmd" + cmd);
   except Exception as ex:
      log.error("processAction - " + str(ex));
