from tkinter import*
from random import choice, randint

scrw = 400
scrh = 300
time_delay = 100

class Ball:
    number = 20
    min_R = 15
    max_R = 40
    av_col = ['green', 'blue', 'red']
    def __init__(self):
        ''' —оздание шарика со случайными координатами на холсте с проверкой выхода за границы холста'''        
        R = randint(Ball.min_R, Ball.max_R)
        x = randint(0, scrw -2*R -1)
        y = randint(0, scrh- 2*R -  1)
        self._y = y
        self._x = x
        self._R = R         
        fillcolor = choice(Ball.av_col)
        self._avatar = cnvs.create_oval(x, y, x+2*R, y+2*R, width= 1,fill=fillcolor,  outline = fillcolor)        
        self._Vx = randint(-2,2)
        self._Vy = randint(-2,2)
    
    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        # отбой от вертикальных стенок
        if self._x < 0:
            self._x = 0
            self._Vx = -self._Vx
        elif self._x + 2*self._R >= scrw:
            self._x = scrw - 2*self._R -1
            self._Vx = -self._Vx
        # отбой от горизонтальных стенок
        if self._y < 0:
            self._y = 0
            self._Vy = -self._Vy
        elif self._y + 2*self._R >= scrh:
            self._y = scrh - 2*self._R - 1
            self._Vy = -self._Vy
        cnvs.coords(self._avatar, self._x, self._y,self._x+2*self._R, self._y+2*self._R)
class Gun: # пушка
    def __init__(self):
        self._x = 0
        self._y = scrh -1
        self._lx = 30
        self._ly = -30
        self_avatar = cnvs.create_line(self._x, self._y, self._x+self._lx, self._y + self._ly)
        
    def shoot(self): #выстрел
        shell = Ball()
        shell._R = 5
        shell._x =  self._x+self._lx
        shell._y = self._y + self._ly - shell._R
        shell._Vx =  self._lx/10 
        shell._Vy = self._ly/10        
        shell.fly()
        return shell
    
        
def init_game():
    ''' —оздание объектов-м€чиков дл€ игры и объекта-пушки '''
    global balls, gun, shell_fly
    balls = [Ball() for i in range(Ball.number)]    
    gun = Gun()
    shell_fly = []

def init_maim_window():
    global root, cnvs, scores_text, scores_value
    root = Tk()
    root.title('ѕушка')
    scores_value = IntVar()
    cnvs = Canvas(root, background = 'white', width=scrw, height= scrh )
    scores_text = Entry(root, textvariable = scores_value)     
    cnvs.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    cnvs.bind('<Button-1>', click_event_hand)
    
 
def timer_event():
    #print('“ик-так')
    #расчеты по времени
    for ball in balls:
        ball.fly()
    for shell in shell_fly:
        shell.fly()
    cnvs.after(time_delay,timer_event)    
  
  
def click_event_hand(event):
    global shell_fly
    shell = gun.shoot()
    shell_fly.append(shell)
    
    
     
if __name__ == '__main__':
    init_maim_window()
    init_game()
    timer_event()
    root.mainloop()
    print('≈ще разок?')