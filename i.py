import time

def dot():
  for i in range(6):
    print('                    iiiiiii')
    time.sleep(0.05)

def line():
  for i in range(18):
    print('                    IIIIIII')
    time.sleep(0.05)

while True:
  dot()
  print()
  time.sleep(0.05)
  print()
  time.sleep(0.05)
  line()
  print()
  time.sleep(0.05)
  print()
  time.sleep(0.05)
