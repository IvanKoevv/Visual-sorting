import time


def partition(data, head, tail, drawData, TimeTick):
    border = head
    pivot = data[tail]

    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(TimeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, colorArray(len(data), head, tail, border, j, True))
            time.sleep(TimeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
        drawData(data, colorArray(len(data), head, tail, border, j))
        time.sleep(TimeTick)

    drawData(data, colorArray(len(data), head, tail, border, tail, True))
    time.sleep(TimeTick)
    data[border], data[tail] = data[tail], data[border]
    time.sleep(TimeTick)
    return border


def quick_sort(data, head, tail, drawData, TimeTick):
    if head < tail:
        p = partition(data, head, tail, drawData, TimeTick)
        quick_sort(data, head, p - 1, drawData, TimeTick)
        quick_sort(data, p + 1, tail, drawData, TimeTick)


def colorArray(dataLen, head, tail, border, currIdx, isswapping=False):
    colorArray = []
    for i in range(dataLen):

        if i >= head and i <= tail:
            colorArray.append("gray")
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] == "orange"
        elif i == border:
            colorArray[i] == "red"
        elif i == currIdx:
            colorArray[i] == "yellow"

        if isswapping:
            if i == border or i == currIdx:
                colorArray[i] = "green"
    return colorArray
