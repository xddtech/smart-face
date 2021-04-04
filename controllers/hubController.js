const fs = require('fs');
const http = require('http');
const url = require('url');

const hubFile = 'public/hub/action.txt';
const startInfoFile = 'public/hub/startinfo.txt';
const emptyAction = {'action':'', 'value':''};

//http://localhost:3000/hub/action?lasttime=2615672679587.32
exports.getActionObject = (req, res) => {
   const params = url.parse(req.url,true).query;
   if (params && params.lasttime) {
      let lasttime = Number(params.lasttime);
      let stats = fs.statSync(hubFile);
      let filetime = stats.mtimeMs;
      if (filetime < lasttime) {
         //res.writeHead(404);
         //res.write('lasttime ' + lasttime + ' > filetime ' + filetime);
         res.send(emptyAction);
         return;
      }
   }
   const data = fs.readFileSync(hubFile, 'utf8')
   res.send(data);
}

//http://localhost:3000/hub/startinfo
//http://localhost:3000/hub/startinfo.txt
exports.getStartInfo = (req, res) => {
   const data = fs.readFileSync(startInfoFile, 'utf8')
   res.send(data);
}