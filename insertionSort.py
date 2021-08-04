import time

def insertionSort(data,drawData,TimeTick):
    for i in range(1,len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -=1
            drawData(data, ["yellow" if x==j or x==j+1 else "red" for x in range(len(data))])
            time.sleep(TimeTick)
        data[j+1] = key
        drawData(data, ["white" if x==i else "red" for x in range(len(data))])
        time.sleep(TimeTick)
