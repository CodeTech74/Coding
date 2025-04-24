import time
start_time = time.time()
x = 5
n = 0
while x > 0:
    if time.time() - start_time >= 5:
      break
    z = x * n
    print(f"{x} x {n} = {z}")
    n +=1 