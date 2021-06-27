import threading 
import time
import random

def hello(i):
  time.sleep(random.randint(1,10))
  print("hello world " + str(i) + " " + str(threading.get_ident()))

if __name__ == '__main__':
  for i in range(5):
    x = threading.Thread(target=hello, args=[i])
    x.start()