import time
from tkinter import Misc

def selectionSort(data, drawData, TimeTick):
    for i in range(len(data)):
        min_idx=i
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:
                min_idx= j
            drawData(data, ["white" if x==j else "blue" if x==min_idx else"red" for x in range(len(data))])
            time.sleep(TimeTick)

        data[i], data[min_idx] = data [min_idx], data[i]
        drawData(data, ["yellow" if x==i or x==min_idx else "red" for x in range(len(data))])
        time.sleep(TimeTick) 
