class Ball:
    def __init__(self,tag:str,canvas_reference) -> None:
        self.posx = 0
        self.posy = 0
        self.reverse_x = False
        self.reverse_y = False
        self.color = 'red'
        self.c = canvas_reference
        self.tag = tag
        self.size=50
        # (x,y) - tuple
        self.centered_pos = self.get_center_pos()
        #self.centered_pos = ((self.posx+self.size)/2,(self.posy+self.size)/2)

    def draw_to(self,x:int, y:int) -> None:
        self.c.create_oval(x,y,x+self.size,y+self.size, fill=self.color, tag=self.tag)

    def get_center_pos(self) -> None:
        self.centered_pos = ((self.posx+self.size)/2,(self.posy+self.size)/2)

    def draw(self) -> None:
        self.c.create_oval(self.posx,self.posy,self.posx+self.size,self.posy+self.size, fill=self.color, tag=self.tag)
