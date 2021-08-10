import random
from tkinter import *
from tkinter import ttk
from sorting_algorithms.bubblesort import bubble_sort
from sorting_algorithms.mergesort import mergeSort
from sorting_algorithms.quicksort import quick_sort
from sorting_algorithms.selectionSort import selectionSort
from sorting_algorithms.insertionSort import insertionSort
from sorting_algorithms.shellsort import shellSort

root = Tk()
root.title("Sorting")
root.geometry("1280x720+200+80")
root.config(bg="#082A46")
selected_algorithm = StringVar()
data = []


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 570
    canvas_width = 1250
    x_width = canvas_width / (len(data))
    offset = 0
    spacing_bet_rect = 0
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 540

        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0 + 1, y0, x1, y1, fill=colorArray[i])
        # canvas.create_text(x0+10,y0,anchor=SW,text=str(data[i]),fill= "orange")
    root.update()


def StartAlgorithm():
    global data

    if algo_menu.get() == "Bubble sort":
        bubble_sort(data, drawData, speedscale.get())
        drawData(data, ["green" for x in range(len(data))])
    elif algo_menu.get() == "Merge sort":
        mergeSort(data, drawData, speedscale.get(), 0, len(data) - 1)
        drawData(data, ["green" for x in range(len(data))])
    elif algo_menu.get() == "Quick sort":
        quick_sort(data, 0, len(data) - 1, drawData, speedscale.get())
        drawData(data, ["green" for x in range(len(data))])
    elif algo_menu.get() == "Selection Sort":
        selectionSort(data, drawData, speedscale.get())
        drawData(data, ["green" for x in range(len(data))])
    elif algo_menu.get() == "Insertion Sort":
        insertionSort(data,drawData, speedscale.get())
        drawData(data, ["green" for x in range(len(data))])
    elif algo_menu.get() == "Shell Sort":
        shellSort(data,drawData,speedscale.get())
        drawData(data, ["green" for x in range(len(data))])






def Generate():
    global data
    print("Selected Algorithm " + selected_algorithm.get())
    minivalue = int(minscalevalue.get())
    maxivalue = int(maxlabelvalue.get())
    sizeevalue = int(sizevalue.get())

    data = []
    for _ in range(sizeevalue):
        data.append(random.randrange(minivalue, maxivalue + 1))
    drawData(data, ["#a90042" for x in range(len(data))])


mainlabel = Label(
    root, text="Algorithm : ", bg="red", width=10, fg="black", relief=GROOVE, bd=5
)
mainlabel.place(x=0, y=0)

algo_menu = ttk.Combobox(
    root,
    state="readonly",
    width=15,
    textvariable=selected_algorithm,
    values=["Bubble sort", "Merge sort", "Quick sort", "Selection Sort", "Insertion Sort", "Shell Sort"],
)
algo_menu.place(x=145, y=0)
algo_menu.current(0)

random_generate = Button(
    root,
    text="Generate",
    bg="red",
    relief=SUNKEN,
    activebackground="green",
    activeforeground="white",
    bd=5,
    width=10,
    command=Generate,
)
random_generate.place(x=1140, y=0)


sizevaluelabel = Label(
    root, text="Size : ", bg="red", width=8, fg="black", height=2, relief=GROOVE, bd=5
)
sizevaluelabel.place(x=0, y=60)

sizevalue = Scale(
    root,
    from_=0,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    relief=GROOVE,
    bd=2,
    width=15,
)
sizevalue.place(x=120, y=60)

minvaluelabel = Label(
    root, text="Min : ", bg="red", width=8, fg="black", height=2, relief=GROOVE, bd=5
)
minvaluelabel.place(x=240, y=60)
minscalevalue = Scale(
    root, from_=0, to=20, resolution=1, orient=HORIZONTAL, relief=GROOVE, bd=2, width=15
)
minscalevalue.place(x=360, y=60)

maxvaluelabel = Label(
    root, text="Max : ", bg="red", width=8, fg="black", height=2, relief=GROOVE, bd=5
)
maxvaluelabel.place(x=480, y=60)
maxlabelvalue = Scale(
    root,
    from_=1,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    relief=GROOVE,
    bd=2,
    width=15,
)
maxlabelvalue.place(x=600, y=60)

speedvaluelabel = Label(
    root, text="Speed : ", bg="red", width=8, fg="black", relief=GROOVE, bd=5
)
speedvaluelabel.place(x=400, y=0)
speedscale = Scale(
    root,
    from_=0.00050,
    to=1.0,
    resolution=0.00050,
    length=200,
    digits=5,
    orient=HORIZONTAL,
    relief=GROOVE,
    bd=2,
    width=10,
)
speedscale.place(x=520, y=0)

start = Button(
    root,
    text="Start",
    bg="red",
    relief=SUNKEN,
    activebackground="green",
    activeforeground="white",
    bd=5,
    width=10,
    command=StartAlgorithm,
)
start.place(x=1140, y=60)

canvas = Canvas(root, width=1250, height=570, bg="black")
canvas.place(x=10, y=130)

root.mainloop()
