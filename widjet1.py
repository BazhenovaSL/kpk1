from tkinter import* 

def button1_command():
    print('Hello!!!!')

def print_hello(event):
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)
    me = event.widget 
    # äåéñòâèÿ ñ me
    if me == button1:
        print('hello')
    elif me == button2:
        print('Press but2')
    else:
        #âûçâàòü îøèáêó
        raise ValueError()
        

def init_main_win():
    global root, button1, button2, lab, text, sc
    
    root = Tk()

    button1 = Button(root,text='Êíîï÷èê1', command=button1_command) 
    button1.bind('<Button>', print_hello)
    

    button2 = Button(root,text ='Êíîï÷èê2')
    button2.bind('<Button>', print_hello) 
    variable= IntVar(0) 
    
    lab = Label(root, textvariable=variable) 
    sc = Scale(root, orient = HORIZONTAL, length = 300, from_=0, to=100, tickinterval=10,resolution=5, variable=variable ) # Øêàëà
    text=Entry(root, textvariable=variable) 
    for obj in  button1, button2, lab, sc, text :
        obj.pack() 
    
    
    
if __name__ == '__main__':
    init_main_win()
    
    
    root.mainloop()
