import time
import os;

class Logger:
  maxFileSize = 8000;
  totalLines = 0;
  # log level: 0 - DEBUG, 1 - INFO, 2 - ERROR
  logLevel = 0;

  def __init__(self, name):
     self.name = name;
     self.fileName = "logs/" + name + ".log";
     if not os.path.exists('logs'):
        os.makedirs('logs')
     file = open(self.fileName, "w");
     file.write("");
     file.close();

  def cleanLogFile(self):
     ofile = open(self.fileName, "r");
     lines = ofile.readlines();
     ofile.close();

     nfile = open(self.fileName, "w");
     i = 0;
     for line in lines:
        i += 1;
        if i > (self.totalLines/2):
           nfile.write(line);

     nfile.close();
     self.totalLines = self.totalLines / 2;

  def write(self, message):
     self.totalLines += 1;
     file = open(self.fileName, "a");
     file.write(message + "\n");

     file.close();

     if os.stat(self.fileName).st_size > self.maxFileSize:
        self.cleanLogFile();

  def log(self, level, message):
      line = time.strftime("%Y-%m-%d %H:%M:%S") + " - " + level + ": " + message;
      self.write(line);

  def info(self, message):
      if self.logLevel <= 1:
         self.log("INFO", message);

  def debug(self, message):
      if self.logLevel == 0:
         self.log("DEBUG", message);

  def error(self, message):
      self.log("ERROR", message);


