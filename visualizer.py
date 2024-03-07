import tkinter as tk
import random

root = tk.Tk()
root.title('Insertion Sort Visualizer')

canvas = tk.Canvas(root, width=600, height=400, bg='Sky Blue')
canvas.pack(fill=tk.BOTH, expand=True)

#Generate random array
array = [random.randrange(1,100) for _ in range(random.randrange(20, 50))]

def draw_array(arr, highlight = -1):
    canvas.delete("all")
    bar_width = canvas.winfo_width() / len(arr)
    for i, val in enumerate(arr):
        x0 = i*bar_width
        y0 = canvas.winfo_height() - (val/max(arr) * canvas.winfo_height())
        x1 = (i + 1) * bar_width
        y1 = canvas.winfo_height()

        color = "pink" if i == highlight else "black"
        canvas.create_rectangle(x0,y0,x1,y1, fill=color)
    root.update_idletasks

draw_array(array)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        temp = arr[i]
        j  = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j-=1
            draw_array(arr, highlight=j+1)
            root.update()
            root.after(100)
        arr[j + 1] = temp
    draw_array(arr)



start_button = tk.Button(root, text="Start Sort", command=lambda: insertion_sort(array))
start_button.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
