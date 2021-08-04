import time

def shellSort(data,drawData,TimeTick):
    gap = len(data) // 2

    while gap >0:
        i=0
        j=gap

        while j <len(data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            drawData(data, ["yellow" if x==j or x==i and gap>0 else "red" for x in range(len(data))])
            time.sleep(TimeTick)
            i+= 1
            j+= 1


            k=i
            while k - gap > -1:
                if data[k-gap] > data[k]:
                    data[k-gap], data[k] = data[k], data[k-gap]
                drawData(data, ["white" if x==(k-gap) or x==k else "red" for x in range(len(data))])
                time.sleep(TimeTick/10)
                k -=1
        gap //=2
        drawData(data, ["yellow" if x==gap and gap>0 else "red" for x in range(len(data))])
        time.sleep(TimeTick)
