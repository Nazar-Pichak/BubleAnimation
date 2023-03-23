import tkinter
import random
import time

colors = ["blue", "green", "yellow", "brown", "purple", "orange", "grey", 'powder blue', 'plum4', 'PowderBlue', 'RosyBrown4']
colour = random.choice(colors)

window = tkinter.Tk()
window.title("Buble Animation")
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.attributes('-fullscreen',True)

photo = tkinter.PhotoImage(file = r"C:\Users\Назар\Downloads\icons8-python-64.png")
window.iconphoto(False, photo)

canvas = tkinter.Canvas(window, width=width, height=height, bg='RoyalBlue4' )
canvas.pack()

circles = []

for i in range(20):
    colour = random.choice(colors)
    size = random.randint(50, 100)
    x = random.randint(200, 300 - size)
    y = random.randint(200, 300 - size)
    a = {}
    a["dx"] = random.randint(-1, 10)
    a["dy"] = random.randint(-1, 10)
    a["id"] = canvas.create_oval(x, y, x + size, y + size, fill=colour)
    circles.append(a)

try:
    while True:
        for circle in circles:
            x0, y0, x1, y1 = canvas.coords(circle['id'])
            if x0 < 0 or y0 < 0:
                circle["dx"] = -circle["dx"]
                circle["dy"] = -circle["dy"]
            if x1 > width or y1 > width and x1 > height or y1 > height:
                circle["dx"] = -circle["dx"]
                circle["dy"] = -circle["dy"]
            canvas.move(circle["id"], circle["dx"], circle["dy"])
        time.sleep(0.01)
        canvas.update()
        
except tkinter.TclError:
    window.mainloop()