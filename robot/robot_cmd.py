from logger import Logger
import time
import robot_cmd_doer as cmdDoer

class CmdProcessor:
   log = Logger("robot_cmd")

   cmdAction = "";
   cmdValue = 0.0;

   def setCmdAction(self, cmd, value):
      try:
         if cmdDoer.isValid(cmd, value):
            self.cmdAction = cmd;
            self.cmdValue = float(value);
            self.log.debug("setCmd " + self.cmdAction + "/" + str(self.cmdValue));
      except Exception as ex:
         self.log.error("setCmdAction error - " + str(ex));

   def runCmd(self, cmdDiffTime):
      #self.log.debug("runCmd value=" + str(self.cmdValue));
      try:
         if self.cmdValue > 0:
            self.cmdValue = self.cmdValue - cmdDiffTime;
            # self.log.info("run cmd " + self.cmdAction + ": " + str(self.cmdValue));
            cmdDoer.doCommand(self.cmdAction, cmdDiffTime);
      except Exception as ex:
         self.log.error("runCmd error - " + str(ex));
