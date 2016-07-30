from tkinter import*
from random import choice, randint

ball_number = 20
ball_min_R = 15
ball_max_R = 40
ball_av_col = ['green', 'blue', 'red', 'yellow', 'magenta', 'gray', 'cyan', '#AA6500']

def click_ball(event):
    # ��������� ������� ����  ��� ���� ��������. �� ������  �� ������� ����������� �������� � ���������� �����      
    #(event.x, event.y)
    obj = cnvs.find_closest(event.x, event.y)
    x1, y1, x2, y2 = cnvs.coords(obj)   
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        cnvs.delete(obj)
        # ����� ��������� ����
        create_random_ball() # ��������� ����� �����
        
def move_all_balls(event):
    # ��������� ����������� �������
    for obj in cnvs.find_all():
        dx  = randint(-1,1)
        dy =  randint(-1,1)
        cnvs.move(obj, dx, dy)


def create_random_ball():
    ''' �������� ������ �� ���������� ������������ �� ������ � ��������� ������ �� ������� ������'''
    R = randint(ball_min_R, ball_max_R)
    x = randint(0, int(cnvs['width']) -2*R -1)
    y = randint(0, int(cnvs['height'])- 2*R -  1)
    
    cnvs.create_oval(x, y, x+2*R, y+2*R, fill=rnd_col(), width= 1)


def rnd_col():
    '''���������� ��������� ����'''
    
    return choice(ball_av_col)

def init_ball_catch_game():
    ''' �������� ������� ��� ����'''
    for i in range(ball_number):
        create_random_ball()

def init_maim_window():
    global root, cnvs
    
    root = Tk()
    cnvs = Canvas(root, background = 'white', width=400, height= 400 )
    cnvs.bind('<Button>', click_ball)
    cnvs.bind('<Motion>', move_all_balls)
    cnvs.pack()
    
    
    

if __name__ == '__main__':
    init_maim_window()
    init_ball_catch_game()
    root.mainloop()
    print('��� �����?')

