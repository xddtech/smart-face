const http = require('http');
const url = require('url');
const fs = require('fs');
const hubFile = "public/hub/action.txt";

const actionCache = {
   action: "",
   value: "",
   time: 0,
   timeString: ""
};

exports.getInfo = (req, res) => {
   res.render("robot", {
    url: req.url,
    req: req
  });
}

exports.getActionObject = (req, res) => {
   res.send(actionCache);
}

exports.postAction = (req, res) => {
   const queryObject = url.parse(req.url,true).query;
   if (queryObject && queryObject.action) {
      //console.log("action=" + JSON.stringify(queryObject))
      //fs.writeFile(hubFile, JSON.stringify(queryObject), function (err) {
      //    if (err) { console.log( "Failed to write hub file: " + err); }
      //});
      actionCache.action = queryObject.action;
      actionCache.value = queryObject.value;
      actionCache.time = (new Date()).getTime();  // in milliseconds
      actionCache.timeString = getTimestamp();

      res.send("Received command: " + queryObject.action);
   } else {
      res.send("No action command");
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
