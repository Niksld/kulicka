from tkinter import Canvas, Scale, Tk, Toplevel, Button
from random import choice, randrange
from time import sleep
import Objects

W_WIDTH = 1200
W_HEIGHT = 800
FRAMERATE = 30
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
def add_random_ball():
    global OBJECTS
    temp = Objects.Ball(f"ball{len(OBJECTS)+1}",c)
    temp.posx = randrange(W_WIDTH)
    temp.posy = randrange(W_HEIGHT)
    temp.reverse_x = choice([True,False])
    temp.reverse_y = choice([True,False])
    temp.color = choice(COLORS)
    OBJECTS.append(temp)

def click_add_ball(event):
    global OBJECTS
    temp = Objects.Ball(f"ball{len(OBJECTS)+1}",c)
    temp.posx = event.x
    temp.posy = event.y
    temp.reverse_x = choice([True,False])
    temp.reverse_y = choice([True,False])
    temp.color = choice(COLORS)
    OBJECTS.append(temp)

def clear_canvas():
    global OBJECTS
    OBJECTS.clear()


#  Create child window / controls
w_controls = Toplevel(w)
w_controls.geometry('400x600')
w_controls.title(f'{w.title()} - Controls')
w_controls.resizable(False,False)
velocity_x = Scale(
    w_controls,
    from_=0,
    to=100,
    orient='horizontal',
    label='Velocity (x)'
)

velocity_y = Scale(
    w_controls,
    from_=0,
    to=100,
    orient='horizontal',
    label='Velocity (y)'

)
btn_add_ball = Button(
    w_controls,
    text="Add Ball",
    command=add_random_ball
)

btn_clear_balls = Button(
    w_controls,
    text='Clear Canvas',
    command=clear_canvas   
)

velocity_x.pack()
velocity_y.pack()
btn_add_ball.pack()
btn_clear_balls.pack()

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
    posx_adjust = velocity_x.get()
    posy_adjust = velocity_y.get()

    
    #  Check for edges

    # X
    # Screen Border checks
    if obj.posx + obj.size == W_WIDTH:
        obj.reverse_x = True
    elif obj.posx == 0:
        obj.reverse_x = False
    # Check for hits that would miss the screen border
    elif (obj.posx + obj.size + posx_adjust) > W_WIDTH:
        posx_adjust = (obj.posx + obj.size) - W_WIDTH
        obj.reverse_x = True
    elif obj.posx - posx_adjust < 0:
        posx_adjust = 0
        obj.posx = 0
        obj.reverse_x = False

    # Y
    # Screen Border checks
    if obj.posy + obj.size == W_HEIGHT:
        obj.reverse_y = True
    elif obj.posy == 0:
        obj.reverse_y = False
    # Check for other hits
    elif (obj.posy + obj.size + posy_adjust) > W_HEIGHT:
        posy_adjust = 0
        obj.posy = W_HEIGHT - obj.size
        obj.reverse_y = True
    elif obj.posy - posy_adjust < 0:
        posy_adjust = 0
        obj.posy = 0
        obj.reverse_y = False

    if obj.posx+10 > W_WIDTH or obj.posx < 0: 
        obj.posx = 250
        print(f"{obj.tag} reset pos")
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
        
def check_object_hit(obj):
    global OBJECTS

    #check all objects for intercept
    for object in OBJECTS:
        if object == obj:
            continue

        if range(obj.posx,obj.posx+obj.size) in range(object.posx,object.posx+object.size):
            print('reversed')
            obj.reverse_x = not obj.reverse_x
            object.reverse_x = not obj.reverse_x 

def draw_scene() -> None:
    c.delete('all')
    for object in OBJECTS:
        object.draw()

def update():
    #  Hitbox code
    for obj in OBJECTS:
        check_object_hit(obj)
        check_edge_hit(obj)

def loop():
    update()
    draw_scene()
    c.after(FRAMERATE,loop)

w.protocol('WM_DELETE_WINDOW', exit_app)
w_controls.protocol('WM_DELETE_WINDOW', exit_app)
loop()

c.bind("<Button-1>", click_add_ball)
c.mainloop()