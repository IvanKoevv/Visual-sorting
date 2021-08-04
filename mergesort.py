import time
def merge(data,start,mid,end,drawData,timeTick):
    p=start
    q=mid+1
    tempArray=[]

    for i in range(start,end+1):
        if p>mid:
            tempArray.append(data[q])
            q+=1
        elif q>end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1
    for p in range(len(tempArray)):
        data[start]=tempArray[p]
        start +=1

def mergeSort(data,drawData,timeTick,start,end):
    if start < end:
        mid=int((start + end)/2)
        mergeSort(data,drawData,timeTick,start,mid)
        mergeSort(data,drawData,timeTick,mid+1,end)
        merge(data,start,mid,end,drawData,timeTick)
        drawData(data, ['green' if x >= start and x < mid else 'yellow' if x==mid else 'blue' if x>mid and x<=end else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data,['red' for x in range(len(data))])