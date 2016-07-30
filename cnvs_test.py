from tkinter import*

def paint(event):
    # Обработка событий для холста
    print(event.x, event.y)
    if event.widget != cnvs:
        print('так не должно быть')
        return
    cnvs.coords(line, 0, 0, event.x, event.y)

root = Tk()

cnvs = Canvas(root, background = 'white', width=400, height= 400 )
cnvs.bind('<Motion>', paint)
cnvs.pack()

line = cnvs.create_line(0,0,10,10) # линия не виджет, она внутри холста, ее не надо паковать
for i in range(10):
    cnvs.create_oval(7+i*40, 7+i*40, i*40+20, i*40+20, fill='green', width= 4)


root.mainloop()
print('это будет при выходе из приложения')
