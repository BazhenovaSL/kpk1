from tkinter import* 

def button1_command():
    print('Hello!!!!')

def print_hello(event):
    #print(event.keycode)
    print(event.num)
    print(event.x, event.y)
    #print(event.x_root, event.y_root)
    me = event.widget 
    # действия с me
    if me == button1:
        print('hello')
    elif me == button2:
        print('Press but2')
    else:
        #вызвать ошибку
        raise ValueError()
        

def init_main_win():
    ''' Инициализвция главного окна. Создание и упаковка виджетов'''
    global root, button1, button2, lab, text, sc
    
    root = Tk()

    button1 = Button(root,text='Кнопчик1', command=button1_command) # 'это кнопка с разными действиями для пробела и для кнопок мыши
    button1.bind('<Button>', print_hello)
    

    button2 = Button(root,text ='Кнопчик2')
    button2.bind('<Button>', print_hello) #Это кнопка с одинаковыми действиями для пробела и для кнопок мыши
    variable= IntVar(0) 
    
    lab = Label(root, textvariable=variable) #Значение положения ползунка
    sc = Scale(root, orient = HORIZONTAL, length = 300, from_=0, to=100, tickinterval=10,resolution=5, variable=variable ) # Шкала
    text=Entry(root, textvariable=variable) # Окно для  отображения или ввода  значений шкалы с точностью 5
    for obj in  button1, button2, lab, sc, text :
        obj.pack() # упаковка всех объектов
    
    
    
if __name__ == '__main__':
    init_main_win()
    
    
    root.mainloop()