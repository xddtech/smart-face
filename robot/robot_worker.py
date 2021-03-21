import time


def run(event, action):

   i = 1;
   while True:
      if event.is_set():
         break;
      print("worker " + str(i) + ": " + action[0]);
      i = i + 1;
      time.sleep(4);
      