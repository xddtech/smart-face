
// DEBUG: 0, INFO: 1, ERROR: 2

const fs = require('fs');
const logFile = "public/logs/server.log";
const logBakFile = "public/logs/server_bak.log";
const maxLogFileSize = 2000;

exports.logLevel = 0;

exports.info = (messgae) => {
   if (exports.logLevel <= 1)
      log("INFO", messgae);
}

exports.error = (messgae) => {
   log("ERROR", messgae);
}

 exports.debug = (messgae) => {
    if (exports.logLevel <= 0)
       log("DEBUG", messgae);
 }

function log(level, message) {
   let str =  getTimestamp() + " " + level + ": " + message + "\n";
   fs.appendFile(logFile, str, function (err) {
      if (err) { console.log( "Failed to write log file: " + err); }
   });
   var stats = fs.statSync(logFile);
   if (stats.size >= maxLogFileSize) {
      backupLogFile();
   }
}

function backupLogFile() {
   try {
      if (fs.existsSync(logBakFile)) {
         fs.unlinkSync(logBakFile);
      }
      fs.rename(logFile, logBakFile, (error) => {
         console.log("Failed to rename log bak file: " + error);
      });
    } catch(err) {
      console.error(err)
    }
}

function getTimestamp() {
   let now = new Date();
   let mm = '' + (now.getMonth() + 1);
   let dd = '' + now.getDate();
   let yyyy = now.getFullYear();

   let hh = '' + now.getHours();
   let mi = '' + now.getMinutes();
   let ss = '' + now.getSeconds();

   if (mm.length < 2) 
      mm = '0' + mm;
   if (dd.length < 2) 
      dd = '0' + dd;
   if (hh.length < 2)
      hh = '0' + hh;
   if (mi.length < 2)
      mi = '0' + mi;
   if (ss.length < 2)
      ss = '0' + ss;

   return [yyyy, mm, dd].join('-') + 'T' + [hh, mi, ss].join(':');
}