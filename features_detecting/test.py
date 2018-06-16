#!/usr/bin/python3

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay, i):
   count = 0
   print(i)
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, 1) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, 1) )
except:
   print ("Error: unable to start thread")
