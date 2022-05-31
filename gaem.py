from tkinter import Canvas, Scale, Tk, Toplevel, Button
from random import choice, randrange
import Objects

W_WIDTH = 1200
W_HEIGHT = 800
FRAMERATE = 17
COLORS = ['blue','red','black','cyan','magenta','green','blue','yellow','grey','brown','lime','teal','pink']
OBJECTS = []

#Gravity = 10


#  Create main window
w = Tk()
w.title('kulicka :)')
c = Canvas(width=W_WIDTH,height=W_HEIGHT)
c.pack()
w.resizable(False,False)

# //CHILD WINDOW

#Child W. methods

#  Slider
def slider_x(val):
    global Gravity
    Gravity = int(val)
def add_ball():
    global OBJECTS
    temp = Objects.Ball(f"ball{len(OBJECTS)+1}",c)
    temp.posx = randrange(W_WIDTH)
    temp.posy = randrange(W_HEIGHT)
    temp.color = choice(COLORS)
    OBJECTS.append(temp)


#  Create child window / controls
w_controls = Toplevel(w)
w_controls.geometry('400x600')
w_controls.title(f'{w.title()} - Controls')
w_controls.resizable(False,False)
ball_gravity_x = Scale(
    w_controls,
    from_=-100,
    to=100,
    orient='horizontal',
    label='Velocity (x)',
    command=slider_x

)

ball_gravity_y = Scale(
    w_controls,
    from_=-100,
    to=100,
    orient='horizontal',
    label='Velocity (y)',
    command=slider_x

)
btn_add_ball = Button(
    w_controls,
    text="Add Ball",
    command=add_ball
)

ball_gravity_x.set(10)
ball_gravity_y.set(10)
ball_gravity_x.pack()
ball_gravity_y.pack()
btn_add_ball.pack()

#  Window Methods
def exit_app():
    
    #  Dont even ask.
    try:
        w.destroy()
    except:
        pass
    try:
        w_controls.destroy()
    except:
        pass


#  Env methods
# def draw_circle(x:int,y:int) -> None:
#     c.create_oval(x,y,x+50,y+50, fill=ball1.color, tag='ball')

def check_edge_hit(obj):
    obj.get_center_pos()
    posx_adjust = ball_gravity_x.get()
    posy_adjust = ball_gravity_y.get()

    
    #  Check for edges
    if obj.posx + obj.size == W_WIDTH:
        obj.reverse_x = True
    elif obj.posx == 0:
        obj.reverse_x = False
    elif obj.posx + obj.size > W_WIDTH:
        posx_adjust = (obj.posx + obj.size) - W_WIDTH
        obj.reverse_x = True
    elif obj.posx - posx_adjust < 0:
        posx_adjust = 0
        obj.posx = 0
        obj.reverse_x = False

    if obj.posy + obj.size == W_HEIGHT:
        obj.reverse_y = True
    elif obj.posy == 0:
        obj.reverse_y = False
    elif obj.posy + obj.size > W_HEIGHT:
        posy_adjust = (obj.posy + obj.size) - W_HEIGHT
        obj.reverse_y = True
    elif obj.posy - posy_adjust < 0:
        posy_adjust = 0
        obj.posy = 0
        obj.reverse_y = False

    if obj.posx > W_WIDTH or obj.posx < 0: 
        obj.posx = 250
    if obj.posy > W_HEIGHT or obj.posy < 0:
        obj.posy = 250



    if obj.reverse_x:
        obj.posx -= posx_adjust
    else:
        obj.posx += posx_adjust

    if obj.reverse_y:
        obj.posy -= posy_adjust
    else:
        obj.posy += posy_adjust
        

    print(f"{obj.tag}: X {obj.posx} Y {obj.posy} Center {obj.centered_pos}")
    # obj.posx += ball_gravity_x.get()
    # obj.posy += ball_gravity_y.get()


def draw_scene() -> None:
    c.delete('all')
    for object in OBJECTS:
        object.draw()

def update():
    #  Hitbox code
    for object in OBJECTS:
        check_edge_hit(object)


def loop():
    update()
    draw_scene()
    c.after(FRAMERATE,loop)

w.protocol('WM_DELETE_WINDOW', exit_app)
w_controls.protocol('WM_DELETE_WINDOW', exit_app)
loop()

c.mainloop()