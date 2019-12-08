import time
from threading import Thread
import queue

def sequential():
    start = time.time()
    numofbells = 5
    count = 3
    base = ["123","213","231","321","312","132"]
    permlist = []

    while count < numofbells:
        ##Update list to have room for new bell
        for i in range(len(base)):
            for j in range(count + 1):
                permlist.append(base[i])
        
        count += 1
        temp = len(permlist)

        ##Add new bell
        for k in range(temp):
            cycle = count - (k % count)
            temp2 = permlist[k]
            temp2 = temp2[:cycle-1] + str(count) + temp2[cycle-1:]
            permlist[k] = temp2

        
        base = permlist
        permlist = []

    
    end = time.time()
    #print(base)
    print(" ")
    print("Sequential: ", end - start, " seconds.  ", numofbells, " bells.")


def pthread(base):
    permlist = []
    for i in range(len(base) + 1):
        permlist.append(base)

    return permlist

def parallel():
    start = time.time()
    numofbells = 5
    count = 3
    base = ["123","213","231","321","312","132"]
    que = queue.Queue()
    threads_list = list()
    permlist = []

    while count < numofbells:
        ##Update list to have room for new bell
        for i in range(len(base)):
            t1 = Thread(name="Thread-1", target=lambda q, arg1: q.put(pthread(arg1)), args=(que, base[i]))
            t1.start()
            threads_list.append(t1)

        for t in threads_list:
            t.join()
            permlist = permlist + que.get()

        threads_list = list()
        count += 1
        cycle = count
        temp = len(permlist)

        ##Add new bell
        for k in range(temp):
            temp2 = permlist[k]
            temp2 = temp2[:cycle-1] + str(count) + temp2[cycle-1:]
            permlist[k] = temp2

            if cycle == 1:
                cycle = count
            else:
                cycle -= 1
        
        base = permlist
        permlist = []
    
    end = time.time()
    ##print(base)
    print(" ")
    print("Parallel: ", end - start, " seconds.  ", numofbells, " bells.")



permlist = []

def snake(lst, insertVal, index):
    currentVal = lst[index]
    insLoc = (insertVal) - (index % insertVal)
    lst[index] = currentVal[:insLoc-1] + str(insertVal) + currentVal[insLoc-1:]

def parallel2():
    start = time.time()
    numofbells = 5
    count = 3
    base = ["123","213","231","321","312","132"]
    permlist = []
    threads = list()

    while count < numofbells:
        ##Update list to have room for new bell
        for i in range(len(base)):
            for j in range(count + 1):
                permlist.append(base[i])
        
        count += 1
        temp = len(permlist)

        ##Add new bell
        for k in range(temp):
            t = Thread(target=snake, args=(permlist, count, k,))
            t.start()
            threads.append(t)
        
        [t.join for t in threads]

        base = permlist
        permlist = []

    
    end = time.time()
    #print(base)
    print(" ")
    print("Parallel: ", end - start, " seconds.  ", numofbells, " bells.")



sequential()
parallel()
parallel2()