class Ball:
    def __init__(self,tag:str,canvas_reference) -> None:
        self.posx = 0
        self.posy = 0
        self.reverse_x = False
        self.reverse_y = False
        self.color = 'red'
        self.c = canvas_reference
        self.tag = tag
        self.size_x=50
        self.size_y=self.size_x
        # (x,y) - tuple
        self.centered_pos = self.get_center_pos()
        #self.centered_pos = ((self.posx+self.size)/2,(self.posy+self.size)/2)

    def draw_to(self,x:int, y:int) -> None:
        self.c.create_oval(x,y,x+self.size_x,y+self.size_y, fill=self.color, tag=self.tag)

    def get_center_pos(self) -> None:
        self.centered_pos = ((self.posx+self.size_x)/2,(self.posy+self.size_y)/2)

    def draw(self) -> None:
        self.c.create_oval(self.posx,self.posy,self.posx+self.size_x,self.posy+self.size_y, fill=self.color, tag=self.tag)
