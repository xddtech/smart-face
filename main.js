
const express = require('express')
const { exec } = require("child_process");
const fs = require('fs');

const log = require("./utils/Logger");

const app = express()

app.use(express.urlencoded({
  extended: false
}));
app.use(express.json());
app.use(express.static("public"));
app.use(express.static("robot/logs"));
app.set("view engine", "ejs")

app.set("port", process.env.SMART_PORT || 3000)


app.get('/', (req, res) => {
  res.render("index", {
    url: req.url,
    req: req
  });
})

const homeController = require("./controllers/homeController")
app.get("/camera", homeController.showCurrent);

const robotController = require("./controllers/robotController")
app.get("/robot", robotController.getInfo);
app.post("/robot", robotController.postAction);

const hubController = require('./controllers/hubController')
app.get('/hub/action', hubController.getActionObject);
app.get('/hub/startinfo', hubController.getStartInfo);

app.listen(app.get("port"), () => {
  log.info("======================================\n\n");
  log.info(`Server running at http://localhost:${app.get("port")}`);
  app_init();
})

app_init = function() {
   log.info('Initilize server application, OS: ' + process.platform);
   let cmd = 'ifconfig';
   if (process.platform.includes('32') || process.platform.includes('64')) {
     cmd = 'ipconfig';
   }

   exec(cmd, (error, stdout, stderr) => {
      if (error) {
         console.log(`error: ${error.message}`);
         return;
      }
      if (stderr) {
         log.error(`init failed to exec ${cmd}: ${stderr}`);
         return;
      }
      app_saveStartInfo(stdout);
   });
}

app_saveStartInfo = function(stdout) {
   const file = 'public/hub/startinfo.txt';
   log.info('Save start info to ' + file);
   let info = 'Smart Serve started at ' + new Date().toString();
   info = info + '\r\n========================================\r\n';
   fs.writeFile(file, info, function(err) {
      if (err) { log.error( "Failed to write startinfo file: " + err); }
   });

   let data = stdout;
   fs.writeFile(file, data, function (err) {
      if (err) { log.error( "Failed to write startinfo file: " + err); }
  });
}