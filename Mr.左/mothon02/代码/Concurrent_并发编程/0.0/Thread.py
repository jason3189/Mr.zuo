from test import *
import threading
import time

jobs = []
st = time.time()
for i in range(10):
    t = threading.Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
print("Thread io:", time.time() - st)

# Thread io: 8.935524225234985
