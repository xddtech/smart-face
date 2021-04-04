
robot_postAction = function(action, value) {
   var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
         console.log('resp=' + this.responseText);
      }
   };
   var params = "action=" + action + "&value=" + value;
   xhttp.open("POST", "robot?" + params, true);
   xhttp.send();
}
