
robot_postAction = function(action) {
   var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
         console.log('resp=' + this.responseText);
      }
   };
   xhttp.open("POST", "robot?action=" + action, true);
   xhttp.send();
}
