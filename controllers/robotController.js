const http = require('http');
const url = require('url');
const fs = require('fs');
const hubFile = "public/hub/action.txt";

exports.getInfo = (req, res) => {
   res.render("robot", {
    url: req.url,
    req: req
  });
}

exports.postAction = (req, res) => {
   const queryObject = url.parse(req.url,true).query;
   if (queryObject && queryObject.action) {
      console.log("action=" + JSON.stringify(queryObject))
      fs.writeFile(hubFile, JSON.stringify(queryObject), function (err) {
          if (err) { console.log( "Failed to write hub file: " + err); }
      });

      res.send("Received command: " + queryObject.action);
   } else {
      res.send("No action command");
   }
}
