import threading
import time

start = time.perf_counter()

i = 0
sq = []


def func2(val):
    global i
    sq.append(val[i] ** 2)
    i += 1
    time.sleep(2)


Thread2 = []

for _ in range(5):
    t = threading.Thread(target=func2, args=[[1, 2, 3, 4, 5]])
    Thread2.append(t)
    t.start()
for _ in range(5):
    Thread2[_].join()
print(sq)


# def func(sec):
#     global i
#     #print(f'sleep {sec[i]} sec(s)')
#     i+=1
#     time.sleep(sec[i])
#
#     #print('Done sleeping')
#
# Threads=[]
#
# for _ in range(5):
#     t=threading.Thread(target=func,args=[[5,4,3,2,1]])
#     Threads.append(t)
#     t.start()
# for _ in range(5):
#     Threads[_].join()

# func(5)
# func(6)


end = time.perf_counter()

print(f'{end - start} seconds')
